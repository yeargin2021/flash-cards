# Flashcard App

This is a simple Flashcard application built using Python and Tkinter. It allows users to navigate through a small set of flashcards, flipping them to view the question and answer, and moving forward and backward between cards.

---

## Features

- **Question and Answer Display:** Each flashcard has a question on one side and an answer on the other.
- **Navigation:** Use the "Next" and "Previous" buttons to go through the flashcards.
- **Flip Function:** You can flip a flashcard to switch between its question and answer.

---

## How to Use

1. Clone or manually download the repository to your local machine.
2. Open the project folder and ensure Python is installed on your system.
3. Run the app by executing the following command:
   ```bash
   python flashcard_app.py
   ```
4. A window will open, and the flashcard app will launch.

---

## How to Modify the App

### Modifying Flashcards

To change the flashcards or add more, edit the `flashcards` list in the `flashcard_app.py` file.

The `flashcards` list is defined like this:
```python
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "What is the color of the sky?", "answer": "Blue"},
]
```

Each flashcard is a dictionary containing:
- **`question`**: The question to display on the front of the card.
- **`answer`**: The answer to display when the card is flipped.

To edit an existing flashcard, update the `question` and `answer` content. For example:
```python
flashcards = [
    {"question": "What is the capital of Germany?", "answer": "Berlin"},  # Updated flashcard
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "What is the color of the sky?", "answer": "Blue"},
]
```

To add a new flashcard, append a new dictionary to the `flashcards` list:
```python
flashcards.append({"question": "What is 10 x 3?", "answer": "30"})
```

---

### Customizing the App's Appearance

You can modify the app's appearance by adjusting the following sections in the code:

#### 1. **Label Font**
The `content_label`'s font and style are defined as:
```python
self.content_label = tk.Label(self.card_frame, text="", font=("Helvetica", 16), wraplength=400, justify="center", bg="white")
```
- Update the font name, size, or background color if needed. For example:
```python
font=("Arial", 18)  # Change to Arial with size 18
bg="lightblue"      # Change the background color to light blue
```

#### 2. **Frame Appearance**
The flashcard frame's background color, border, and padding are configured in this line:
```python
self.card_frame = tk.Frame(root, padx=40, pady=40, bg="white", relief=tk.RAISED, borderwidth=2)
```
- For example, to change the border color and padding:
```python
bg="lightgray", padx=50, pady=50
```

---

## Example Updates for Practice

### Add a Fourth Flashcard
Add the following dictionary to the `flashcards` list:
```python
{"question": "What is the square root of 16?", "answer": "4"}
```

### Customize Fonts and Appearance
- Change all fonts to use `"Arial"` instead of `"Helvetica"`.
- Update the background of the flashcard frame to have a light gray color.

---

## Requirements

The app requires:
- **Python 3.x**
- **Tkinter**, which is included by default with Python installations.
