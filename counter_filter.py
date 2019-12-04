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

print filter((lambda x: (x%2) == 0), Counter(1, 100 ,1))
# the last 1 is the step
# below returns the odd numbers
print filter((lambda x: (x%2) != 0), Counter(1, 100 ,1))

print reduce((lambda x,y: x+y), Counter(1, 100, 1))