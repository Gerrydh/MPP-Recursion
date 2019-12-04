class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self
    
    def next(self):
        if self.current > self.high: #Stop condition of iteration
            raise StopIteration #Stop condition of iteration
        else:
            self.current += 1
        return self.current - 1

for i in Counter(10, 20):
    print i