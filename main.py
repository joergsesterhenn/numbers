# fooling around with our classes for a chance at exploratory testing

from io import BytesIO
from random import randrange

from number_writer.german.germannumberwriter import GermanNumberWriter
from number_writer.english.englishnumberwriter import EnglishNumberWriter
from gtts import gTTS
from pygame import mixer, time


def main():
    user_input = ''
    lang = ''
    while user_input not in ('q', 'Q'):
        while user_input not in ('q', 'Q', 'g', 'G', 'e', 'E'):
            user_input = (
                input("Enter language [e: english, g: german (q to quit)]: "))
            lang = user_input
        while user_input not in ('q', 'Q', 'l', 'L'):
            user_input = (
                input("Enter number (q to quit, l to choose language): "))
            number = user_input
            if number.isdecimal():
                print_and_say(number, lang)


def print_and_say(number, lang):
    """
    prints the number as text and then reads the integer number with
    the Google text to speech framework, so that we can compare results
    """
    if lang in ("g", "G"):
        language = 'de'
        text = GermanNumberWriter(int(number)).to_text()
    else:
        language = 'en'
        text = EnglishNumberWriter(int(number)).to_text()
    print(text)

    # fun with accents
    accents = ['com.au', 'co.uk', 'ca', 'co.in', 'ie', 'co.za', 'us']
    number_as_audio = (
        gTTS(text=number,
             lang=language,
             tld=accents[randrange(len(accents))],
             slow=False))
    fp = BytesIO()
    number_as_audio.write_to_fp(fp)
    fp.seek(0)
    mixer.init()
    mixer.music.load(fp)
    mixer.music.play()
    while mixer.music.get_busy():
        time.Clock().tick(10)


if __name__ == "__main__":
    main()
