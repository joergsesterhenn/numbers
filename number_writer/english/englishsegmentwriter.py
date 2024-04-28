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

    def to_text(self):
        """
        :return: this segment as text
        """
        hundreds = ""
        hundreds_separator = ""
        tens = ""
        tens_separator = ""
        digits = ""

        if self.hundreds:
            hundreds = self.DIGITS[self.hundreds] + self.HUNDRED_SUFFIX
            if self.tens or self.units:
                hundreds_separator = self.PARTIAL_HUNDREDS_SEPERATOR
        if self.tens:
            if self.tens == 1:
                tens = self.TEENS[self.units]
            elif self.tens > 1:
                tens = self.TENS[self.tens]
                if self.units:
                    tens_separator = self.PARTIAL_TENS_SEPERATOR
                    digits = self.DIGITS[self.units]
        elif self.units:
            digits = self.DIGITS[self.units]

        return hundreds + hundreds_separator + tens + tens_separator + digits
