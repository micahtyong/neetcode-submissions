from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # Dict: { key: ([value_t1, value_t2], [t1, t2])}
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Handle case where key is new (set)
        if key not in self.d:
            self.d[key] = ([value], [timestamp])
        else:
        # Handle case where key has timestamp already (append)
            self.d[key][0].append(value)
            self.d[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # Handle case where key is not in dict
        if key not in self.d:
            return ""
        else:
        # Handle case where key is in dict (bisect timestamp list to find index)
        # Then index into first list
            # Binary search, O(log n)
            index = bisect_right(self.d[key][1], timestamp) - 1
            print(self.d[key], index)
            if index < 0: # Key was not defined at that timestamp
                return ""
            return self.d[key][0][index]
