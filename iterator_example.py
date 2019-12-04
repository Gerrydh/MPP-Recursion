class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.length = len(string)

    def __iter__(self):
        return self
    
    def next(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            self.index +=1
        return self.string[self.index-1]

for c in StringIterator("Ger"):
    if c == "i":
        print("Found another 'e'!")
