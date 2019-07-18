class School:
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster
    
    def add_student(self, full_name, grade_lvl):
        if grade_lvl in self.roster and full_name not in self.roster[grade_lvl]:
            self.roster[grade_lvl].append(full_name)
        else:
            self.roster[grade_lvl] = [full_name]
         
    def grade(self, grade_lvl):
        return self.roster[grade_lvl]
    
    
    def sort_roster(self):
        for i in self.roster:
            if isinstance(i, int):
                self.roster[i].sort()
        return self.roster
        
        