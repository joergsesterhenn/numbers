import unittest

from approvaltests.approvals import verify

from number_writer.english.englishnumberwriter import EnglishNumberWriter
from number_writer.numbersegmenter import NumberSegmenter


class NumbersTest(unittest.TestCase):
    # testplan:
    #
    # x 1 --> one
    # x test single digit
    # x 10 --> ten
    # x 99 --> ninety nine
    # x test two digits
    # x 100 --> one hundred
    # x 300 --> three hundred
    # x 310 --> three hundred and ten
    # x test three digits
    # x 1501 --> one thousand, five hundred and one
    # x 12609 --> twelve thousand, six hundred and nine
    # x 512607 --> five hundred and twelve thousand, six hundred and seven
    # x 43112603 --> forty three million, one hundred and twelve thousand, six hundred and three

    def test_single_digits(self):
        result = [EnglishNumberWriter(number).to_text() for number in range(0, 10)]
        verify(result)
 
    def test_every_two_digit_number(self):
        result = "\n".join(
            [EnglishNumberWriter(number).to_text() for number in range(10, 100)])
        verify(result)

    def test_every_three_digit_number(self):
        result = "\n".join(
            [EnglishNumberWriter(number).to_text() for number in range(100, 1000)])
        verify(result)
        
    def test_one_thousand_five_hundred_and_one(self):
        result = EnglishNumberWriter(1501).to_text()
        verify(result)

    def test_dissecting_to_order(self):
        splitter = NumberSegmenter(1501)
        result = list(splitter.segments())
        verify(result)

    def test_twelve_thousand_six_hundred_and_nine(self):
        result = EnglishNumberWriter(12609).to_text()
        verify(result)
    
    def test_five_hundred_and_twelve_thousand_six_hundred_and_seven(self):
        result = EnglishNumberWriter(512607).to_text()
        verify(result)
    
    def test_forty_three_million(self):
        result = EnglishNumberWriter(43112603).to_text()
        verify(result)
        
    def test_one_million(self):
        result = EnglishNumberWriter(1000000).to_text()
        verify(result)
        
    def test_sample_in_millions(self):
        result = "\n".join(
            [EnglishNumberWriter(number).to_text() for number in
             range(1000000, 100000000, 215431)])
        verify(result)
       
    def test_a_really_long_one(self):
        result = EnglishNumberWriter(1050907000407750600030640022401).to_text()
        verify(result)


if __name__ == "__main__":
    unittest.main()
