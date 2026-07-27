class TimeMap:

    def __init__(self):
        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = {}
        if timestamp not in self.keys[key]:
            self.keys[key][timestamp] = [] 
        self.keys[key][timestamp].append(value)   

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        seen = 0
        for time in self.keys[key]:
            if time <= timestamp:
                seen = max(seen,time)
        return "" if seen == 0 else self.keys[key][seen][-1]
        