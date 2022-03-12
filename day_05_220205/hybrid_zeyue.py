"""
Inheritance type :  multiple inheritance
Description:
Instrument (sound_range, precision, play())
PercussionInstrument (sound_type, activation_mode, hit())
KeyboardInstrument (sound_type, activation_mode, press())
Piano (type, hit_strings())
A piano is a percussion instrument and a keyboard instrument and keyboard instruments and percussion instruments are
instruments.

"""


class Instrument:
    def __init__(self, sound_range, precision):
        self.sound_range = sound_range
        self.precision = precision

    def play(self):
        print("the instrument is playing")


class PercussionInstrument(Instrument):
    def __init__(self, sound_range, precision, sound_type, activation_mode):
        super().__init__(sound_range, precision)
        self.sound_type = sound_type
        self.activation_mode = activation_mode

    def hit(self):
        print("the percussion instrument was hit")


class KeyboardInstrument(Instrument):
    def __init__(self, sound_range, precision, sound_type, activation_mode):
        super().__init__(sound_range, precision)
        self.sound_type = sound_type
        self.activation_mode = activation_mode

    def press(self):
        print("the keys of the keyboard instrument are pressed")


class Piano(PercussionInstrument, KeyboardInstrument):
    def __init__(self, sound_range, precision, sound_type, activation_mode, piano_type):
        super().__init__(sound_range, precision, sound_type, activation_mode)
        self.piano_type = piano_type

    def hit_strings(self):
        print("the piano's hammers hit the strings and produced sounds")


# main program
instrument = Instrument("D1-F4", "very precise")
print(instrument.sound_range, instrument.precision)
instrument.play()

percussion_instrument = PercussionInstrument("D1-F4", "very precise", "percussion", "beater")
print(percussion_instrument.sound_range, percussion_instrument.precision, percussion_instrument.sound_type, percussion_instrument.activation_mode)
percussion_instrument.play()
percussion_instrument.hit()

keyboard_instrument = KeyboardInstrument("D1-F4", "mildly precise", "pipes", "keyboard")
print(keyboard_instrument.sound_range, keyboard_instrument.precision, keyboard_instrument.sound_type, keyboard_instrument.activation_mode)
keyboard_instrument.play()
keyboard_instrument.press()

piano = Piano("A0-C8", "88 notes", "strings", "keyboard", "specialized")
print(piano.sound_range, piano.precision, piano.sound_type, piano.activation_mode, piano.piano_type)
piano.play()
piano.hit()
piano.press()
piano.hit_strings()
