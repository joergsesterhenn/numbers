class GermanSegmentWriter:
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
        # needs to be "eins" if it is in the lowest order only
        # --> handle in german_number_writer
        # needs to be "eine" if there are lower orders higher than 1
        # --> handle in german_number_writer
        return self.DIGITS[self.units]
