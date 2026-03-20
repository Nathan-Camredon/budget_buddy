import tkinter
from tkinter import messagebox

def hello():
    username="azerty"
    password="12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login success",message="successfully logged in.")
    else:
        messagebox.showerror(title="Login error",message="login not successfully in.")


window=tkinter.Tk()
window.title("Login form")
window.geometry("600x400")
window.configure(bg='#333333')
frame=tkinter.Frame(bg="#333333")
login_label=tkinter.Label(frame,text="Login",bg="#333333",fg="#FF3399",font=("Arial",30))
username_label=tkinter.Label(frame,text="Username",bg="#333333",fg="#FFFFFF",font=("Arial",16))
username_entry=tkinter.Entry(frame,font=("Arial",16))
password_entry=tkinter.Entry(frame,show="*",font=("Arial",16))
password_label=tkinter.Label(frame,text="password",bg="#333333",fg="#FFFFFF",font=("Arial",16))
button=tkinter.Button(frame,text="Login",bg="#FF3399",fg="#FFFFFF",command=hello)
frame.pack()

login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=20)
button.grid(row=3,column=0,columnspan=2,pady=30)


window.mainloop()
        