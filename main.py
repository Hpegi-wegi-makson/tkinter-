
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showerror, showwarning, showinfo
import tkinter as tk
import datetime
from pyexpat.errors import messages


current_datetime = datetime.datetime.now()
main_window = Tk()
main_window.title("METANIT.COM")
main_window.geometry("700x600+600+250")

conn = sqlite3.connect(r'C:\Users\Maksz\PycharmProjects\Tkinter_1\Existing_accounts.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS AccountCreated (
                  id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  login TEXT,
                  password TEXT,
                  fio TEXT
                  )
''')


#cursor.execute('''CREATE TABLE IF NOT EXISTS Applications (
 #                 application_number INTEGER PRIMARY KEY AUTOINCREMENT,
  #                datatime TEXT,
   #               equipment_in_need_of_repair TEXT,
    #              type_of_malfunction TEXT,
     #             problem description TEXT,
      #            fio_client TEXT
       #           FOREIGN KEY (fio) REFERENCES AccountCreated (fio)
        #          )
#''')

registr_login_value = StringVar()
registr_password_value = StringVar()
login_fio_value = StringVar()

def adding_to_variable():
    registr_login_value_sql = registr_login_value.get()
    registr_password_value_sql = registr_password_value.get()
    login_fio_value_sql = login_fio_value.get()
    showinfo(title="Акккаунт успешно создан", message="Акккаунт успешно создан")
    cursor.execute(
        "INSERT INTO AccountCreated (login, password, fio) VALUES (?,?,?)",
        (registr_login_value_sql, registr_password_value_sql,login_fio_value_sql)
    )
    conn.commit()
    print(f"Login: {registr_login_value_sql}, Password: {registr_password_value_sql},ФИО: {login_fio_value_sql} ")


login_login_value = StringVar()
login_password_value = StringVar()


def adding_and_checking():
    login_login_value_sql = login_login_value.get()
    login_password_value_sql = login_password_value.get()
    print(f"Login: {login_login_value_sql}, Password: {login_password_value_sql} ")
    cursor.execute(f'''
                              SELECT login, password, id FROM AccountCreated
                              WHERE login="{login_login_value_sql}" AND password="{login_password_value_sql}"
    ''')
    result = cursor.fetchone()
    print(result)
    if result is not None:
        db_id,db_login, db_password = result
        print(())
        login_next_level()
    else:showerror(title="Ошибка", message="В базе данных нет созданного аккаунта с таким паролем или логином")

def login_next_level():
    for widget in main_window.winfo_children():  # удаляет все прошлые элементы
        widget.destroy()

    text_create_application = ttk.Label(text="Создать заявку ", font=20)
    button_create_application = ttk.Button(text="Создать",command=window_create_application)

    text_viewing_application = ttk.Label(text="Посмотреть статус заявки", font=20)
    button_viewing_application = ttk.Button(text="Посмотреть")

    text_create_application.grid(row=0, column=0, padx=50, pady=100, ipadx=30, ipady=20)
    button_create_application.grid(row=1, column=0, padx=50, pady=10, ipadx=30, ipady=20)
    text_viewing_application.grid(row=0, column=1, padx=50, pady=100, ipadx=30, ipady=20)
    button_viewing_application.grid(row=1, column=1, padx=50, pady=10, ipadx=30, ipady=20)




def window_create_application():
    for widget in main_window.winfo_children():  # удаляет все прошлые элементы
        widget.destroy()
    device = ["Мышь", "Клавиатура", "Системный блок", "Монитор", "Инернет"]
    fault_options = ["Невозможно пользоваться", "Можно пользоваться,но с трудом", "Немного мешает при пользование"]

    def get_device():
        index = listbox_application.curselection()[0]
        selected_item = listbox_application.get(index)
        listbox_application_two.insert(tk.END, selected_item)
        listbox_application.delete(index)


    def delite_device():
        index = listbox_application_two.curselection()
        selected_item = listbox_application_two.get(index)
        listbox_application.insert(tk.END, selected_item)
        listbox_application_two.delete(index)

    selected_fault = StringVar()
    device_var = Variable(value=device)


    def get_info_window_create_application():
        broken_devices = listbox_application_two.get(0, tk.END)
        print(current_datetime)
        print(broken_devices)
        problem_description_text = text_problem_description.get("1.0", tk.END)
        print(problem_description_text)
        selected_fault_sql = selected_fault.get()
        print(selected_fault_sql)

     #   cursor.execute('''
     #       SELECT fio
      #      FROM AccountCreated
      #      WHERE login="{login_login_value_sql}"
      #  ''',
      #                 )
     #   fio_client = cursor.fetchone()[0]
      #  cursor.execute(
      #      "INSERT INTO Applications (datatime, equipment_in_need_of_repair,type_of_malfunction, problem description, fio_client) VALUES (?,?,?,?,?)",
       #     (current_datetime, broken_devices, problem_description_text,selected_fault_sql, login_fio_value_sql)
      #  )



    listbox_application = Listbox(listvariable=device_var, height=5, width=15)
    listbox_application_two = Listbox(height=6, width=15)
    button_get_device = ttk.Button(text="Добавить", command=get_device)
    text_what_get_device = ttk.Label(text="Выберите какое оборудование у вас не исправно и добовьте", font=18 )
    button_delite_device = ttk.Button(text="Удалить из выбранного",command=delite_device)
    button_back_login_menu = ttk.Button(text="Назад в меню ⟸", command=login_next_level)
    text_heder_window_radiobutton = ttk.Label(text="Выберите и опишите  неисправности", font=18)
    text_problem_description = Text(height=8, width=15)
    button_send_request = ttk.Button(text="Отправить заявку",command=get_info_window_create_application)

    #broken_devices = listbox_application_two.get(0, tk.END)        здесь будет лежать весь товар который выбрали как сломанный
    #print(contents)

    listbox_application.grid(row=1, column=0, rowspan=2, padx=(10, 5), pady=10,)
    listbox_application_two.grid(row=1, column=1, rowspan=2, padx=(5, 10), pady=10)
    button_get_device.grid(row=1, column=2, padx=(10, 10), pady=10)
    text_what_get_device.grid(row=0, columnspan=3, padx=10, pady=(10, 20), sticky='w')
    button_delite_device.grid(row=2, column=2, padx=(10, 10), pady=10)
    button_back_login_menu.grid(row=1, column=3, padx=(10, 10), pady=10)
    text_heder_window_radiobutton.grid()
    text_problem_description.grid(row=9, column=0, columnspan=2, pady=10)
    button_send_request.grid(row=10, column=2, columnspan=2, pady=10)


    def select_fuc_fault():
        text_heder_window_radiobutton.config(text=f"Выбрано: {selected_fault.get()}")
    i= 0
    for mistake in fault_options:
        button_mistakes = ttk.Radiobutton(text=mistake, value=mistake, variable=selected_fault,
                                          command=select_fuc_fault)
        button_mistakes.grid(row=i + 4, column=0, sticky='w')
        i += 1


def registr_menu():
    for widget in main_window.winfo_children(): #удаляет все прошлые элементы
        widget.destroy()

    text_login = ttk.Label(text="Логин: ", font=20)
    entry_login = ttk.Entry(font=14, textvariable=registr_login_value)

    text_password = ttk.Label(text="Пароль: ", font=20)
    entry_password = ttk.Entry(font=14, textvariable=registr_password_value)

    text_fio = ttk.Label(text="ФИО: ", font=20)
    entry_fio = ttk.Entry(font=14, textvariable=login_fio_value)

    button_back_login_menu = ttk.Button(text="Назад ⟸",command=login_and_registr_menu)

    button_ready_login_menu = ttk.Button(text="Создать",command=adding_to_variable)


    text_login.grid(row=0, column=0, padx=50, pady=10, ipadx=30, ipady=20)
    entry_login.grid(row=0, column=1)
    text_password.grid(row=1, column=0, padx=50, pady=(0, 150), ipadx=30, ipady=20)
    entry_password.grid(row=1, column=1, pady=(0, 150))
    button_back_login_menu.place(relx=1,rely=0,anchor=NE,height=50)
    button_ready_login_menu.grid(row=2, column=1, ipadx=50, ipady=20, padx=(0, 150))
    text_fio.grid(row=1, column=0)
    entry_fio.grid(row=1, column=1)

def login_menu():
    for widget in main_window.winfo_children(): #удаляет все прошлые элементы
        widget.destroy()


    for widget in main_window.winfo_children(): #удаляет все прошлые элементы
        widget.destroy()

    text_login = ttk.Label(text="Логин: ", font=20)
    entry_login = ttk.Entry(font=14, textvariable=login_login_value)

    text_password = ttk.Label(text="Пароль: ", font=20)
    entry_password = ttk.Entry(font=14, textvariable=login_password_value)

    button_back_login_menu = ttk.Button(text="Назад ⟸",command=login_and_registr_menu)

    button_ready_login_menu = ttk.Button(text="Войти", command=adding_and_checking)


    text_login.grid(row=0, column=0, padx=50, pady=100, ipadx=30, ipady=20)
    entry_login.grid(row=0, column=1)
    text_password.grid(row=1, column=0, padx=50, pady=(0, 70), ipadx=30, ipady=20)
    entry_password.grid(row=1, column=1, pady=(0, 70))
    button_back_login_menu.place(relx=1,rely=0,anchor=NE,height=50)
    button_ready_login_menu.grid(row=2, column=1, ipadx=50, ipady=20, padx=(0, 150))




def login_and_registr_menu():
    for widget in main_window.winfo_children(): #удаляет все прошлые элементы
        widget.destroy()
    button_register = ttk.Button(main_window, text="Создать аккаунт", command=registr_menu)
    button_register.pack(side = LEFT, anchor = W, padx=50,  ipadx=20, ipady=20)

    button_login = ttk.Button(main_window, text="Войти в аккаунт", command=login_menu)
    button_login.pack(side = RIGHT, anchor=E, padx=50,  ipadx=20, ipady=20)
button_go = ttk.Button( text="Не робот", command=login_and_registr_menu)
button_go.pack(pady=20)

main_window.mainloop()