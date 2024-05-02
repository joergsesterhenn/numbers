from number_writer.german.germansegmentwriter import GermanSegmentWriter
from number_writer.numberwriter import NumberWriter


class GermanNumberWriter(NumberWriter):
    # names for multiples of thousand - we are counting with the long scale
    ORDERS_SUFFIX = ['', 'tausend', ' Million', ' Milliarde', ' Billion',
                     ' Billiarde', ' Trillion', ' Trilliarde', ' Quadrillion',
                     ' Quadrilliarde', ' Quintillion']

    SEPERATOR_OF_ORDERS = ' '

    def to_text(self):
        """
        :return: the number as text
        """
        # edge cases handled first
        if self.number == 0:
            return 'null'

        number_as_text = ''

        for order, segment in self.number_segmenter.segments():
            segment_as_text = GermanSegmentWriter(segment).to_text()
            if segment_as_text:
                order_separator = self.calculate_order_separator(order)
                is_plural, cardinal_singular_suffix = (
                    self.calculate_cardinal_singular_suffix(
                        order, segment_as_text))
                order_suffix = self.calculate_order_suffix(is_plural, order)
                number_as_text += (
                        order_separator +
                        segment_as_text +
                        cardinal_singular_suffix +
                        order_suffix)

        return number_as_text

    def calculate_order_suffix(self, is_plural, order):
        """
         drei
         ...hundert
         ...tausend
         eine Million
         zwei Million   + e + n
         drei Milliarde     + n
        """
        order_plural_suffix = ""
        if is_plural and order > 1:
            if order % 2 == 0:
                order_plural_suffix += "e"
            order_plural_suffix += "n"
        return self.ORDERS_SUFFIX[order] + order_plural_suffix

    def calculate_cardinal_singular_suffix(self, order, segment_as_text):
        """
        ein_s_
        einhundertein_s_
        einhundertein__tausend !!!
        ein_e_ Million
        einhundertein_s_ Millionen
        """
        is_plural = segment_as_text != "ein"
        cardinal_singular_suffix = ""
        if segment_as_text[-3:] == "ein":
            if order == 1:
                pass
            elif order == 0 or is_plural:
                cardinal_singular_suffix = "s"
            else:
                cardinal_singular_suffix = "e"
        return is_plural, cardinal_singular_suffix

    def calculate_order_separator(self, order):
        """
        if we are not the highest/lowest order lead with a seperator
        """
        return self.SEPERATOR_OF_ORDERS \
            if self.number_segmenter.get_order_of_number() > order > 0 else ""
