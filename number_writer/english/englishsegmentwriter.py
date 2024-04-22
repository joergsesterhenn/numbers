from number_writer.segmentwriter import SegmentWriter


class EnglishSegmentWriter(SegmentWriter):
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
