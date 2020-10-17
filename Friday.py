import speech_recognition as sr
import client
from time import ctime
import playsound
import os
import random
from gtts import gTTS
import time
import wikipedia
DISCONNECT_MESSAGE = '!DISCONNECT'
r = sr.Recognizer()


class Person:
    name = ''
    age = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for t in terms:
        if t in voice_data:
            return True


def friends_jokes():
    friends = str(random.randint(1, 13))
    playsound.playsound(f"./friends/{friends}.mp3")


def friday_speak(audio_str):
    tts = gTTS(text=audio_str, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def record_audio(ask=False):
    with sr.Microphone() as source:

        if ask:
            friday_speak(ask)

        audio = r.listen(source)
        voice_data = ''

        if trigger:
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                friday_speak('Sorry, I did not get that')
            except sr.RequestError:
                friday_speak('Sorry, my speech service is down')
        else:
            try:
                voice_data = r.recognize_google(audio)
            except:
                pass

        return voice_data


def respond(voice_data):

    global trigger
    global sock_client
    # HELLO - GREETINGS
    if there_exists(['hey Friday', 'hi Friday', 'Friday']) and not trigger:
        greetings = [f"hey, how can I help you {person.name}?", f"hey, what's up? {person.name}",
                     f"I'm listening", f"how can I help you {person.name}? ", f"hi there {person.name}", "yes?"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        friday_speak(greet)
        trigger = True

    # FRIDAY NAME
    if there_exists(["what is your name", "what's your name", "tell me your name"]) and trigger:
        if person.name:
            name_resp = ["my name is Friday", "I'm Friday, that's my whole name",
                         "my name is Friday, like the day"]
            friday_speak(name_resp[random.randint(0, len(name_resp) - 1)])
            trigger = False
        else:
            friday_speak("my name is Friday. what's your name?")

    if there_exists(["my name is"]) and trigger:
        person_name = voice_data.split("is")[-1].strip()
        friday_speak(f"okay, I will remember that {person_name}")
        person.setName(person_name)
        trigger = False

    # MY NAME
    if there_exists(["tell me my name", "what's my name", "what is my name"]) and trigger:
        if person.name:
            existing_resp = [
                f"your name is {person.name}", f"your name is {person.name}, at least that's what you tell me"]
            response = existing_resp[random.randint(0, len(existing_resp) - 1)]
            friday_speak(response)
            trigger = False
        else:
            not_exisisting_resp = ["sorry, you did not tell me your name. Would you?",
                                   "I don't know your name. What is it?", "sorry, I didn't know it. Would you tell me please?"]
            response = not_exisisting_resp[random.randint(
                0, len(not_exisisting_resp) - 1)]
            friday_speak(response)

    # WHY IS FRIDAY
    if there_exists(["why is your name friday", "by whom were you named for", "by whom were you named friday"]) and trigger:
        friday_names = ["my name stands for Female Replacement Intelligent Digital Assistant Youth and I'm your AI assistant",
                        "I was named after Tony Stark's AI assistant"]
        response = friday_names[random.randint(0, len(friday_names) - 1)]
        friday_speak(response)
        trigger = False

    # IRON MAN - TONY STARK
    if there_exists(["who's Tony Stark", "who is Tony Stark"]) and trigger:
        tony = ["you really don't know who Tony Stark is? He is fucking iron man!",
                "I can't belive it. I recommend you watch the avengers movies before talking to me again."]
        response = tony[random.randint(0, len(tony) - 1)]
        friday_speak(response)
        trigger = False

    # TIME
    if there_exists(["what's the time", "tell me the time", "what time is it"]) and trigger:
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        friday_speak(time)
        trigger = False

    # EXIT
    if there_exists(["exit", "quit", "goodbye"]) and trigger:
        ex = ["going offline", f"bye {person.name}", "adios", "seem like you aren't enjoing my company. Goodbye",
              "see you", "have a nice day, goodbye", "bye bye", "system going down"]
        response = ex[random.randint(0, len(ex) - 1)]
        friday_speak(response)
        trigger = False
        sock_client.send(DISCONNECT_MESSAGE)
        exit()

    # LIGHTS ON
    if there_exists(["turn the lights on", "lights on", "i can't see", "i can not see", "i can't see anything", "world is black for me", "my room is in complete darkness"]) and trigger:
        # turn the lights on

        if sock_client.send('HIGH'):
            lights_on = ["lighting your world up", "turning the lights on", "i hope you can see now",
                         "you should be able to see now", "can you see me now? hahaha i'm kidding i'm just a robot"]
            response = lights_on[random.randint(0, len(lights_on) - 1)]
        else:
            response = 'Sorry, I could not do it'
        friday_speak(response)
        trigger = False

    # LIGHTS OFF
    if there_exists(["turn the lights off", "lights off", "i don't wanna see anymore"]) and trigger:
        lights_off = ["turning your lighs off", "shutting your world down", "lights off",
                      "embrace the darkness", "certanly you can't see me now", "goodbye lights, you were a good friend"]
        response = lights_off[random.randint(0, len(lights_off) - 1)]
        friday_speak(response)
        trigger = False

    # JOKE
    if there_exists(["tell me a joke", "make me laugh", "i'm sad", "i'm in a bad mood"]) and trigger:
        friday_speak("here's a frinds joke for you")
        friends_jokes()
        trigger = False

    # WIKIPEDIA
    if there_exists(["wikipedia", "Wikipedia"]) and trigger:
        wiki = voice_data.lower().split("wikipedia")[1]
        try:
            page = wikipedia.page(wiki)
            friday_speak(f"this is what I found on wikipedia for{wiki}")
            friday_speak(page.summary.split('\n')[0])
        except:
            friday_speak(f"sorry, i couldn't find anything for{wiki}")

        trigger = False


time.sleep(1)
person = Person()
sock_client = client.SocketClient()
trigger = False
print("Running Assistant")

while True:
    voice_data = record_audio()
    respond(voice_data)
