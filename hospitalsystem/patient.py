# Patient class 

class Patient:
    def __init__(self, fname, sname, triage_score):
        self._fname = fname
        self._sname = sname
        self._triage_score = triage_score
        self._time_in_queue = 0

    def __str__ (self):
        return "{} {}".format(self.get_fname(), self.get_sname())

    def __lt__ (self, other):
        if self.get_triage_score() < other.get_triage_score():
            return True
        elif self.get_triage_score() == other.get_triage_score():
            if self.get_time_in_queue() < other.get_time_in_queue():
                return True
    
    def __eq__(self, other):
        if self._fname == other._fname and self._sname == other._sname:
            return True

    def get_fname(self):
        return self._fname

    def get_sname(self):
        return self._sname

    def get_triage_score(self):
        return self._triage_score

    def get_time_in_queue(self):
        return self._time_in_queue
    
    def increase_time_in_queue(self):
        self._time_in_queue += 1