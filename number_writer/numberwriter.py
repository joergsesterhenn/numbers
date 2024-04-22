from abc import ABCMeta, abstractmethod

from number_writer.numbersegmenter import NumberSegmenter


class NumberWriter(metaclass=ABCMeta):
    """
    Writes a number as text.
    """
    def __init__(self, number: int):
        self.number = number
        self.number_segmenter = NumberSegmenter(number)

    @abstractmethod
    def to_text(self):
        """
        :return: the number as text
        """
        pass