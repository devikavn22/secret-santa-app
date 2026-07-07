# 🎄 Automated Corporate Secret Santa Matrix Engine

An enterprise-grade, constraint-aware Secret Santa allocation web tool built natively in Python using **Streamlit**. This system processes employee lists and validates historical datasets to instantly run conflict-free, randomized pairings.

## 🛠️ Software Engineering Architecture

This application balances development speed with production-grade engineering principles:
- **Clean Modular Layout:** Decoupled algorithms (`core/assigner.py`), core parsing structures (`core/io_handler.py`), and typed system objects (`core/models.py`).
- **Object-Oriented Design (OOP):** Strict validation handling within state classes.
- **Robust Algorithms:** Implements random graph derangements with automatic loop-break resolution to handle historical pairing restrictions.

## 🚀 Step-by-Step Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/secret-santa-app.git](https://github.com/YOUR_USERNAME/secret-santa-app.git)
   cd secret-santa-app



---------------------------------
## Folder structure

secret-santa-app/
│
├── .gitignore
├── README.md
├── requirements.txt
├── app.py                  # Streamlit UI & Application Entry Point
├── core/
│   ├── __init__.py
│   ├── models.py          # OOP Data Models
│   ├── io_handler.py      # Streamlit/In-Memory CSV Parsers
│   └── assigner.py        # Core Derangement Matching Algorithm
└── tests/
    ├── __init__.py
    └── test_assigner.py   # Automated Constraint Verification Tests



    