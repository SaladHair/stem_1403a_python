"""
Inheritance type :  multiple inheritance
Description:
PercussionInstrument (sound_range, precision, sound_type, hit())
KeyboardInstrument (sound_range, precision, sound_type, press())
Piano (type, hit_strings())
A piano is a percussion instrument and a keyboard instrument.

"""


class PercussionInstrument:
    def __init__(self, sound_range, precision, sound_type):
        self.sound_range = sound_range
        self.precision = precision
        self.sound_type = sound_type

    def hit(self):
        print("the percussion instrument was hit")


class KeyboardInstrument():
    def __init__(self, sound_range, precision, sound_type):
        self.sound_range = sound_range
        self.precision = precision
        self.sound_type = sound_type

    def press(self):
        print("the keys of the keyboard instrument are pressed")


class Piano(PercussionInstrument, KeyboardInstrument):
    def __init__(self, sound_range, precision, sound_type, type):
        super().__init__(sound_range, precision, sound_type)
        self.type = type

    def hit_strings(self):
        print("the piano's hammers hit the strings and produced sounds")


# main program
percussion_instrument = PercussionInstrument("D1-F4", "very precise", "percussion")
print(percussion_instrument.sound_range, percussion_instrument.precision, percussion_instrument.sound_type)
percussion_instrument.hit()

keyboard_instrument = KeyboardInstrument("D1-F4", "mildly precise", "pipes")
print(keyboard_instrument.sound_range, keyboard_instrument.precision, keyboard_instrument.sound_type)
keyboard_instrument.press()

piano = Piano("A0-C8", "88 notes", "strings", "specialized")
print(piano.sound_range, piano.precision, piano.sound_type, piano.type)
piano.hit()
piano.press()
piano.hit_strings()
