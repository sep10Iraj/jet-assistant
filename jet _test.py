
import time
import pyttsx3
import webbrowser
import os
import subprocess
from colorama import Fore

def color():
    print("""1-Hacker
2-Sea
3-pinky""")
    color=input("enter mode:")
    if color == "1":
        my_color= Fore.GREEN
    elif color == "2":
        my_color= Fore.BLUE
    elif color == "3":
        my_color= Fore.RED
    return my_color
color_1=color()  
def voice(user_input,print_yes_or_no=True):
    if print_yes_or_no == True:
        print(color_1,user_input)
    se=pyttsx3.init()
    se.setProperty('rate', 100)
    se.say(user_input)
    se.runAndWait()
print(color_1,"""'welcom to jet'
this assistant can do some command:
open some app
command:open [edge-word]
open some web site
command:open [aparat-fast dict]
some os command
command: endwork
and daily conversation
for example hi or what is your favorite food and ...
if you want to see this page enter 'help'
 """)

voice("hi what is your name?",False)
name_1=input(f"{color_1}What is your name?")


dir=os.getcwd()
while True :
    os.system("cls")
    text=input('==>>').lower()
    
    if text == "hello":
        anser=f'hi {name_1},how can I help?'
    elif text == "who is sepehr" :
        anser='sepehr is my developer'
    elif text == "help":
        print("""'  welcom to jet'
    this assistant can do some command:
    open some app
    command:open [edge-word]
    open some web site
    command:open [aparat-fast dict]
    some os command
    command: endwork
    and daily conversation
    for example hi or what is your favorite food and ...
    if you want to see this page enter 'helo'""")       
    elif text == "what is your name":
        anser='my name is jet'
    elif text == "tell me a joke" :
        anser= '''I cant tell joke but I can say:
        ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha'''       
    elif text == "who is your best friend" :
        anser=f'{name_1}is my best frind' 
    elif text == "what time is it":
        anser= time.strftime('%H:%M')              
    elif text == "where are you":
        print(dir)
        anser=' '    
    elif text == 'who am i':
        anser=f'you are {name_1}'   
    elif text == "open edge":
        os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        anser="opening"
    elif text == "open word":
        os.startfile("C:\\Users\\digi max\\OneDrive\\Desktop\\Word 2016")
        anser="opening"
    elif text == 'what is your favorite food' :
        anser='I like pizza but I cant eat 😥'
    elif text == "open sound"  :
        import sound
    elif text == 'open note':
        import sepehr_note
        anser=' '
    elif text == 'open calculator':
        import c
        anser=' ' 
    elif text == "aparat":
        webbrowser.open("https://www.aparat.com")
        anser=" opening"
    elif text == "fast dict":
        webbrowser.open("https://www.bing.com/search?q=%DA%AF%D9%88%DA%AF%D9%84+%D8%AA%D8%B1%D8%AC%D9%85%D9%87&form=ANSPH1&refig=f8622eb7aa1542758a389eaf43c5ecaa&pc=U531&sp=1&qs=HS&pq=%DA%AF%D9%88%DA%AF%D9%84&sk=PRES1&sc=8-4&cvid=f8622eb7aa1542758a389eaf43c5ecaa")
        anser=" opening"
    elif text == "end work":
        os.system("shutdown.exe /h")
    elif text == "bye":
        voice(f"bye {name_1}")
        break    
    else:
        anser='''I dont understand.
I dont have any answer for your question'''
    voice(anser)