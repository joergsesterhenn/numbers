from number_writer.numbersegmenter import NumberSegmenter
from number_writer.english_number_writer.segmentwriter import SegmentWriter


class NumberWriter:

    # names for multiples of thousand - we are counting with the short scale
    ORDERS_SUFFIX = ['', ' thousand', ' million', ' billion', ' trillion',
                     ' quadrillion', ' quintillion', ' sextillion',
                     ' septillion', ' octillion', ' nonillion']

    SEPERATOR_OF_ORDERS = ', '

    number: int
    number_segmenter: NumberSegmenter

    def __init__(self, number: int):
        self.number = number
        self.number_segmenter = NumberSegmenter(number)

    def to_text(self):
        """
        :return: the number as text
        """

        # edge case handled first
        if self.number == 0:
            return 'zero'

        number_as_text = ''

        # build number_as_text by traversing and appending
        # segments of three digits from highest to lowest orders
        for order, segment in self.number_segmenter.segments():

            # get a segment as text
            segment_as_text = SegmentWriter(segment).to_text()

            # if this segment is not empty
            if segment_as_text:
                # if we are not the highest order lead with a comma
                if order != self.number_segmenter.get_order_of_number():
                    number_as_text += self.SEPERATOR_OF_ORDERS

                # append the segment text to the number
                number_as_text += segment_as_text

                # attach the orders suffix
                number_as_text += self.ORDERS_SUFFIX[order]

        return number_as_text
