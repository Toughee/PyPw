import tkinter as tk

window = tk.Tk()

window.title("PyPw")
window.geometry("500x700")

mainlabel = tk.Label(text = "PwPw - Password generator app")
mainlabel.grid(column=1, row=1)

secondlabel = tk.Label(text = "App desc")
secondlabel.grid(column=2, row=2)

thirdlabel = tk.Label(text = "Choose an option below")
thirdlabel.grid(column=3, row=3)

EasyPw=tk.Button(text="Generate an easy password",
    width=25,
    height=2,
    bg="green",
    fg="white")

EasyPw.grid(
    column=3, 
    row=1
    )

window.mainloop()

# resultlabel = tk.Label(text = "Your Password is")
# resultlabel.grid(column=1, row=1)


#  Pseudocode section

    # length - 8
    # class EasyPw
        # Easy to remember password
        # onclick
        # generate + send to resulttab

    # length 12
    # class mediumPW


    # length 16

    # class hardPw

    # length 24


    #class veryhardPw

    # length 32

    # class ultraHardPw

    # class passphrase # 8 words

    # class harderPassphrase # 12 words

    # class hardestPassphrase # 20 words

    # "This is your new Password. Write it down and make sure not to give it to anybody"

    # Copy your new password

    # button onclick
        # Password copied successfully!