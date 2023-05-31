import requests
import json
import pyttsx3

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=72896d400d474c47a27165825230704&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
temp_c = wdic["current"]["temp_c"]

# Define the text to be spoken
text = f"The current weather in {city} is {temp_c} degrees celcius"

# Define the text to be spoken
print(f"The current weather in {city} is {temp_c} degrees celcius")

# Create an instance of the TTS engine
engine = pyttsx3.init()

# Use the TTS engine to speak the text
engine.say(text)
engine.runAndWait()