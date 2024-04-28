from abc import ABCMeta, abstractmethod


class SegmentWriter(metaclass=ABCMeta):
    """
    Writes a segment of numbers as text.
    """
    def __init__(self, segment: str):
        """
        :param segment: needs to be a string consisting of three digits
        """
        self.hundreds = int(segment[0])
        self.tens = int(segment[1])
        self.units = int(segment[2])
