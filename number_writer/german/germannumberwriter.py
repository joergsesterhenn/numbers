from number_writer.german.germansegmentwriter import GermanSegmentWriter
from number_writer.numberwriter import NumberWriter


class GermanNumberWriter(NumberWriter):
    # names for multiples of thousand - we are counting with the long scale
    ORDERS_SUFFIX = ['', 'tausend', ' Million', ' Milliarde', ' Billion',
                     ' Billiarde', ' Trillion', ' Trilliarde',
                     ' Quadrillion', ' Quadrilliarde', ' Quintillion']

    SEPERATOR_OF_ORDERS = ' '

    def to_text(self):
        """
        :return: the number as text
        """

        # edge cases handled first
        if self.number == 0:
            return 'null'
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
                # if we are not the highest order lead with a seperator
                if self.number_segmenter.get_order_of_number() > order > 0:
                    number_as_text += self.SEPERATOR_OF_ORDERS

                # append the segment text to the number
                number_as_text += segment_as_text

                is_plural = True
                if segment_as_text == "ein":
                    if order == 0:
                        number_as_text += "s"
                    elif order > 1:
                        number_as_text += "e"
                    is_plural = False

                # attach the orders suffix
                number_as_text += self.ORDERS_SUFFIX[order]
                if is_plural and order > 1:
                    if order % 2 == 0:
                        number_as_text += "e"
                    number_as_text += "n"

        return number_as_text
