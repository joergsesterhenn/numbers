from number_writer.english.englishsegmentwriter import EnglishSegmentWriter
from number_writer.numberwriter import NumberWriter


class EnglishNumberWriter(NumberWriter):
    # names for multiples of thousand - we are counting with the short scale
    ORDERS_SUFFIX = ['', ' thousand', ' million', ' billion', ' trillion',
                     ' quadrillion', ' quintillion', ' sextillion',
                     ' septillion', ' octillion', ' nonillion']

    SEPERATOR_OF_ORDERS = ', '

    def to_text(self):
        """
        :return: the number as text
        """

        # edge case handled first
        if self.number == 0:
            return 'zero'

        number_as_text = ''

        for order, segment in self.number_segmenter.segments():
            segment_as_text = EnglishSegmentWriter(segment).to_text()
            if segment_as_text:
                order_separator = self.calculate_order_separator(order)
                order_suffix = self.calculate_order_suffix(order)
                number_as_text += (order_separator +
                                   segment_as_text +
                                   order_suffix)

        return number_as_text

    def calculate_order_suffix(self, order):
        return self.ORDERS_SUFFIX[order]

    def calculate_order_separator(self, order):
        return self.SEPERATOR_OF_ORDERS \
            if order != self.number_segmenter.get_order_of_number() else ""
