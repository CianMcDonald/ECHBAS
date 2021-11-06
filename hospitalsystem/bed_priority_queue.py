import heapq
from patient import Patient

class PriorityHeap:
    def __init__(self):
        self._queue = []

    def push_queue(self, patient):
        heapq.heappush(self._queue, patient)

    def pop_queue(self):
        try:
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
        for pateint in names:
            name = pateint.split()
            to_remove = Patient(name[0], name[1], 0)
            self._queue.remove(to_remove)
        heapq.heapify(self._queue)
        print(self._queue)



