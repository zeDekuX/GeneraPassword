import customtkinter
import tkinter
import random
import string

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("600x600")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


def generaPassMin():
    # Genera una stringa di caratteri minuscoli
    lettere = string.ascii_lowercase

    ris(lettere)


def generaPassMaiusc():
    lettere = string.ascii_uppercase

    ris(lettere)


def generaPassMinMaiusc():
    lettere = string.ascii_letters

    ris(lettere)


def generaPassSoloNumeri():
    lettere = string.digits

    ris(lettere)


def generaPassSoloSimboli():
    lettere = string.punctuation

    ris(lettere)


def generaAllPass():
    lettere = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    ris(lettere)


def generaAllPassSenzaSimboli():
    lettere = string.ascii_lowercase + string.ascii_uppercase + string.digits

    ris(lettere)


def printProva():
    print(":)")


label = customtkinter.CTkLabel(master=frame, text="Generatore di password")
label.grid(row=0, column=1, pady=12, padx=10)

labelLunghezza = customtkinter.CTkLabel(master=frame, text="lunghezza password")
labelLunghezza.grid(row=1, column=0)

lunghezza = customtkinter.CTkEntry(master=frame)
lunghezza.grid(row=1, column=1)

button = customtkinter.CTkButton(master=frame, text="Minuscole", command=generaPassMin)
button.grid(row=2, column=0, pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Maiuscole", command=generaPassMaiusc)
button1.grid(row=2, column=1, pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Maiuscole e Minuscole", command=generaPassMinMaiusc)
button2.grid(row=2, column=2, pady=12, padx=10)

button3 = customtkinter.CTkButton(master=frame, text="Numeri", command=generaPassSoloNumeri)
button3.grid(row=3, column=0, pady=12, padx=10)

button4 = customtkinter.CTkButton(master=frame, text="Simboli", command=generaPassSoloSimboli)
button4.grid(row=3, column=1, pady=12, padx=10)

button5 = customtkinter.CTkButton(master=frame, text="No Simboli", command=generaAllPassSenzaSimboli)
button5.grid(row=3, column=2, pady=12, padx=10)

button6 = customtkinter.CTkButton(master=frame, text="Password Completa", command=generaAllPass)
button6.grid(row=4, column=1, pady=12, padx=10)

risultato = customtkinter.CTkLabel(master=frame, text="")
risultato.grid(row=1, column=2)

def ris(lettere):
    password = ''.join(random.choice(lettere) for i in range(int(lunghezza.get())))
    risultato.configure(text=password)
    def copiaRisultato():
        root.clipboard_clear()
        root.clipboard_append(str(risultato._text))
        buttonCopia.configure(text="Copiato")

    buttonCopia = customtkinter.CTkButton(master=frame, text="Copia", command=copiaRisultato)
    buttonCopia.grid(row=9, column=2, pady=12, padx=10)

    buttonCopia.configure(fg_color="red",hover_color="#642424")


root.mainloop()
