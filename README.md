# 🤖 ChatBot : Star*

A simple, rule-based chatbot built using Python, employing a TF-IDF approach for response generation and a PySimpleGUI-based user interface for seamless interaction.

---

## 📚 Libraries Used

- **NumPy (`numpy`)** — Numerical computations
- **NLTK (`nltk`)** — Natural language processing and lemmatization
- **String (`string`)** — String manipulation
- **Random (`random`)** — Generating random values
- **PySimpleGUI (`PySimpleGUI`)** — Simple GUI framework for Python
- **scikit-learn (`sklearn`)**
  - `TfidfVectorizer` — Converts text to numerical vectors
  - `cosine_similarity` — Calculates similarity between text inputs

---

## 📖 How It Works

### 1️⃣ Reading the Corpus
- Loads text data from `chatbot.txt`  
- Text corpus serves as the knowledge base for generating responses  

### 2️⃣ Text Preprocessing
- Converts all text to lowercase for consistency  
- Performs tokenization:
  - `sent_tokenize()` — Splits text into sentences
  - `word_tokenize()` — Splits sentences into words  

### 3️⃣ Text Normalization
- Uses **NLTK Lemmatizer** to reduce words to their base form

### 4️⃣ Greeting Detection
- Detects if user input contains a greeting (like *hello*, *hi*, *hey*)  
- Replies with a random greeting from a predefined list

### 5️⃣ Response Generation
- Converts both user input and existing corpus into **TF-IDF vectors**
- Computes **cosine similarity** between the user input and corpus sentences  
- Responds with the most similar sentence  

### 6️⃣ GUI Layout
- Designed using **PySimpleGUI**
- Components:
  - Multiline output area for conversation history
  - Text input box for user messages
  - “Send” and “Exit” buttons  

### 7️⃣ Event Loop
- Waits for user input  
- Responds based on input (greeting, response generation, or goodbye)
- Closes on “bye” or Exit button  

---

## 📊 Algorithm Summary

| Concept             | Description                                                                 |
|:-------------------|:----------------------------------------------------------------------------|
| **Approach**        | Rule-based chatbot using **TF-IDF** and **cosine similarity**                |
| **Response Logic**  | Compares user input to a text corpus and finds the closest match             |
| **NLU Level**       | Basic — understands greetings and responds contextually to user inputs       |
| **User Interface**  | Created with **PySimpleGUI** for an interactive conversational experience    |

---


## 📝 How to Run

1. Install required libraries:
   ```bash
   pip install numpy nltk PySimpleGUI scikit-learn
