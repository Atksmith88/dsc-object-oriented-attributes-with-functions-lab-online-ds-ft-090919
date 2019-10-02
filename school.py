class School:
    def __init__(self, name = None):
        self.name = name
        self.roster = {}
    def add_student(self, name = None, grade = None):
        if str(grade) in self.roster.keys():
            self.roster[str(grade)].append(name)
        else:
            self.roster[str(grade)] = [name]
    def grade(self, grade):
        return self.roster[str(grade)]
    def sort_roster(self):
        for grade in self.roster.keys():
            self.roster[str(grade)].sort()
        return self.roster