import numpy as np
import os
import sys
from pydub import AudioSegment


def float_checker(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

# Source - https://stackoverflow.com/a/51434954
def speed_changer(sound, speed=1.0):

    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })

    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

# Source - https://stackoverflow.com/a/44730611
def pitch_changer(audio,octaves):
  new_sample_rate = int(audio.frame_rate * (2.0 ** octaves))
  return audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})    

def export(audio):
    new_filename = 'new' + raw_name + '.' + file_type

    try:
        audio.export(new_filename, format=file_type)
    except Exception as e:
        sys.exit('Audio failed to export.')

    sys.exit(f'The new audio file was created at {new_filename}. Enjoy!')


print('Hello! This is an audio editor program which will create a copy of a audio file (x.wav, .mp3, x.ogg, x.flv) with any effect that you select below. Make sure to select the export option after you\'re done adding effects to your audio. The audio file must be in the same directory as this py file.')
file = input('File: ')

if not os.path.isfile(file): 
    sys.exit('Invalid file name. Make sure the file is in the same directory as this file and that you have added the file type tag (i.e. .mp3)')

raw_name = file[0:len(file)-4]
file_type = file[len(file)-3:len(file)]

try:
    audio = AudioSegment.from_file(file, file_type)
except:
    sys.exit("Invalid file type. Make sure your file is a file type supported by ffmpeg.")


while True:
    effect = input('''
        Select an effect (Enter a number 1-6):
        1. Change Pitch
        2. Change Speed of Music
        3. Increase/Decrease Volume
        4. Reverse Audio
        5. Export
        6. Exit
    ''')

    if effect == '1':
        octave = '.'
        while not float_checker(octave):
            octave = float(input('Enter the amount of octaves you would like to go down or up(-0.5 to go down half an octave, 2.0 to go up 2 octaves): '))
        audio = pitch_changer(audio, octave) 
        print('Your desired pitch has been adjusted.')

    if effect == '2':
        speed = '.'
        while not float_checker(speed):
            speed = float(input('Enter desired speed (0.5 - half speed, 2 - double speed, etc): '))
        audio = speed_changer(audio, speed)
        print('Your desired speed has been implemeneted.')


    if effect == '3':
        decibels = ''
        while not float_checker(decibels):
            decibels = input('Enter the amount of decibels to increase or decrease by (1 to go up 1 decibel): ')
        audio += decibels
        print('The volume has been modified.')

    if effect == '4':
        audio = audio.reverse()
        print('The audio has been reversed.')

    if effect == '5':
        export(audio)

    if effect == '6':
        sys.exit("You have exited the program.")

