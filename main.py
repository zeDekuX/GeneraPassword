import random
import string
import tkinter

import customtkinter as ctk

ctk.set_appearance_mode("dark")  # tema
ctk.set_default_color_theme("green")  # tema dei pulsanti e label

root = ctk.CTk()
root.resizable(width=False, height=False)
root.title("Genera password by Ionà e Circosta")
root.geometry("650x550")

# frame contentente gli input
frameInput = ctk.CTkFrame(master=root)
frameInput.pack(pady=20, padx=60, fill="both", expand=True)

# etichette input
labelGeneratorePasswords = ctk.CTkLabel(master=frameInput, text="Generatore di password")
labelGeneratorePasswords.grid(row=0, column=1, pady=12, padx=10)

labelLunghezzaPasswords = ctk.CTkLabel(master=frameInput, text="Lunghezza password: ")
labelLunghezzaPasswords.grid(row=1, column=0, padx=20)

entryLunghezzaPasswords = ctk.CTkEntry(master=frameInput)
entryLunghezzaPasswords.grid(row=1, column=1, pady=10, padx=10)

labelNumeroPasswords = ctk.CTkLabel(master=frameInput, text="Quantità password da generare: ")
labelNumeroPasswords.grid(row=2, column=0, pady=10, padx=10)

entryNumeroPasswords = ctk.CTkEntry(master=frameInput)
entryNumeroPasswords.grid(row=2, column=1)

# frame contenete i vari bottoni
frameBottoni = ctk.CTkFrame(master=root)
frameBottoni.pack(pady=20, padx=60, fill="both", expand=True)

# costanti, python non possiede costanti per convenzione le indichiama in CAPSLOCK
ALFABETOMINUSCOLO = string.ascii_lowercase
ALFABETOMAIUSCOLO = string.ascii_uppercase
ALFABETO = string.ascii_letters

CIFRE = string.digits
SIMBOLI = string.punctuation

ALFANUMERICO = ALFABETO + CIFRE
COMPLETO = ALFABETO + CIFRE + SIMBOLI
# attributi
lettere = ""  # dichiaro variabile globale lettere che deve venire "richiamata" in ogni metodo scrivendo "global


def generaPassMin():
    global lettere
    lettere = string.ascii_lowercase
    ris(lettere)


def generaPassMaiusc():
    global lettere
    lettere = string.ascii_uppercase
    ris(lettere)


def generaPassMinMaiusc():
    global lettere
    lettere = string.ascii_letters
    ris(lettere)


def generaPassSoloNumeri():
    global lettere
    lettere = string.digits
    ris(lettere)


def generaPassSoloSimboli():
    global lettere
    lettere = string.punctuation
    ris(lettere)


def generaAllPass():
    global lettere
    lettere = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    ris(lettere)


def generaAllPassSenzaSimboli():
    global lettere
    lettere = string.ascii_lowercase + string.ascii_uppercase + string.digits
    ris(lettere)


def ris(lettere):
    risultato.configure(text=generaPassword(lettere))  # chiamata metodo diretto


def printProva():
    print(":)")


# creazioni vari bottoni
button = ctk.CTkButton(master=frameBottoni, text="Minuscole", command=generaPassMin)
button.grid(row=2, column=0, pady=12, padx=10)

button1 = ctk.CTkButton(master=frameBottoni, text="Maiuscole", command=generaPassMaiusc)
button1.grid(row=2, column=1, pady=12, padx=10)

button2 = ctk.CTkButton(master=frameBottoni, text="Maiuscole e Minuscole", command=generaPassMinMaiusc)
button2.grid(row=2, column=2, pady=12, padx=10)

button3 = ctk.CTkButton(master=frameBottoni, text="Numeri", command=generaPassSoloNumeri)
button3.grid(row=3, column=0, pady=12, padx=10)

button4 = ctk.CTkButton(master=frameBottoni, text="Simboli", command=generaPassSoloSimboli)
button4.grid(row=3, column=1, pady=12, padx=10)

button5 = ctk.CTkButton(master=frameBottoni, text="No Simboli", command=generaAllPassSenzaSimboli)
button5.grid(row=3, column=2, pady=12, padx=10)

button6 = ctk.CTkButton(master=frameBottoni, text="Password Completa", command=generaAllPass)
button6.grid(row=4, column=1, pady=12, padx=10)

risultato = ctk.CTkLabel(master=frameInput, text="")
risultato.grid(row=1, column=2)


def copiaRisultato():
    root.clipboard_clear()
    root.clipboard_append(
        str(risultato.cget("text")))  # metodo cget per accedere al testo invece di accedere al parametro privato
    buttonCopia.configure(text="Copiato")


buttonCopia = ctk.CTkButton(master=frameBottoni, text="Copia", command=copiaRisultato)
buttonCopia.grid(row=4, column=2, pady=12, padx=10)
buttonCopia.configure(fg_color="red", hover_color="#642424")


def generaPassword(
        lettere):  # estratto il vero metodo che genera la password e tolto l'inutile ciclo che non faceva nulla
    return ''.join(random.choice(lettere) for _i in range(int(entryLunghezzaPasswords.get())))


global password


def stampaPass(lettere, nuovaFinestra, riga=1, Colonne=0):
    rigaL = riga  # 1
    rigaB = riga  # 1
    colonnaL = Colonne  # 0
    colonnaB = Colonne + 1  # 1
    cont = 0  # per contare quante pw sono state generate
    rigaMax = 11  # limite di righe per la finestra "pass generate" (aggiungere 1 al limite desiderato)
    global password
    password = []

    def copiaPassword(password):
        root.clipboard_clear()
        root.clipboard_append(str(password))

    for i in range(int(entryNumeroPasswords.get())):

        password.append(generaPassword(lettere))

        cont += 1
        LabelQ = ctk.CTkLabel(nuovaFinestra, text=f"Password {cont}: {password[cont - 1]}")
        LabelQ.grid(row=rigaL, column=colonnaL, padx=20, pady=10)
        rigaL += 1

        if rigaL == rigaMax:
            colonnaL += 2
            rigaL = 1

        buttonQ = ctk.CTkButton(nuovaFinestra, text="Copia",
                                command=lambda testo=password[cont - 1]: copiaPassword(testo))
        buttonQ.grid(row=rigaB, column=colonnaB, padx=2, pady=4)
        rigaB += 1
        if rigaB == rigaMax:
            colonnaB += 2
            rigaB = 1


def copiaTutto():
    global password
    sommaPassword = ""
    for i in password:
        sommaPassword += f"{i}\n"
    root.clipboard_clear()
    root.clipboard_append(sommaPassword)


def apriFinestra():
    global lettere
    # Crea la nuova finestra
    nuovaFinestra = ctk.CTkToplevel(root)
    nuovaFinestra.title("Password Generate")
    nuovaFinestra.geometry("750x550")
    nuovaFinestra.resizable(width=True, height=False)

    labelMessaggio = ctk.CTkLabel(nuovaFinestra, text="Password Generate")
    labelMessaggio.grid(row=0, column=0)
    stampaPass(lettere, nuovaFinestra)

    buttonCopiaTutto = ctk.CTkButton(nuovaFinestra, text="Copia Tutto", command=copiaTutto)
    buttonCopiaTutto.grid(row=0, column=1, padx=4, pady=10)
    buttonCopiaTutto.configure(fg_color="red", hover_color="#642424")


# Crea il pulsante nella finestra principale
pulsante = ctk.CTkButton(root, text="Vedi le tue password", command=apriFinestra)
pulsante.pack()

root.mainloop()
