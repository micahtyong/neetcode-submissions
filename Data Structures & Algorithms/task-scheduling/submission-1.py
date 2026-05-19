# Naive:
# Reminds me of defer_callback problem
#   - Used a min_heap where key: timestamp to dequeue, value: callable
# Treat tasks like a queue to call defer_callback
# - If we pop from the queue, any task w/ the same name must update priority
# - No native update method though... can do it lazily?
# - We should track current "timestamp", start at 0, and return that.
# - Basically if we cannot pop off the queue, we "sleep"
# - EAGERLY try to hit tasks that have most amount of duplicates
# - Waiting time n is constant for all tasks
# Space: O(m). Runtime: O(m log m)

# Min-Heap
# key: (-freq, next_valid_timestamp)
# value: task (e.g., "A")

# Pre-processing needed to get freq_dict { task_id: freq }

# When we pop element
# If freq < -1, just increment freq + timestamp and reinsert
# else, just remove elem
from collections import defaultdict
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Order: Process most frequent tasks first
        ts = 0
        freq_dict = defaultdict(int)
        for task in tasks: 
            freq_dict[task] += 1
        
        # Heap to manage what element to pop in or out.
        h = []
        for task_id, freq in freq_dict.items():
            h.append((-freq, task_id))
        heapify(h)

        # Cooldown dict that we process. heap: timestamp -> entry
        cooldown = [] 

        def cooldown_fwd():
            # See if anything from cooldown can be re-inserted in the queue
            while cooldown and cooldown[0][0] <= ts:
                heappush(h, heappop(cooldown)[1])

        # Process tasks.
        while len(h) > 0 or len(cooldown) > 0:
            # Heap is empty. Cooldown for 1 ts.
            if len(h) == 0:
                ts += 1
                cooldown_fwd()
                continue

            freq, task_id = heappop(h)
            ts += 1

            if freq < -1:
                elem = (freq + 1, task_id)
                heappush(cooldown, (ts + n, elem))
        
            cooldown_fwd()
        
        return ts
        


    def leastIntervalNaive(self, tasks: List[str], n: int) -> int:
        # no soln....
        timestamp = 0

        # Get frequency of tasks
        freq_dict = defaultdict(int)
        for task in tasks: 
            freq_dict[task] += 1
        
        # Build min_heap
        h = [] # Faster to heapify than call heappush n times
        for task_id, freq in freq_dict.items():
            # ((-freq, next_valid_timestamp), task)
            h.append(((-freq, 0), task_id))
        heapify(h)

        # Process CPU tasks
        while len(h) > 0:
            print("Heap:", h, "timestamp:", timestamp)

            # Find next available task to run
            i = -1
            for i in range(len(h)):
                next_available_timestamp = h[i][0][1]
                if timestamp >= next_available_timestamp:
                    break # Use current i
            
            # # If nothing available to run, just wait
            if i == -1:
                print("idle for this timestamp")
                timestamp += 1
                continue

            # Run the CPU task
            key, task_id = h.pop(i)
            heapify(h)
            neg_freq, next_valid = key
            if neg_freq < -1:
                neg_freq += 1
                next_valid = timestamp + 1 + n # wait n after this turn
                heappush(h, ((neg_freq, next_valid), task_id))
            # else case we do nothing and just remove the elemement!

            timestamp += 1
        
        return timestamp



        