class FlatIterator:

    def __init__(self, list_of_lists):
        self.stop = False
        self.result_list = list_of_lists
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stop:
            while self.i < len(self.result_list):
                if self.j < len(self.result_list[self.i]):
                    value = self.result_list[self.i][self.j]
                    self.j += 1
                    return value
                self.i += 1
                self.j = 0
            self.stop = True
        raise StopIteration





def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
