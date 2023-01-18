from tkinter import * 

window = Tk()
window.title("Seznam úkolů")
window.minsize(400,400)
window.resizable(False, False)
window.iconbitmap("input/icon.ico")

# Fonty a Barvy
main_font = ("Times New Roman", 12)
main_color = "#dd7f00"
button_color = "#ffbe66"
window.config(bg=main_color)

# Funkce
def add_text():
    # přidání textu
    list_box.insert(END ,user_input.get())
    user_input.delete(0, END)

def remove_text_item():
    # odstraní jednu položku v seznamu
    list_box.delete(ANCHOR)

def clear_all_list():
    # odstraní všechny položky ze seznamu
    list_box.delete(0, END)

def save_tasks():
    # Uloží ukoly do textového souboru 
    with open("tasks.txt", "w") as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")

def open_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Chyba ve funkci na otevírání souboru .txt")

# Framy 
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg= main_color)
button_frame = Frame(window, bg=main_color)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# Input frame obsah
user_input = Entry(input_frame, width=35, borderwidth=3, font= main_font)
user_input.grid(row = 0, column = 0, padx=5, pady=5)

add_button = Button(input_frame, text= "Přidat", command= add_text, font=main_font, bg=button_color, borderwidth=2, padx=5, pady=5)
add_button.grid(row=0, column= 1, padx=5, pady=5, ipadx=10)

# Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky= NS)

# Text frame obsah
list_box = Listbox(text_frame, font=main_font, width = 45, borderwidth=3, height = 15, yscrollcommand=text_scrollbar.set)
list_box.grid(row= 0, column= 0)

# Propojení scrollbaru s textem
text_scrollbar.config(command=list_box.yview)

# Button Frame obsah
button1 = Button(button_frame, font=main_font, text="Odstranit položku", borderwidth=2, bg= button_color, command=remove_text_item)
button2 = Button(button_frame, font=main_font, text="Smazat seznam", borderwidth=2, bg= button_color, command=clear_all_list)
button3 = Button(button_frame, font=main_font, text="Uložit", borderwidth=2, bg= button_color, command= save_tasks)
button4 = Button(button_frame, font=main_font, text="Zavřít", borderwidth=2, bg= button_color, command= window.destroy)

button1.grid(row=0, column=0, padx=3, pady=10)
button2.grid(row=0, column=1, padx=3, pady=10)
button3.grid(row=0, column=2, padx=3, pady=10, ipadx=8)
button4.grid(row=0, column=3, padx=3, pady=10, ipadx=8)

# Načteme seznam ukolu do list boxu
open_tasks()

#
window.mainloop()