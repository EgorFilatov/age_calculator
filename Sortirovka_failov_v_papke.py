from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime

days = []
months = []
years = []

first_day = 0
while len(days) < 31:
    first_day = first_day + 1
    days.append(first_day)

first_month = 0
while len(months) < 12:
    first_month = first_month + 1
    months.append(first_month)

first_year = 1900
while len(years) < 121:
    first_year = first_year + 1
    years.append(first_year)


window = Tk()
window.geometry('500x100+400+100')
window.title('Определение возраста')

current_datetime = datetime.now()
label_current_date = Label(window, text = 'Текущая дата: %d.%d.%d' % (current_datetime.day, current_datetime.month, current_datetime.year))
label_current_date.grid(column = 0, row = 0)

label_date_of_birth = Label(window, text = 'Введите дату вашего рождения:')
label_date_of_birth.grid(column = 0, row = 1)

combo_dd = Combobox(window, width = 3)
combo_dd['values'] = days
combo_dd.grid(column = 1, row = 1)
combo_dd.current(0)

combo_mm = Combobox(window, width = 3)
combo_mm['values'] = months
combo_mm.grid(column = 2, row = 1)
combo_mm.current(0)

combo_yy = Combobox(window, width = 6)
combo_yy['values'] = years
combo_yy.grid(column = 3, row = 1)
combo_yy.current(120)

age = 0
def calculate_age():
    if int(combo_yy.get()) < current_datetime.year:
        if int(combo_mm.get()) < current_datetime.month:
            age = current_datetime.year - int(combo_yy.get())
            label_show_age.config(text = 'Ваш возраст: %d' % age)
        if int(combo_mm.get()) > current_datetime.month:
            age = current_datetime.year - int(combo_yy.get())
            label_show_age.config(text = 'Ваш возраст: %d' % (age - 1))
        if int(combo_mm.get()) == current_datetime.month:
            if int(combo_dd.get()) <= current_datetime.day:
                age = current_datetime.year - int(combo_yy.get())
                label_show_age.config(text = 'Ваш возраст: %d' % age)
            if int(combo_dd.get()) > current_datetime.day:
                age = current_datetime.year - int(combo_yy.get())
                label_show_age.config(text = 'Ваш возраст: %d' % (age - 1))


button_calculate = Button(window, text = 'Рассчитать', command = calculate_age)
button_calculate.grid(column = 4, row = 1)


label_show_age = Label(window, text = 'Ваш возраст: ')
label_show_age.grid(column = 0, row = 2)












window.mainloop()

