import random
import string
import customtkinter

customtkinter.set_appearance_mode("dark")  # tema
customtkinter.set_default_color_theme("green")  # tema dei pulsanti e label

root = customtkinter.CTk()
root.resizable(width=True, height=True)
root.title("Genera password by Ionà e Circosta")
root.geometry("600x550")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(pady=20, padx=60, fill="both", expand=True)

lettere = "" # dichiaro variabile globale lettere che deve venire "richiamata" in ogni metodo scrivendo "global lettere" per poterla usare


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


def printProva():
    print(":)")


# creazioni delle varie etichette

label = customtkinter.CTkLabel(master=frame, text="Generatore di password")
label.grid(row=0, column=1, pady=12, padx=10)

labelLunghezza = customtkinter.CTkLabel(master=frame, text="Lunghezza password: ")
labelLunghezza.grid(row=1, column=0, padx=20)

lunghezza = customtkinter.CTkEntry(master=frame)
lunghezza.grid(row=1, column=1, pady=10, padx=10)

labelQuantity = customtkinter.CTkLabel(master=frame, text="Quantità password da generare: ")
labelQuantity.grid(row=2, column=0, pady=10, padx=10)

quantity = customtkinter.CTkEntry(master=frame)
quantity.grid(row=2, column=1)
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
    risultato.configure(text=generaPassword(lettere)) # chiamata metodo diretto

    def copiaRisultato():
        root.clipboard_clear()
        root.clipboard_append(str(risultato.cget("text"))) # metodo cget per accedere al testo invece di accedere al parametro privato
        buttonCopia.configure(text="Copiato")

    buttonCopia = customtkinter.CTkButton(master=frame2, text="Copia", command=copiaRisultato)
    buttonCopia.grid(row=4, column=2, pady=12, padx=10)
    buttonCopia.configure(fg_color="red", hover_color="#642424")


def generaPassword(lettere): # estratto il vero metodo che genera la password e tolto l'inutile ciclo che non faceva un cazzo prob copiato da chatgpt senza guardare
    return ''.join(random.choice(lettere) for _i in range(int(lunghezza.get())))


def stampaPass(lettere, nuova_finestra, riga=1, Colonne=0):
    rigaL = riga  # 1
    rigaB = riga  # 1
    colonnaL = Colonne  # 0
    colonnaB = Colonne + 1  # 1
    cont = 0  # per contare quante pw sono state generate
    rigaMax = 11  # limite di righe per la finestra "pass generate" (aggiungere 1 al limite desiderato)

    for i in range(int(quantity.get())):
        cont += 1
        LabelQ = customtkinter.CTkLabel(nuova_finestra, text=f"Password {cont}: {generaPassword(lettere)}") # robba
        LabelQ.grid(row=rigaL, column=colonnaL, padx=20, pady=10)
        rigaL += 1

        if rigaL == rigaMax:
            colonnaL += 2
            rigaL = 1

        buttonQ = customtkinter.CTkButton(nuova_finestra, text="eheh")
        buttonQ.grid(row=rigaB, column=colonnaB, padx=2, pady=4)
        rigaB += 1
        if rigaB == rigaMax:
            colonnaB += 2
            rigaB = 1


def apriFinestra():
    global lettere
    # Crea la nuova finestra
    nuovaFinestra = customtkinter.CTkToplevel(root)
    nuovaFinestra.title("Password Generate")
    nuovaFinestra.geometry("500x500")

    labelMessaggio = customtkinter.CTkLabel(nuovaFinestra, text="Password Generate")
    labelMessaggio.grid(row=0, column=0)
    stampaPass(lettere, nuovaFinestra)


# Crea il pulsante nella finestra principale
pulsante = customtkinter.CTkButton(root, text="Vedi le tue password", command=apriFinestra)

pulsante.pack()

root.mainloop()
