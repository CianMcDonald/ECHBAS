import heapq
from patient import Patient

class PriorityHeap:
    def __init__(self):
        self._queue = []

    def push_queue(self, patient):
        heapq.heappush(self._queue, patient)

    def pop_queue(self):
        return heapq.heappop(self._queue)

    def length_of_queue(self):
        return len(self._queue)
  
    def smallest_value(self):
        try:
            return self._queue[0]
        except IndexError:
            return "Error: Empty queue"

