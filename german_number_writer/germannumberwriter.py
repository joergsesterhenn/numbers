from german_number_writer.germannumbersegmenter import GermanNumberSegmenter
from german_number_writer.germansegmentwriter import GermanSegmentWriter

class GermanNumberWriter:

    # names for multiples of thousand - we are counting with the long scale
    ORDERS_SUFFIX = ['', 'tausend', ' Million', ' Milliarde', ' Billion',
                     ' Billiarde', ' Trillion', ' Trilliarde',
                     ' Quadrillion', ' Quadrilliarde', ' Quintillion']

    SEPERATOR_OF_ORDERS = ' '

    number: int
    number_segmenter: GermanNumberSegmenter

    def __init__(self, number: int):
        self.number = number
        self.number_segmenter = GermanNumberSegmenter(number)

    def to_text(self):
        """
        :return: the number as text
        """

        # edge case handled first
        if self.number == 0:
            return 'null'

        # edge case handled first
        if self.number == 1:
            return 'eins'

        number_as_text = ''

        # build number_as_text by traversing and appending
        # segments of three digits from highest to lowest orders
        for order, segment in self.number_segmenter.segments():

            # get a segment as text
            segment_as_text = GermanSegmentWriter(segment).to_text()

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
