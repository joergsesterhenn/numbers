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
            if user_input in ('q', 'Q'):
                return
        while user_input not in ('q', 'Q'):
            user_input = (
                input("Enter number (q to quit, l to choose language): "))
            number = user_input
            if number.isdecimal():
                if lang in ('g', 'G'):
                    print_and_say(
                        GermanNumberWriter(int(number)).to_text(),
                        'de')
                else:
                    print_and_say(
                        EnglishNumberWriter(int(number)).to_text())
            if user_input in ('l', 'L'):
                break
            if user_input in ('q', 'Q'):
                return


def print_and_say(text, language='en'):
    print(text)
    # fun with accents
    accents = ['com.au', 'co.uk', 'ca', 'co.in', 'ie', 'co.za', 'us']
    number_as_audio = (
        gTTS(text=text,
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
