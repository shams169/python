from abc import ABCMeta, abstractstaticmethod


class IChair(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_dimensions():
        pass


class BigChair(IChair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return f"Height: {self.height}, Width: {self.width} and Depth: {self.depth}"


class ChairFactory():

    @staticmethod
    def get_chair(chairType):
        try:
            if chairType == 'BigChair':
                return BigChair()
            raise AssertionError("Chair not found")
        except AssertionError as _e:
            print(_e)

if __name__ == '__main__':
    chair = ChairFactory.get_chair("BigChair")
    print(f'{chair.__class__} , {chair.get_dimensions()}')
