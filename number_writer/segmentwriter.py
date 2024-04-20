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
    TENS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
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
        segment_as_text = ''

        if self.hundreds:
            segment_as_text = (self.DIGITS[self.hundreds]
                               + self.HUNDRED_SUFFIX)
            if self.tens or self.units:
                segment_as_text += self.PARTIAL_HUNDREDS_SEPERATOR

        if self.tens == 1:
            return segment_as_text + self.TEENS[self.units]
        elif self.tens > 1:
            segment_as_text += self.TENS[self.tens]
            if self.units:
                segment_as_text += self.PARTIAL_TENS_SEPERATOR

        segment_as_text += self.DIGITS[self.units]

        return segment_as_text
