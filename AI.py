import speech_recognition
import pyttsx3
from datetime import date

engine = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
while True:
    with speech_recognition.Microphone() as mic:
        print("I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you=""
    print("You:" + you)

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Thinh"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "how are you" in you:
        robot_brain = "Im fine, thank you"
    elif "bye" in you:
        robot_brain = "Goodbye"
        print(robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
        break
    else:
        robot_brain = "I do not understand"

    print(robot_brain)
    engine.say(robot_brain)
    engine.runAndWait()