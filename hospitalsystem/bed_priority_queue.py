import heapq
from patient import Patient
from copy import copy, deepcopy

class PriorityHeap:
    def __init__(self):
        self._queue = []

    def push_queue(self, patient):
        self.increase_time()
        heapq.heappush(self._queue, patient)
        

    def pop_queue(self):
        try:
            self.increase_time()
            return heapq.heappop(self._queue)
        except IndexError:
            return "Error: Empty queue"

    def length_of_queue(self):
        return len(self._queue)
  
    def smallest_value(self):
        try:
            return self._queue[0]
        except IndexError:
            return "Error: Empty queue"
    
    def remove_from_queue(self, names):
        """
            Takes list of "fname sname" removes patients from queue that match
        """
        for patient in names:
            name = patient.split()
            to_remove = Patient(name[0], name[1], 0)
            self._queue.remove(to_remove)
        self.increase_time()
        heapq.heapify(self._queue)

    def increase_time(self):
        for patient in self._queue:
            patient.increase_time_in_queue()

    def ordered_list(self):
        copied_queue = deepcopy(self)
        names = []
        while copied_queue.length_of_queue() != 0:
            names.append(copied_queue.pop_queue())
        return names


