class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])#it will run for again updates

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        result = ""
        for v, t in self.store[key]:
            if t <= timestamp:
                result = v
            else:
                break
        return result