import requests
import json
from tkinter import *
from tkinter import messagebox as mb

from бронирование_дораб import window

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx = 10, pady = 10)

entry = Entry()
entry.pack(palx = 10, pady = 10)

Button(text="Получить курс обмена валют", command = exchange).pack(palx = 10, pady = 10)


window.mainloop()





