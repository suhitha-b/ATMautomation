from nltk.chat.util import Chat,reflections
pairs=[
    [r'hi',['hiii']],
    [r'hii|hello|hey',['Hlo how can i help you']],
    [r'how are you',['i am doing well hoping u good']],
    [r'what is your name',['my name is chatbot']],
    [r'who invented you',['i was invented by suhitha']],
]
chat=Chat(pairs,reflections)
chat.converse()
def quit1():
    print("hi i am chat bot ask me something")
if __name__=="__main__":
    quit1()