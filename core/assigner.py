import random
from typing import List, Dict
from core.models import Employee, Assignment

class SecretSantaAssigner:
    """Core rules matrix processing algorithm enforcing non-self mapping and historical checks."""
    
    def __init__(self, employees: List[Employee], past_assignments: Dict[str, str]):
        self.employees = employees
        self.past_assignments = past_assignments

    def generate_assignments(self) -> List[Assignment]:
        if len(self.employees) < 2:
            raise ValueError("Secret Santa simulation requires at least 2 distinct employees.")

        max_attempts = 1000
        for attempt in range(max_attempts):
            pool = list(self.employees)
            random.shuffle(pool)
            
            assignments = []
            valid_run = True
            
            for giver in self.employees:
                # Filter candidates based on specific criteria
                valid_candidates = [
                    receiver for receiver in pool 
                    if receiver != giver and self.past_assignments.get(giver.email) != receiver.email
                ]
                
                if not valid_candidates:
                    valid_run = False
                    break  # Hit a dead end; reshuffle core pool and restart execution
                
                chosen_receiver = random.choice(valid_candidates)
                pool.remove(chosen_receiver)
                assignments.append(Assignment(giver, chosen_receiver))
                
            if valid_run:
                return assignments
                
        raise RuntimeError(
            "Allocation impossible. The historical rules or pool limits make it impossible "
            "to find a unique combination. Check your inputs."
        )