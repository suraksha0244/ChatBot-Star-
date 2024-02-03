import PySimpleGUI as sg
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Importing and Reading the corpus(Data)
with open('chatbot.txt', 'r', errors='ignore') as f:
    raw_doc = f.read().lower()

nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

# Text Preprocessing
lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Defining the greeting function
GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREET_RESPONSES = ["Hi", "Hey", "nods", "Hi there", "Hello", "I am glad! You are talking to me"]


def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)


# Response generation
def response(user_response):
    robo1_response = ''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')

    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo1_response = robo1_response + "I am sorry! I don't understand you"
        return robo1_response
    else:
        robo1_response = robo1_response + sent_tokens[idx]
        return robo1_response


# PySimpleGUI layout with a placeholder
layout = [
    [sg.Text("ChatBot : My name is Star*. Let's have a conversation! Ask me anything about Machine Learning, I'm here to help you :)", font=('Helvetica', 14))],
    [sg.Multiline(size=(100, 20), key='-OUTPUT-', disabled=True, background_color='lightgrey', font=('Helvetica', 12))],
    [sg.InputText(key='Input1', size=(60, 1), tooltip="Type your question here", font=('Helvetica', 12), justification='left', enable_events=True)],
    [sg.Button('Send', button_color=('white', 'green'), size=(10, 1), border_width=2), sg.Button('Exit', button_color=('white', 'red'), size=(10, 1), border_width=2)],
]

window = sg.Window('Title', layout, finalize=True)
window['Input1'].bind("<Return>", "_Enter")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Send' or (event == 'Input1' + "_Enter" and values['Input1']):
        user_response = values['Input1'].strip().lower()

        # Display user's input in the output area with blue color
        window['-OUTPUT-'].print(f"User : {user_response}", text_color='blue')

        if user_response != 'bye':
            if user_response == 'thanks' or user_response == 'thank you':
                # Display bot response in the output area with green color
                window['-OUTPUT-'].print("Star* : You're Welcome..", text_color='green')
                break
            else:
                if greet(user_response) is not None:
                    # Display bot response in the output area with green color
                    window['-OUTPUT-'].print(f"Star* : {greet(user_response)}", text_color='green')
                else:
                    sent_tokens.append(user_response)
                    word_tokens.extend(nltk.word_tokenize(user_response))
                    final_words = list(set(word_tokens))
                    response_text = response(user_response)
                    # Display bot response in the output area with green color
                    window['-OUTPUT-'].print(f"Star* : {response_text}", text_color='green')
                    sent_tokens.remove(user_response)
        else:
            # Display bot response in the output area with red color
            window['-OUTPUT-'].print("Star* : Goodbye! Take care <3", text_color='red')
            break

        # Clear the input box
        window['Input1'].update('')
        # Grab focus to clear the text when clicked
        window['Input1'].Widget.focus_force()

# Close the window
window.close()