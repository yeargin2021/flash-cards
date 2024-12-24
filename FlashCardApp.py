import tkinter as tk

# Flashcard data
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "What is the color of the sky?", "answer": "Blue"},
]


class FlashCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")

        self.current_card = 0  # Index of the current flashcard
        self.show_answer = False  # Whether to show the answer or question

        # Flashcard frame
        self.card_frame = tk.Frame(root, padx=40, pady=40, bg="white", relief=tk.RAISED, borderwidth=2)
        self.card_frame.pack(pady=20, padx=20)

        # Label to display question/answer
        self.content_label = tk.Label(self.card_frame, text="", font=("Helvetica", 16), wraplength=400,
                                      justify="center", bg="white")
        self.content_label.pack()

        # Button frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Navigation buttons
        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.prev_card, state="disabled")
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.flip_button = tk.Button(self.button_frame, text="Flip", command=self.flip_card)
        self.flip_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_card)
        self.next_button.pack(side=tk.LEFT, padx=10)

        # Show the first card
        self.update_card()

    def update_card(self):
        """Update the flashcard content shown."""
        card = flashcards[self.current_card]
        if self.show_answer:
            self.content_label.config(text=card["answer"])
        else:
            self.content_label.config(text=card["question"])

        # Update buttons' state
        self.prev_button.config(state="normal" if self.current_card > 0 else "disabled")
        self.next_button.config(state="normal" if self.current_card < len(flashcards) - 1 else "disabled")

    def flip_card(self):
        """Flip the card to show the opposite side."""
        self.show_answer = not self.show_answer
        self.update_card()

    def prev_card(self):
        """Go to the previous flashcard."""
        if self.current_card > 0:
            self.current_card -= 1
            self.show_answer = False
            self.update_card()

    def next_card(self):
        """Go to the next flashcard."""
        if self.current_card < len(flashcards) - 1:
            self.current_card += 1
            self.show_answer = False
            self.update_card()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashCardApp(root)
    root.mainloop()