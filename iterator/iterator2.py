class TopThree:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 3:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopThree()

# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
print(values.__next__())

print(next(values))
print(next(values))
# print(next(values))
