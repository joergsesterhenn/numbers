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
        hundreds = self.DIGITS[self.hundreds] + self.HUNDRED_SUFFIX
        hundreds_separator = ""
        tens = ""
        tens_separator = ""
        digits = ""
        if self.tens or self.units:
            hundreds_separator = self.PARTIAL_HUNDREDS_SEPERATOR
        if self.tens == 1:
            tens = self.TEENS[self.units]
            digits = ""
        elif self.tens > 1:
            tens = self.TENS[self.tens]
            if self.units:
                tens_separator = self.PARTIAL_TENS_SEPERATOR
                digits = self.DIGITS[self.units]
        else:
            digits = self.DIGITS[self.units]
        return hundreds + hundreds_separator + tens + tens_separator + digits

    def handle_tens(self):
        if self.tens == 1:
            return self.TEENS[self.units]
        else:
            segment = self.TENS[self.tens]
            if self.tens > 1 and self.units:
                segment += self.PARTIAL_TENS_SEPERATOR
            return segment + self.DIGITS[self.units]

    def handle_units(self):
        return self.DIGITS[self.units]
