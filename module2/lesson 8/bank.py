from course import get_currency, today
from tkinter import *

window = Tk()
window.geometry("500x500")
window_image = PhotoImage(file=r"/module2/lesson 8/bg.png")
bg_image = Label(window, image=window_image)
bg_image.grid(row=0, column=0)

image_logo = PhotoImage(file=r"/module2/lesson 8/logo.png")

label_logo = Label(window, image=image_logo)
label_logo.place(x=0, y=0)

label_title = Label(window, text='Банк Приколов', font='TimesNewRoman 36')
label_title.place(x=155, y=50)

label_currencies = Label(window, text=f'Курс валют на: {today}', font='TimesNewRoman 20')
label_currencies.place(x=10, y=160)

dollar_info = get_currency('R01235')
dollar_info_str = f'{dollar_info.get("name")} {dollar_info.get("value")}'

dollar_currency = Label(window, text=dollar_info_str, font='TimesNewRoman 16')
dollar_currency.place(x=10, y=210)

euro_info = get_currency('R01239')
euro_info_str = f'{euro_info.get("name")} {euro_info.get("value")}'

euro_currency = Label(window, text=euro_info_str, font='TimesNewRoman 16')
euro_currency.place(x=10, y=240)

yuan_info = get_currency('R01375')
yuan_info_str = f'{yuan_info.get("name")} {yuan_info.get("value")}'

yuan_currency = Label(window, text=yuan_info_str, font='TimesNewRoman 16')
yuan_currency.place(x=10, y=270)

entry = Entry(font='TimesNewRoman 16')
entry.place(x=10, y=400)

y = 30


def search():
    global y
    currency_id = entry.get()
    currency_info = get_currency(currency_id)
    currency_info_str = f'{currency_info.get("name")} {currency_info.get("value")}'
    currency_label = Label(window, text=currency_info_str, font='TimesNewRoman 16')
    currency_label.place(x=10, y=240 + y)

    y += 30


image_button = PhotoImage(file=r"/module2/lesson 8/click.png")
btnimage = image_button.subsample(160, 200)
button = Button(text='Найти', font='TimesNewRoman 16', command=search, image=btnimage, compound=RIGHT)
button.place(x=300, y=390)

window.resizable(width=False, height=False)
window.mainloop()
