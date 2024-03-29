class MyIterator:
    def __init__(self, max_limit):
        self.max_limit = max_limit
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

a = MyIterator(4)
for i in a:
    print(i)