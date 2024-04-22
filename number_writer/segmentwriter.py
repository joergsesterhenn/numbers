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

    def to_text(self):
        """
        :return: this segment as text
        """
        if self.hundreds:
            return self.handle_hundreds()
        elif self.tens:
            return self.handle_tens()
        elif self.units:
            return self.handle_units()

    @abstractmethod
    def handle_hundreds(self):
        """
        This method handles segments with hundreds.
        """
        pass

    @abstractmethod
    def handle_tens(self):
        """
        This method handles segments without hundreds.
        """
        pass

    @abstractmethod
    def handle_units(self):
        """
        This method handles segments with units only.
        """
        pass
