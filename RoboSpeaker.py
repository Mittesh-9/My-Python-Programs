import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Mittesh")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "p":
            os.system("PowerShell -Command \"Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye Bye Friend')\"")
            break
        command = f'PowerShell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)