import random
import string

import customtkinter

customtkinter.set_appearance_mode("dark")  # tema
customtkinter.set_default_color_theme("green")  # tema dei pulsanti e label

root = customtkinter.CTk()
root.resizable(width=True, height=False)
root.title("Genera password by Ionà e Circosta")
root.geometry("600x350")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(pady=20, padx=60, fill="both", expand=True)

def generaPassMin():
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


# creazioni delle varie etichette

label = customtkinter.CTkLabel(master=frame, text="Generatore di password")
label.grid(row=0, column=1, pady=12, padx=10)

labelLunghezza = customtkinter.CTkLabel(master=frame, text="lunghezza password")
labelLunghezza.grid(row=1, column=0)

lunghezza = customtkinter.CTkEntry(master=frame)
lunghezza.grid(row=1, column=1)

# creazioni vari bottoni

button = customtkinter.CTkButton(master=frame2, text="Minuscole", command=generaPassMin)
button.grid(row=2, column=0, pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame2, text="Maiuscole", command=generaPassMaiusc)
button1.grid(row=2, column=1, pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame2, text="Maiuscole e Minuscole", command=generaPassMinMaiusc)
button2.grid(row=2, column=2, pady=12, padx=10)

button3 = customtkinter.CTkButton(master=frame2, text="Numeri", command=generaPassSoloNumeri)
button3.grid(row=3, column=0, pady=12, padx=10)

button4 = customtkinter.CTkButton(master=frame2, text="Simboli", command=generaPassSoloSimboli)
button4.grid(row=3, column=1, pady=12, padx=10)

button5 = customtkinter.CTkButton(master=frame2, text="No Simboli", command=generaAllPassSenzaSimboli)
button5.grid(row=3, column=2, pady=12, padx=10)

button6 = customtkinter.CTkButton(master=frame2, text="Password Completa", command=generaAllPass)
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

    buttonCopia = customtkinter.CTkButton(master=frame2, text="Copia", command=copiaRisultato)
    buttonCopia.grid(row=4, column=2, pady=12, padx=10)

    buttonCopia.configure(fg_color="red", hover_color="#642424")

root.mainloop()
