''' Iterator function that iterates by 1 until a maximum specified value'''

class Iterator:

    # initialize max and current values
    def __init__(self, maxIteration):
        self.maxIteration = maxIteration
        self.current = 0

    # returns the iterator object
    def __iter__(self):
        return self

    # iterates though
    def __next__(self):
        if self.current >= self.maxIteration:
            raise StopIteration

        self.current += 1
        return self.current