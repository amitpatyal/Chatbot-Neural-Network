from tkinter import *
from helper_function import GetChatbotResponse

def GetResponse():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12))

        response = GetChatbotResponse(msg)
        ChatLog.insert(END, "Bot: " + response + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


chatbot_window = Tk()
chatbot_window.title("Python Chatbot")
chatbot_window.geometry("400x500")
chatbot_window.resizable(width=FALSE, height=FALSE)
ChatLog = Text(chatbot_window, bd=0, bg="white", height="8", width="50", font="Arial", )
ChatLog.config(state=DISABLED)
scrollbar = Scrollbar(chatbot_window, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
SendButton = Button(chatbot_window, font=("Verdana", 12, 'bold'), text="Send", width="7", height="5",
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                    command=GetResponse)
EntryBox = Text(chatbot_window, bd=0, bg="white", width="29", height="5", font="Arial")
# EntryBox.bind("<Return>", GetResponse)
scrollbar.place(x=376, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)
chatbot_window.mainloop()