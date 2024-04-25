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
    PARTIAL_HUNDREDS_SEPERATOR = ''

    def handle_hundreds(self):
        segment_as_text = self.DIGITS[self.hundreds] + self.HUNDRED_SUFFIX
        if self.tens or self.units:
            segment_as_text += self.PARTIAL_HUNDREDS_SEPERATOR
        if self.tens == 1:
            return segment_as_text + self.TEENS[self.units]
        elif self.tens > 1:
            if self.units:
                segment_as_text += (
                        self.DIGITS[self.units] + self.PARTIAL_TENS_SEPERATOR)
            return segment_as_text + self.TENS[self.tens]
        elif self.units == 1:
            return segment_as_text + "eins"
        else:
            return segment_as_text + self.DIGITS[self.units]

    def handle_tens(self):
        if self.tens == 1:
            return self.TEENS[self.units]
        else:
            segment_as_text = ""
            if self.units:
                segment_as_text += (self.DIGITS[self.units]
                                    + self.PARTIAL_TENS_SEPERATOR)

            return segment_as_text + self.TENS[self.tens]

    def handle_units(self):
        # if self.units == 1:
        #   "ein/eine/eins" depending on the order
        #   --> handle in german number_writer
        return self.DIGITS[self.units]
