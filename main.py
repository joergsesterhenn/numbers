# fooling around with our classes for a chance at exploratory testing

from io import BytesIO
from random import randrange

from number_writer.german.germannumberwriter import GermanNumberWriter
from number_writer.english.englishnumberwriter import EnglishNumberWriter
from gtts import gTTS
from pygame import mixer, time

from number_writer.numberwriter import NumberWriter


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
    number_as_text,number_as_audio = convert(number, lang)
    print(number_as_text)
    say(number_as_audio)


def convert(number, lang):
    number_writer: NumberWriter
    if lang in ("g", "G"):
        language = 'de'
        number_writer = GermanNumberWriter(int(number))
    else:
        language = 'en'
        number_writer = EnglishNumberWriter(int(number))
    number_as_text = number_writer.to_text()
    number_as_audio = gTTS(text=number, lang=language)
    return number_as_text, number_as_audio


def say(audio):
    mixer.init()
    mixer.music.load(to_file_like_object(audio))
    mixer.music.play()
    while mixer.music.get_busy():
        time.Clock().tick(10)


def to_file_like_object(audio):
    fp = BytesIO()
    audio.write_to_fp(fp)
    fp.seek(0)
    return fp


if __name__ == "__main__":
    main()
