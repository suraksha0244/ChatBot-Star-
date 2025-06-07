
# 🤖 ChatBot: Star*

A simple, rule-based chatbot built using Python, employing a **TF-IDF (Term Frequency–Inverse Document Frequency)** approach for response generation and a **PySimpleGUI**-based user interface for seamless interaction.

---

## 📜 Table of Contents
- [Features](#-features)
- [Libraries Used](#-libraries-used)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Run the Project](#-run-the-project)

---

## 🎯 Features
- Greets the user with random greetings.
- Responds contextually based on text similarity with a predefined corpus.
- Basic natural language understanding using **TF-IDF vectorization**.
- Interactive GUI created with **PySimpleGUI**.
- Clean, color-coded message layout.
- Custom handling for 'bye', 'thanks', and greetings.

---

## 📚 Libraries Used
- **NumPy** — Numerical computations.
- **NLTK** — Tokenization, lemmatization, and text processing.
- **String** — String manipulation utilities.
- **Random** — Random selection for responses.
- **Scikit-learn**  
  - `TfidfVectorizer` — Converts text to numerical vectors.
  - `cosine_similarity` — Measures similarity between text vectors.
- **PySimpleGUI** — Lightweight and intuitive GUI framework for Python.

---

## 🔍 How It Works

1. **Load Corpus**
   - Reads text data from `chatbot.txt`, which acts as the knowledge base.

2. **Text Preprocessing**
   - Lowercases text.
   - Tokenizes into sentences and words.
   - Removes punctuation.
   - Lemmatizes words to their root form.

3. **Greeting Detection**
   - Recognizes if user input contains a greeting.
   - Responds with a random greeting from a predefined list.

4. **Response Generation**
   - Converts user input and corpus sentences into TF-IDF vectors.
   - Computes cosine similarity to find the most relevant response.
   - Returns the sentence with the highest similarity or a fallback if no match found.

5. **Graphical Interface**
   - Built using **PySimpleGUI**.
   - Components:
     - Multiline output display.
     - Input text box for user messages.
     - “Send” and “Exit” buttons.

6. **Event Loop**
   - Waits for user input.
   - Processes input and displays appropriate chatbot response.
   - Closes chat on "bye" or by clicking "Exit".

---

## 🛠️ Installation

1. **Clone the repository**

   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name


2. **Install required libraries**

   
   pip install numpy nltk scikit-learn PySimpleGUI
  

3. **Download NLTK data (one-time setup)**

   
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')


---

## ▶️ Run the Project

```bash
python chatbot.py
```


