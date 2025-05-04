import tkinter as tk
from tkinter import ttk
from pyswip import Prolog
from tkinter import messagebox

prolog = Prolog()
prolog.consult('pakar_game_gui.pl')

genres = list()
features = dict()
index_genre = 0
index_feature = 0
current_genre = ""
current_feature = ""

def start_recommendation():
    global genres, features, index_genre, index_feature
    prolog.retractall("feature_pos(_)")  # Reset Prolog database
    prolog.retractall("feature_neg(_)") 
    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)
    # Get list of genres and features
    genres = [g["X"].decode() for g in list(prolog.query("genre(X)"))]
    for g in genres:
        features[g] = [f["X"] for f in list(prolog.query(f"feature(X,\"{g}\")"))]
    index_genre = 0
    index_feature = -1
    next_question()

def next_question(change_genre=False):
    global current_genre, current_feature, index_genre, index_feature
    if change_genre:
        index_genre += 1
        index_feature = -1
    if index_genre >= len(genres):  # All genres checked
        display_result()
        return
    current_genre = genres[index_genre]
    index_feature += 1
    if index_feature >= len(features[current_genre]):  # All features checked
        display_result(current_genre)
        return
    current_feature = features[current_genre][index_feature]
    if list(prolog.query(f"feature_pos({current_feature})")):
        next_question()
        return
    elif list(prolog.query(f"feature_neg({current_feature})")):
        next_question(change_genre=True)
        return
    question = list(prolog.query(f"question({current_feature},Y)"))[0]["Y"].decode()
    display_question(question)

def display_question(question):
    question_box.configure(state=tk.NORMAL)
    question_box.delete(1.0, tk.END)
    question_box.insert(tk.END, question)
    question_box.configure(state=tk.DISABLED)

def answer_response(answer):
    if answer:
        prolog.assertz(f"feature_pos({current_feature})")
    else:
        prolog.assertz(f"feature_neg({current_feature})")
    next_question(change_genre=not answer)

def display_result(genre=""):
    if genre:
        messagebox.showinfo("Rekomendasi Genre", f"Genre game yang cocok untuk Anda adalah: {genre}.")
    else:
        messagebox.showinfo("Rekomendasi Genre", "Tidak ada genre game yang cocok ditemukan.")
    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

# Tkinter GUI
root = tk.Tk()
root.title("Sistem Pakar Rekomendasi Genre Game")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Sistem Pakar Rekomendasi Genre Game",
          font=("Arial", 16)).grid(column=0, row=0, columnspan=3)

ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)

question_box = tk.Text(mainframe, height=4, width=40, state=tk.DISABLED)
question_box.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED,
                    command=lambda: answer_response(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED,
                     command=lambda: answer_response(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Rekomendasi",
                       command=start_recommendation)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
