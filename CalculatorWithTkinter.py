import tkinter

def dodajTextVoEntry(text):
    entry.insert(tkinter.END, text)

def calculate():
    str_to_calculate = str(entry.get())
    calc = eval(str_to_calculate)
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, calc)


screen = tkinter.Tk()
screen.title('Calculator')

screen.geometry("400x500")
screen.config(padx=20, pady=20, bg="#1D1B2A")  # Dark purple base

entry = tkinter.Entry(screen, bg="#2E294E", fg="yellow", insertbackground="yellow", relief="flat", highlightbackground="#6C567B", highlightcolor="#6C567B", bd=2)
entry.config(width=20, font=("default", 14))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

button_color = "#5D3A5A"
text_color = "white"

def create_button(screen, text, row, col, command):
    button = tkinter.Button(screen, text=text, command=command, bg=button_color, fg=text_color, borderwidth=1, relief="ridge")
    button.grid(row=row, column=col, padx=5, pady=5)
    button.config(width=5, height=2)
    return button

# Buttons
create_button(screen, "1", 3, 0, lambda: dodajTextVoEntry("1"))
create_button(screen, "2", 3, 1, lambda: dodajTextVoEntry("2"))
create_button(screen, "3", 3, 2, lambda: dodajTextVoEntry("3"))
create_button(screen, "4", 2, 0, lambda: dodajTextVoEntry("4"))
create_button(screen, "5", 2, 1, lambda: dodajTextVoEntry("5"))
create_button(screen, "6", 2, 2, lambda: dodajTextVoEntry("6"))
create_button(screen, "7", 1, 0, lambda: dodajTextVoEntry("7"))
create_button(screen, "8", 1, 1, lambda: dodajTextVoEntry("8"))
create_button(screen, "9", 1, 2, lambda: dodajTextVoEntry("9"))
create_button(screen, "0", 4, 1, lambda: dodajTextVoEntry("0"))
create_button(screen, "+", 4, 3, lambda: dodajTextVoEntry("+"))
create_button(screen, "-", 3, 3, lambda: dodajTextVoEntry("-"))
create_button(screen, "*", 2, 3, lambda: dodajTextVoEntry("*"))
create_button(screen, "/", 1, 3, lambda: dodajTextVoEntry("/"))
create_button(screen, "=", 5, 3, calculate)

## screen end
screen.mainloop()
