"""
Inheritance type :  multilevel inheritance
Description:
Instrument (sound_range, precision, play())
KeyboardInstrument (keys, sound_type, press())
Piano (type, hit_strings())
A piano is a type of keyboard instrument and a keyboard instrument is a type of instrument.

"""


class Instrument:
    def __init__(self, sound_range, precision):
        self.sound_range = sound_range
        self.precision = precision

    def play(self):
        print("the instrument is playing")


class KeyboardInstrument(Instrument):
    def __init__(self, sound_range, precision, keys, sound_type):
        super().__init__(sound_range, precision)
        self.keys = keys
        self.sound_type = sound_type

    def press(self):
        print("the keys of the keyboard instrument are pressed")


class Piano(KeyboardInstrument):
    def __init__(self, sound_range, precision, keys, sound_type, type):
        super().__init__(sound_range, precision, keys, sound_type)
        self.type = type

    def hit_strings(self):
        print("the piano's hammers hit the strings and produced sounds")


# main program
instrument = Instrument("D1-F4", "very precise")
print(instrument.sound_range, instrument.precision)
instrument.play()

keyboard_instrument = KeyboardInstrument("C2-C7", "56 notes", "levers", "pipes")
print(keyboard_instrument.sound_range, keyboard_instrument.precision, keyboard_instrument.keys, keyboard_instrument.sound_type)
keyboard_instrument.play()
keyboard_instrument.press()

piano = Piano("A0-C8", "88 notes", "levers", "strings", "specialized")
print(piano.sound_range, piano.precision, piano.keys, piano.sound_type, piano.type)
piano.play()
piano.press()
piano.hit_strings()

