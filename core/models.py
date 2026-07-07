class Employee:
    """Represents a unique enterprise employee identity."""
    def __init__(self, name: str, email: str):
        if not name or not name.strip():
            raise ValueError("Employee Name cannot be empty.")
        if not email or not email.strip():
            raise ValueError("Employee Email cannot be empty.")
        
        self.name = name.strip()
        self.email = email.strip().lower()

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.email == other.email
        return False

    def __hash__(self):
        return hash(self.email)


class Assignment:
    """Represents a validated Secret Santa relationship link."""
    def __init__(self, employee: Employee, secret_child: Employee):
        self.employee = employee
        self.secret_child = secret_child

    def to_dict(self) -> dict:
        return {
            "Employee_Name": self.employee.name,
            "Employee_EmailID": self.employee.email,
            "Secret_Child_Name": self.secret_child.name,
            "Secret_Child_EmailID": self.secret_child.email
        }