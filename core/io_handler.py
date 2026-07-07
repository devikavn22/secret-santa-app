# import csv
# import io
# from typing import List, Dict
# from core.models import Employee

# class CSVHandler:
#     """Handles parsing and validation of file streams inside the application framework."""
    
#     @staticmethod
#     def read_employees_from_string(content: str) -> List[Employee]:
#         if not content.strip():
#             raise ValueError("The provided employee CSV file is empty.")
            
#         employees = []
#         seen_emails = set()
#         f = io.StringIO(content)
#         reader = csv.DictReader(f)
        
#         required_fields = {"Employee_Name", "Employee_EmailID"}
#         if not reader.fieldnames or not required_fields.issubset(set(reader.fieldnames)):
#             raise ValueError("Invalid format. CSV must contain 'Employee_Name' and 'Employee_EmailID' headers.")

#         for idx, row in enumerate(reader, start=2):
#             name = row.get("Employee_Name", "").strip()
#             email = row.get("Employee_EmailID", "").strip().lower()
            
#             if not name or not email:
#                 raise ValueError(f"Row {idx} contains invalid data. Missing Name or Email ID.")
#             if email in seen_emails:
#                 raise ValueError(f"Row {idx} violation: Duplicate email identity found for '{email}'.")
                
#             seen_emails.add(email)
#             employees.append(Employee(name, email))
            
#         return employees

#     @staticmethod
#     def read_past_assignments_from_string(content: str) -> Dict[str, str]:
#         past_map = {}
#         if not content or not content.strip():
#             return past_map

#         f = io.StringIO(content)
#         reader = csv.DictReader(f)
        
#         required = {"Employee_EmailID", "Secret_Child_EmailID"}
#         if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
#             return past_map

#         for row in reader:
#             emp_email = row.get("Employee_EmailID", "").strip().lower()
#             child_email = row.get("Secret_Child_EmailID", "").strip().lower()
#             if emp_email and child_email:
#                 past_map[emp_email] = child_email
                
#         return past_map

import csv
import io
from typing import List, Dict
from core.models import Employee

class CSVHandler:
    """Handles parsing and validation of file streams inside the application framework."""
    
    @staticmethod
    def read_employees_from_string(content: str) -> List[Employee]:
        if not content.strip():
            raise ValueError("The provided employee CSV file is empty.")
            
        # FIX: Normalize potential Excel/QuillBot BOM artifacts and hidden carriage returns
        normalized_content = content.encode('utf-8').decode('utf-8-sig').replace('\r\n', '\n')
            
        employees = []
        seen_emails = set()
        f = io.StringIO(normalized_content)
        reader = csv.DictReader(f)
        
        # Strip any accidental whitespace from the detected headers
        if reader.fieldnames:
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
            
        required_fields = {"Employee_Name", "Employee_EmailID"}
        if not reader.fieldnames or not required_fields.issubset(set(reader.fieldnames)):
            raise ValueError(f"Invalid format. CSV must contain 'Employee_Name' and 'Employee_EmailID' headers. Found: {reader.fieldnames}")

        for idx, row in enumerate(reader, start=2):
            # Use stripped keys to safely fetch row data
            name = (row.get("Employee_Name") or "").strip()
            email = (row.get("Employee_EmailID") or "").strip().lower()
            
            if not name or not email:
                raise ValueError(f"Row {idx} contains invalid data. Missing Name or Email ID.")
            if email in seen_emails:
                raise ValueError(f"Row {idx} violation: Duplicate email identity found for '{email}'.")
                
            seen_emails.add(email)
            employees.append(Employee(name, email))
            
        return employees

    @staticmethod
    def read_past_assignments_from_string(content: str) -> Dict[str, str]:
        past_map = {}
        if not content or not content.strip():
            return past_map

        # FIX: Normalize potential Excel/QuillBot BOM artifacts here too
        normalized_content = content.encode('utf-8').decode('utf-8-sig').replace('\r\n', '\n')

        f = io.StringIO(normalized_content)
        reader = csv.DictReader(f)
        
        if reader.fieldnames:
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
        
        required = {"Employee_EmailID", "Secret_Child_EmailID"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            return past_map

        for row in reader:
            emp_email = (row.get("Employee_EmailID") or "").strip().lower()
            child_email = (row.get("Secret_Child_EmailID") or "").strip().lower()
            if emp_email and child_email:
                past_map[emp_email] = child_email
                
        return past_map