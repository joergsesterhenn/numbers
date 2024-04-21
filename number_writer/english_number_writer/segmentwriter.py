class SegmentWriter:
    """
    Writes a segment of numbers as text.
    """

    DIGITS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine']
    # all teens are special - who would have thought!
    TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    # all multiples of ten are also special to us
    TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
            'seventy', 'eighty', 'ninety']

    HUNDRED_SUFFIX = ' hundred'
    PARTIAL_TENS_SEPERATOR = ' '
    PARTIAL_HUNDREDS_SEPERATOR = ' and '

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

    def handle_hundreds(self):
        segment_as_text = self.DIGITS[self.hundreds] + self.HUNDRED_SUFFIX
        if self.tens or self.units:
            segment_as_text += self.PARTIAL_HUNDREDS_SEPERATOR
        if self.tens == 1:
            return segment_as_text + self.TEENS[self.units]

        return self.append_tens_and_units(
            segment_as_text, self.tens, self.units)

    def handle_tens(self):
        if self.tens == 1:
            return self.TEENS[self.units]
        else:
            return self.append_tens_and_units("", self.tens, self.units)

    def handle_units(self):
        return self.DIGITS[self.units]

    def append_tens_and_units(self, segment_as_text, tens, units):
        segment_as_text += self.TENS[tens]

        if tens > 1 and units:
            segment_as_text += self.PARTIAL_TENS_SEPERATOR

        return segment_as_text + self.DIGITS[units]
