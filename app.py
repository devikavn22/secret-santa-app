import streamlit as st
import pandas as pd
import io
from core.io_handler import CSVHandler
from core.assigner import SecretSantaAssigner

# Streamlit Page Setup
st.set_page_config(page_title="Secret Santa Corporate Engine", page_icon="🎄", layout="centered")

st.title("🎄 Corporate Secret Santa Optimizer")
st.write("Upload your employee roster and historical datasets to generate constraint-validated pairings instantly.")

st.divider()

# Layout Columns for File Uploaders
col1, col2 = st.columns(2)

with col1:
    st.subheader("Current Roster")
    emp_file = st.file_uploader("Upload Current Employees (CSV)", type=["csv"], key="current")

with col2:
    st.subheader("History Constraints")
    past_file = st.file_uploader("Upload Past Allocations (Optional CSV)", type=["csv"], key="past")

st.divider()

if emp_file:
    if st.button("Generate Allocation Matrix", type="primary", use_container_width=True):
        try:
            with st.spinner("Processing allocation permutations..."):
                # 1. Parse File Contents via text memory strings
                emp_content = emp_file.getvalue().decode("utf-8")
                employees = CSVHandler.read_employees_from_string(emp_content)
                
                past_history = {}
                if past_file:
                    past_content = past_file.getvalue().decode("utf-8")
                    past_history = CSVHandler.read_past_assignments_from_string(past_content)
                
                # 2. Run Engine Permutation Operations
                engine = SecretSantaAssigner(employees, past_history)
                results = engine.generate_assignments()
                
                # 3. Standardize Object Layouts into Pandas Frame structures
                flat_data = [res.to_dict() for res in results]
                df_output = pd.DataFrame(flat_data)
                
                # 4. Write frame to buffer payload strings
                csv_buffer = io.StringIO()
                df_output.to_csv(csv_buffer, index=False)
                csv_string = csv_buffer.getvalue()
                
            st.success("🎉 Matrix optimized successfully with zero constraint failures!")
            
            # Interactive visual confirmation preview element
            st.subheader("Assignment Matrix Preview")
            st.dataframe(df_output, use_container_width=True)
            
            # Download Control Action Anchor
            st.download_button(
                label="📥 Download Allocations CSV",
                data=csv_string,
                file_name="secret_santa_assignments.csv",
                mime="text/csv",
                use_container_width=True
            )
            
        except ValueError as val_err:
            st.error(f"Data Validation Error: {str(val_err)}")
        except RuntimeError as run_err:
            st.error(f"Algorithmic Error: {str(run_err)}")
        except Exception as e:
            st.error(f"An unexpected internal error occurred: {str(e)}")
else:
    st.info("💡 Please upload the master Current Employee Roster CSV above to unlock matrix matching.")