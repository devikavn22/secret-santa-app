import pytest
from core.models import Employee
from core.assigner import SecretSantaAssigner

def test_secret_santa_strict_constraints():
    e1 = Employee("Hamish Murray", "hamish.murray@acme.com")
    e2 = Employee("Layla Graham", "layla.graham@acme.com")
    e3 = Employee("Matthew King", "matthew.king@acme.com")
    
    employees = [e1, e2, e3]
    # Enforce constraint: e1 cannot choose e2 (last year's pair match rule)
    past_history = {"hamish.murray@acme.com": "layla.graham@acme.com"}
    
    engine = SecretSantaAssigner(employees, past_history)
    assignments = engine.generate_assignments()
    
    assert len(assignments) == 3
    for assignment in assignments:
        # Self matching protection checks
        assert assignment.employee != assignment.secret_child
        # History mapping avoidance verification
        if assignment.employee.email == "hamish.murray@acme.com":
            assert assignment.secret_child.email != "layla.graham@acme.com"