import unittest

from approvaltests.approvals import verify

from number_writer.german.germannumberwriter import GermanNumberWriter
from number_writer.numbersegmenter import NumberSegmenter


class GermanNumbersTest(unittest.TestCase):
    # Testplan:
    # Sollen Zahlen in Wörtern angegeben werden, schreibt man sie zusammen,
    # sofern sie unter einer Million liegen.
    #
    # Die Potenzen von tausend ab der Million (Million, Milliarde, Billion,
    # Billiarde usw.) sind Substantive und werden in entsprechend großen,
    # in Wortform dargestellten Zahlen als einzelnes, groß geschriebenes Wort
    # geführt.
    #
    # Beispiel: 1234678901
    #           = eine Milliarde zweihundertvierunddreißig Millionen
    #             sechshundertachtundsiebzigtausendneunhunderteins
    #
    # 0 --> null
    # 1 --> eins
    # test single digit
    # 10 --> zehn
    # 99 --> neunundneunzig
    # test two digits
    # 100 --> einhundert
    # 300 --> dreihundert
    # 310 --> dreihundertzehn
    # test three digits
    # 1965 = eintausendneunhundertfünfundsechzig
    # 312723 = dreihundertzwölftausendsiebenhundertdreiundzwanzig
    # 2120419 = zwei Millionen einhundertzwanzigtausendvierhundertneunzehn

    def test_single_digits(self):
        result = [GermanNumberWriter(number).to_text() for number in range(0, 10)]
        verify(result, encoding="UTF-8")
 
    def test_every_two_digit_number(self):
        result = "\n".join(
            [GermanNumberWriter(number).to_text() for number in range(10, 100)])
        verify(result, encoding="UTF-8")

    def test_every_three_digit_number(self):
        result = "\n".join(
            [GermanNumberWriter(number).to_text() for number in range(100, 1000)])
        verify(result, encoding="UTF-8")
        
    def test_one_thousand_five_hundred_and_one(self):
        result = GermanNumberWriter(1501).to_text()
        verify(result, encoding="UTF-8")

    def test_dissecting_to_order(self):
        splitter = NumberSegmenter(1501)
        result = list(splitter.segments())
        verify(result, encoding="UTF-8")

    def test_twelve_thousand_six_hundred_and_nine(self):
        result = GermanNumberWriter(12609).to_text()
        verify(result, encoding="UTF-8")
    
    def test_five_hundred_and_twelve_thousand_six_hundred_and_seven(self):
        result = GermanNumberWriter(512607).to_text()
        verify(result, encoding="UTF-8")
    
    def test_forty_three_million(self):
        result = GermanNumberWriter(43112603).to_text()
        verify(result, encoding="UTF-8")
        
    def test_one_million(self):
        result = GermanNumberWriter(1000000).to_text()
        verify(result, encoding="UTF-8")

    def test_one_hundred_one_million(self):
        result = GermanNumberWriter(101000000).to_text()
        verify(result, encoding="UTF-8")


    def test_one_hundred_and_one_thousand(self):
        result = GermanNumberWriter(101000).to_text()
        verify(result, encoding="UTF-8")

    def test_sample_in_millions(self):
        result = "\n".join(
            [GermanNumberWriter(number).to_text() for number in
             range(1000000, 100000000, 215431)])
        verify(result, encoding="UTF-8")
       
    def test_a_really_long_one(self):
        result = GermanNumberWriter(1050907000407750600030640022401).to_text()
        verify(result, encoding="UTF-8")


if __name__ == "__main__":
    unittest.main()
