# Patient class 

class Patient:
    def __init__(self, fname, sname, triage_score):
        self._fname = fname
        self._sname = sname
        self._triage_score = triage_score

    def __str__ (self):
        return "{} {}".format(self.get_fname(), self.get_sname())

    def __lt__ (self, other):
        if self.get_triage_score() < other.get_triage_score():
            return True

    def get_fname(self):
        return self._fname

    def get_sname(self):
        return self._sname

    def get_triage_score(self):
        return self._triage_score