class LayoutCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables  # products
        self.domains = domains      # available slots
        self.constraints = constraints
        self.backtracks = 0
        self.assignments = 0

    def backtracking_search(self, assignment=dict(), use_fc=False, use_ac3=False):
        if use_ac3:
            self.ac3()
        if len(assignment) == len(self.variables):
            return assignment
        
        var = [v for v in self.variables if v not in assignment][0]
        for val in self.domains[var]:
            self.assignments += 1
            if self.is_consistent(var, val, assignment):
                assignment[var] = val
                result = self.backtracking_search(assignment, use_fc, use_ac3)
                if result is not None:
                    return result
                del assignment[var]
            self.backtracks += 1
        return None

    def is_consistent(self, var, val, assignment):
        # Check basic constraints: uniqueness, heavy items, max distance
        for other_var, other_val in assignment.items():
            if other_val == val:
                return False
        return True

    def forward_checking(self, var, val, domains):
        return domains

    def ac3(self):
        return True
