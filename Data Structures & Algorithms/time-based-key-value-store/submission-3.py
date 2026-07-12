class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))  # store timestamp first

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        L, R = 0, len(values) - 1
        result = ""

        while L <= R:
            mid = (L + R) // 2
            mid_timestamp, mid_value = values[mid]

            if mid_timestamp <= timestamp:
                result = mid_value     
                L = mid + 1             
            else:
                R = mid - 1

        return result