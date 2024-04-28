from number_writer.segmentwriter import SegmentWriter


class GermanSegmentWriter(SegmentWriter):
    """
    Writes a segment of numbers as text.
    """

    # special cases "eins/ein/eine"
    DIGITS = ['', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben',
              'acht', 'neun']
    # all teens are special - who would have thought!
    TEENS = ['zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn',
             'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn']
    # all multiples of ten are also special to us
    TENS = ['', '', 'zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig',
            'siebzig', 'achtzig', 'neunzig']

    HUNDRED_SUFFIX = 'hundert'
    PARTIAL_TENS_SEPERATOR = 'und'

    def to_text(self):
        """
        :return: this segment as text
        """
        hundreds = ""
        pre_digits = ""
        tens_separator = ""
        tens = ""
        digits = ""

        if self.hundreds:
            hundreds = self.DIGITS[self.hundreds] + self.HUNDRED_SUFFIX
        if self.tens:
            if self.tens == 1:
                tens = self.TEENS[self.units]
            else:
                if self.units:
                    pre_digits = self.DIGITS[self.units]
                    tens_separator = self.PARTIAL_TENS_SEPERATOR
                tens = self.TENS[self.tens]
        elif self.units:
            digits = self.DIGITS[self.units]

        return hundreds + pre_digits + tens_separator + tens + digits

