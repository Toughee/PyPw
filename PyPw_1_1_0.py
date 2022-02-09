import tkinter as tk

import random

window = tk.Tk()

window.title("PyPw")
window.geometry("500x400")

mainlabel = tk.Label(text = "PwPw - Password generator app")
mainlabel.grid(column=1, row=1)

# secondlabel = tk.Label(text = "App desc")
# secondlabel.grid(column=2, row=2)


Div1 = ("ock", "K29Ty", "EfGV#", "A8v#R", "%tb5#2", "4Et3b", "0$rEq", "Ax^%B", "Hb$et*", "Z-ReU", "U@Yh2", "c8qf3")
Div2 = ("+12ds", "Pr&2Q", "Oeqwm", "A2kG1", "b2&ge", "68r!e", "Djh7^", "Gq$#7", "t3+qQ", "Fd2^o", "Yi3o4", "oIH&Y")
Div3 = ("tijr", "eWl32", "s2B2e", "Qio43", "&7320", "45r*d", "YFoz3!", "Jik#@", "76fd$", "ty3%A", "VweR&", "34tjD")
Div4 = ("Loe5^", "tr8km", "vt4Ro", "A$%@1", "b2%ge", "Uue32", "-Fd@2", "l45e3", "@ewyH", "U%h7B", "PoER3", "32I-j")
Div5 = ("P*Mos", "%&dsI", "387!_", "9dN7#", "9#fw", "b9Sc3", "T4d*8", "%R32k", "50Ue", "weIz7", "y4T&^r", "K9Q!2")


startSect = random.choice(Div1)
secondLeftSect = random.choice(Div2)
MiddleSect = random.choice(Div3)
secondRightSect = random.choice(Div4)
endSect = random.choice(Div5)


NewPw = startSect + secondLeftSect + MiddleSect + secondRightSect + endSect
print(NewPw)


# window.mainloop()


# EasyPw=tk.Button(text="Generate an easy password",
#     width=25,
#     height=2,
#     bg="green",
#     fg="white")

# EasyPw.grid(
#     column=3, 
#     row=1
#     )

