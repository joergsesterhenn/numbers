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
                is_plural, singularity_suffix = (
                    self.calculate_singularity_suffix(order, segment_as_text))
                order_suffix = self.calculate_order_suffix(is_plural, order)
                number_as_text += (
                        order_separator +
                        segment_as_text +
                        singularity_suffix +
                        order_suffix)

        return number_as_text

    def calculate_order_suffix(self, is_plural, order):
        """
        calculate the orders suffix
        """
        order_suffix = self.ORDERS_SUFFIX[order]
        if is_plural and order > 1:
            if order % 2 == 0:
                order_suffix += "e"
            order_suffix += "n"
        return order_suffix

    def calculate_singularity_suffix(self, order, segment_as_text):
        """
        calculate singularity depending on order
        """
        is_plural = True
        singularity_suffix = ""
        if segment_as_text[-3:] == "ein":
            if order == 0:
                singularity_suffix = "s"
            elif order > 1:
                singularity_suffix = "e"
            is_plural = False
        return is_plural, singularity_suffix

    def calculate_order_separator(self, order):
        """
        if we are not the highest/lowest order lead with a seperator
        """
        order_separator = ""
        if self.number_segmenter.get_order_of_number() > order > 0:
            order_separator = self.SEPERATOR_OF_ORDERS
        return order_separator
