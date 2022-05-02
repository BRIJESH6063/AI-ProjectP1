import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

command = ''
x = 1

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    
    try:
        with sr.Microphone() as source:
            print("listening......")
            command = ''
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
                
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('The current time is ' + time)
        return 0
    elif 'how are you' in command :
        print('I am fine Thank you!')
        talk('I am fine Thank you!')
        return 0
    elif 'what are you feeling' in command:
        print('I am feeling good! how may i assist you.')
        talk('I am feeling good! how may i assist you.')
        return 0
    elif 'date today' in command :
        date = datetime.datetime.now().strftime('%D')
        print('Today is'+ date)
        talk('Today is'+ date)
        return 0
    elif 'current year' in command :
        year = datetime.datetime.now().strftime('%Y')
        print('Current year is'+ year)
        talk('Current year is' + year)
        return 0
    elif 'current month' in command :
        month = datetime.datetime.now().strftime('%m')
        month = datetime.datetime.strptime(month,'%m')
        month = month.strftime('%B')
        print('Current Month is '+ month)
        talk('Current Month is '+ month)
        return 0
    elif 'stop' in command :
        talk('Ok! I hope you liked my assistance. Thank you!')
        return 1

while True:
    if (run_alexa()):
        break


    




