import tkinter as tk
from tkinter import messagebox
import random

word_hint_dict = {
    "python": "Popular programming language 🐍 (Programming)",
    "function": "Reusable block of code 🧱 (Programming)",
    "loop": "Used to repeat a block 🔁 (Programming)",

    "tiger": "A big striped cat 🐅 (Animal)",
    "elephant": "Largest land animal 🐘 (Animal)",
    "penguin": "A bird that can't fly 🐧 (Animal)",

    "pizza": "Cheesy Italian delight 🍕 (Food)",
    "burger": "Layered fast food 🍔 (Food)",
    "noodles": "Long stringy food 🍜 (Food)",

    "batman": "Dark Knight 🦇 (Movie)",
    "avatar": "Blue alien epic 🌌 (Movie)",
    "joker": "Famous villain with a smile 🎭 (Movie)",

    "brazil": "Football crazy country 🌎 (Country)",
    "japan": "Land of anime and sushi 🇯🇵 (Country)",
    "canada": "Land of maple leaf 🍁 (Country)",

    "cricket": "Bat and ball sport 🏏 (Sport)",
    "tennis": "Game with rackets 🎾 (Sport)",
    "boxing": "Gloves and punches 🥊 (Sport)",

    "guitar": "String musical instrument 🎸 (Music)",
    "camera": "Used to click photos 📷 (Object)",
    "rocket": "Travels to space 🚀 (Object)",
    "sunflower": "Yellow and follows sun 🌻 (Nature)",
    "laptop": "Portable computer 💻 (Tech)",
}

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 Hangman — 21st Century Edition")
        self.root.configure(bg="#1e1e1e")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.max_attempts = 5
        self.word = ""
        self.hint = ""
        self.display = []
        self.guessed_letters = []
        self.attempts = 0
        self.used_hint = False

        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Hangman Game", font=("Arial", 20, "bold"),
                                    fg="#00ffff", bg="#1e1e1e")
        self.title_label.pack(pady=10)

        self.word_label = tk.Label(self.root, text="", font=("Courier", 26), fg="white", bg="#1e1e1e")
        self.word_label.pack(pady=10)

        self.attempts_label = tk.Label(self.root, text="", font=("Arial", 14), fg="orange", bg="#1e1e1e")
        self.attempts_label.pack(pady=5)

        self.input_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Enter letter:", font=("Arial", 12), fg="white", bg="#1e1e1e").grid(row=0, column=0)

        self.entry = tk.Entry(self.input_frame, font=("Arial", 14), width=5, justify='center')
        self.entry.grid(row=0, column=1, padx=5)
        self.entry.focus()

        self.guess_button = tk.Button(self.input_frame, text="Guess", command=self.check_guess, font=("Arial", 12))
        self.guess_button.grid(row=0, column=2, padx=5)

        self.hint_button = tk.Button(self.root, text="💡 Show Hint", command=self.show_hint, font=("Arial", 12))
        self.hint_button.pack(pady=5)

        self.hint_label = tk.Label(self.root, text="", font=("Arial", 10, "italic"), fg="gray", bg="#1e1e1e")
        self.hint_label.pack()

        self.reset_button = tk.Button(self.root, text="🔁 New Game", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=10)

    def reset_game(self):
        self.word, self.hint = random.choice(list(word_hint_dict.items()))
        self.display = ['_'] * len(self.word)
        self.guessed_letters = []
        self.attempts = 0
        self.used_hint = False

        rand_index = random.randint(0, len(self.word) - 1)
        revealed_letter = self.word[rand_index]
        for i in range(len(self.word)):
            if self.word[i] == revealed_letter:
                self.display[i] = revealed_letter
        self.guessed_letters.append(revealed_letter)

        self.update_display()
        self.update_attempts()
        self.hint_label.config(text="")
        self.entry.config(state='normal')
        self.guess_button.config(state='normal')
        self.hint_button.config(state='normal')

    def update_display(self):
        self.word_label.config(text=' '.join(self.display))

    def update_attempts(self):
        self.attempts_label.config(text=f"Attempts left: {self.max_attempts - self.attempts}/{self.max_attempts}")

    def check_guess(self):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            messagebox.showwarning("Invalid Input", "Please enter a single alphabet.")
            return

        if letter in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You already guessed '{letter}'.")
            return

        self.guessed_letters.append(letter)

        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.display[i] = letter
            self.update_display()
        else:
            self.attempts += 1
            self.update_attempts()

        if '_' not in self.display:
            self.end_game(True)
        elif self.attempts >= self.max_attempts:
            self.end_game(False)

    def show_hint(self):
        if not self.used_hint:
            self.hint_label.config(text=f"Hint: {self.hint}")
            self.used_hint = True
            self.hint_button.config(state='disabled')

    def end_game(self, won):
        self.entry.config(state='disabled')
        self.guess_button.config(state='disabled')
        self.hint_button.config(state='disabled')

        if won:
            messagebox.showinfo("🎉 You Win!", f"Congrats! The word was: '{self.word}'")
        else:
            self.word_label.config(text=' '.join(list(self.word)))
            messagebox.showerror("💀 Game Over", f"Oops! You ran out of attempts. The word was '{self.word}'")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()