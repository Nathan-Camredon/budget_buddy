import tkinter as tk

solde = 2864.22

def update_solde():
    solde_label.config(text=f"Solde : {solde:.2f}€")

def depot():
    global solde
    try:
        montant = float(montant_entry.get())
        solde += montant
        update_solde()
    except:
        pass

def retrait():
    global solde
    try:
        montant = float(montant_entry.get())
        if montant <= solde:
            solde -= montant
            update_solde()
    except:
        pass

window = tk.Tk()
window.title("Application Bancaire")
window.geometry("1000x550")
window.configure(bg="#333333")

tk.Label(window, text="Nom du compte", fg="#FF3399", bg="#333333",
         font=("Arial", 12)).place(x=30, y=20)

tk.Label(window, text="N° du compte", fg="#FF3399", bg="#333333",
         font=("Arial", 10)).place(x=30, y=50)

def bouton(text, y):
    return tk.Button(window, text=text,
                     bg="#333333", fg="#FF3399",
                     activebackground="#444444",
                     font=("Arial", 12, "bold"),
                     width=15, height=2).place(x=30, y=y)

bouton("Transactions", 120)
bouton("Dépôts", 200)
bouton("Retrait", 280)
bouton("Versement", 360)

solde_frame = tk.Frame(window, bg="#333333", width=400, height=80,
                       highlightbackground="#FF3399", highlightthickness=2)
solde_frame.place(x=400, y=80)

solde_label = tk.Label(solde_frame, text=f"Solde : {solde:.2f}€",
                       bg="#333333", fg="#FF3399",
                       font=("Arial", 16, "bold"))
solde_label.place(relx=0.5, rely=0.5, anchor="center")

content_frame = tk.Frame(window, bg="#333333", width=400, height=250,
                         highlightbackground="#FF3399", highlightthickness=2)
content_frame.place(x=400, y=180)

tk.Label(content_frame, text="Montant :", bg="#333333", fg="#FF3399").place(x=20, y=20)
montant_entry = tk.Entry(content_frame, bg="#555555", fg="#FF3399", insertbackground="#FF3399")
montant_entry.place(x=120, y=20)

tk.Label(content_frame, text="Description :", bg="#333333", fg="#FF3399").place(x=20, y=60)
desc_entry = tk.Entry(content_frame, bg="#555555", fg="#FF3399", insertbackground="#FF3399")
desc_entry.place(x=120, y=60)

tk.Button(content_frame, text="Déposer",
          bg="#FF3399", fg="white",
          command=depot).place(x=50, y=120)

tk.Button(content_frame, text="Retirer",
          bg="#FF3399", fg="white",
          command=retrait).place(x=200, y=120)


tk.Button(window, text="Déconnexion",
          bg="#FF3399", fg="white",
          width=20).place(x=600, y=450)


window.mainloop()