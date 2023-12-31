import openai
from textwrap import fill
from tkinter import *
from datetime import datetime
import textwrap
from conversation import IdentityBot  # Assuming your bot class is in IdentityBot.py

# Global variables
bot = None
model = "gpt-3.5-turbo"
user_responses = {}
subject_responses = {}
name = ""  

def send(event):
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
        wraplength=200, font=("Arial", 10), bg="#5BC236", bd=4, justify="left"))
        ChatLog.insert(END,'\n ', "left")
        ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = bot.conduct_conversation(msg)
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res, 
        wraplength=200, font=("San Francisco", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


def send_by_button():
    getmsg = EntryBox.get("1.0", 'end-1c').strip()
    msg = textwrap.fill(getmsg,30)
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
        wraplength=200, font=("Arial", 10), bg="#5BC236", bd=4, justify="left"))
        ChatLog.insert(END,'\n ', "left")
        ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = bot.conduct_conversation(msg)
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res, 
        wraplength=200, font=("San Francisco", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


# The following two functions are defined to add a placeholder text or to delete it.
def deletePlaceholder(event):
    Placeholder.place_forget()
    EntryBox.focus_set()

def addPlaceholder(event):
    if placeholderFlag == 1:
        Placeholder.place(x=6, y=421, height=70, width=265)

# Refresh GUI window every 0.1 seconds, mainly for the "SEND" button.
# If the entry box does not contain text --> 'Send' button is inactive, otherwise it's activated.

def update():
    global placeholderFlag
    if (EntryBox.get("1.0", 'end-1c').strip() == ''):
        SendButton['state'] = DISABLED
        placeholderFlag = 1
    elif EntryBox.get("1.0", 'end-1c').strip() != '':
        SendButton['state'] = ACTIVE
        placeholderFlag = 0
    base.after(100, update)

def start_ui(api_key, name, user_responses, subject_responses, model):
    global base
    global ChatLog
    global EntryBox
    global SendButton
    global Placeholder
    global scrollbar
    global placeholderFlag
    global current_time
    global bot
    # initialize the bot
    bot = IdentityBot(api_key, name, user_responses, subject_responses, model)

    base = Tk()
    base.title(name)
    base.geometry("400x500")
    base.resizable(width=FALSE, height=FALSE)

    #Add menus to the GUI
    main_menu = Menu(base)
    file_menu = Menu(base)
    file_menu.add_command(label="New..")
    file_menu.add_command(label="Save As..")
    file_menu.add_command(label="Exit")
    main_menu.add_cascade(label="File", menu=file_menu)
    #Add the rest of the menu options to the main menu
    main_menu.add_command(label="Edit")
    main_menu.add_command(label="Quit")
    base.config(menu=main_menu)

    now = datetime.now()
    current_time = now.strftime("%D - %H:%M \n")

    # Create Chat window
    ChatLog = Text(base, bd=0, height="8", width="50", font="Helvetica", wrap="word")
    ChatLog.config(state=NORMAL)
    ChatLog.tag_config("right", justify="right")
    ChatLog.tag_config("small", font=("Helvetica", 7))
    ChatLog.tag_config("colour", foreground="#333333")
    '''
    ChatLog.insert(END, current_time, ("small","colour"))
    ChatLog.insert(END,textwrap.fill(f"Hello {'*Name*'}. How can I assist you?",30))
    ChatLog.insert(END,'\n')
    '''
    ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
    ChatLog.config(state=DISABLED)

    # Bind scrollbar to Chat window
    scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="double_arrow")
    ChatLog['yscrollcommand'] = scrollbar.set

    # Create Button to send message
    SendButton = Button(base, font=("San Francisco", 12, 'bold'), text="Send", width="8", height=5,
                        bd=0, fg="#750216", activebackground="#AAAAAA", bg="#999999", command=send_by_button)

    # Create the box to enter message
    EntryBox = Text(base, bd=0, fg="#000000", bg="#fff5f5", highlightcolor="#750216",
                    width="29", height="5", font=("San Francisco",10), wrap="word")

    #Placeholder config and text:
    Placeholder = Text(base, bd=0, fg="#A0A0A0", bg="#fff5f5", highlightcolor="#750216",
                    width="29", height="5", font=("San Francisco",10), wrap="word")
    Placeholder.insert("1.0","Text Message")

    # Place all components on the screen
    scrollbar.place(x=376, y=6, height=406)
    ChatLog.place(x=6, y=6, height=410, width=370)
    EntryBox.place(x=6, y=421, height=70, width=276)
    SendButton.place(x=282, y=421, height=70)
    Placeholder.place(x=6, y=421, height=70, width=276)

    Placeholder.bind("<FocusIn>", deletePlaceholder)
    EntryBox.bind("<FocusOut>", addPlaceholder)

    base.bind('<Return>', send)
    update()
    base.mainloop()
