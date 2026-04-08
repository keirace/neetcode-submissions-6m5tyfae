class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list) # {key: [[time, value], [time, value]]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap[key]
        l, h = 0, len(arr) - 1
        res = ''
        while l <= h:
            m = l+(h-l) // 2
            if timestamp == arr[m][0]:
                return arr[m][1]
            if timestamp > arr[m][0]:
                res = arr[m][1]
                l = m + 1
            else:
                h = m - 1
        return res