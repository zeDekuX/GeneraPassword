import customtkinter
import random
import string

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x600")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


def generaPassMin(lunghezza):
    # Genera una stringa di caratteri minuscoli
    letters = string.ascii_lowercase

    # Crea una lista di caratteri casuali della lunghezza uguale alla variabie
    password = ''.join(random.choice(letters) for i in range(lunghezza))
    label = customtkinter.CTkLabel(master=frame, text=password)
    label.pack()
    print(password)


def generaPassMaiusc(lunghezza):
    # Genera una stringa di caratteri masciucola
    letters = string.ascii_uppercase

    # Crea una lista di caratteri casuali della lunghezza uguale alla variabie
    password = ''.join(random.choice(letters) for i in range(lunghezza))
    print(password)


def generaPassMinMaiusc(lunghezza):
    lettere = string.ascii_letters

    # Crea una lista di caratteri casuali della lunghezza uguale alla variabie
    password = ''.join(random.choice(lettere) for i in range(lunghezza))
    print(password)


def generaPassSoloNumeri(lunghezza):
    lettere = string.digits

    # Crea una lista di caratteri casuali della lunghezza uguale alla variabie
    password = ''.join(random.choice(lettere) for i in range(lunghezza))
    print(password)


def generaPassSoloSimboli(lunghezza):
    lettere = string.punctuation

    # Crea una lista di caratteri casuali della lunghezza uguale alla variabie
    password = ''.join(random.choice(lettere) for i in range(lunghezza))
    print(password)


def generaAllPass(lunghezza):
    lettere = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Crea una lista di caratteri casuali della lunghezza uguale alla variabie
    password = ''.join(random.choice(lettere) for i in range(lunghezza))
    print(password)


def generaAllPassSenzaSimboli(lunghezza):
    lettere = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Crea una lista di caratteri casuali della lunghezza uguale alla variabie
    password = ''.join(random.choice(lettere) for i in range(lunghezza))
    print(password)

def printProva():
    print(":)")

"""
generaPassMin(lunghezza)
generaPassMaiusc(lunghezza)
generaPassMinMaiusc(lunghezza)
generaPassSoloNumeri(lunghezza)
generaPassSoloSimboli(lunghezza)
generaAllPass(lunghezza)
generaAllPassSenzaSimboli(lunghezza)
"""
labelLunghezza = customtkinter.CTkLabel(master=frame, text="lunghezza password")
labelLunghezza.pack()

lunghezza = customtkinter.CTkEntry(master=frame)
lunghezza.pack()

label = customtkinter.CTkLabel(master=frame, text="Generatore di password")
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Minuscole", command=generaPassMin)
button.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Maiuscole", command=printProva)
button1.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Maiuscole e Minuscole", command=printProva)
button2.pack(pady=12, padx=10)

button3 = customtkinter.CTkButton(master=frame, text="Numeri", command=printProva)
button3.pack(pady=12, padx=10)

button4 = customtkinter.CTkButton(master=frame, text="Simboli", command=printProva)
button4.pack(pady=12, padx=10)

button5 = customtkinter.CTkButton(master=frame, text="No Simboli", command=printProva)
button5.pack(pady=12, padx=10)

button6 = customtkinter.CTkButton(master=frame, text="Password Completa", command=printProva)
button6.pack(pady=12, padx=10)


root.mainloop()
