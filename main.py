from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showerror, showwarning, showinfo
import tkinter as tk
import datetime
from pyexpat.errors import messages

class HelloWorld:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("METANIT.COM")
        self.main_window.geometry("700x600+600+250")


        self.data_time = datetime.datetime.now()
        self.entry_login_new_user_value = StringVar()
        self.entry_password_new_user_value = StringVar()
        self.entry_fio_new_user_value = StringVar()
        self.entry_role_new_user_value = StringVar()

        self.conn = sqlite3.connect(r'C:\Users\Maksz\PycharmProjects\Tkinter_2\Existing_accounts.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                          id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          login TEXT,
                          password TEXT,
                          fio TEXT,
                          role TEXT
                          )'''
                            )

        self.authorization_window()


        login = "admin"
        password = "admin_pass"
        fio = "admin"
        role = "admin"


        self.cursor.execute(f'''
            SELECT fio 
            FROM User 
            WHERE login="{login}"
        ''',
                       )
        self.result = self.cursor.fetchone()
        if not self.result:
            self.cursor.execute(
                "INSERT INTO User (login, password, fio,role) VALUES (?,?,?,?)",
                (login, password, fio,role)
            )
            self.conn.commit()





        self.main_window.mainloop()


    def authorization_window(self):
        for widget in self.main_window.winfo_children():  # удаляет все прошлые элементы
            widget.destroy()
        self.text_authorization_login = ttk.Label(text="Логин",font=20)
        self.entry_authorization_login = ttk.Entry(font=14)

        self.text_authorization_password = ttk.Label(text="Пароль",font=20)
        self.entry_authorization_password = ttk.Entry(font=14)

        self.button_authorization_creat = ttk.Button(text="Войти", command=self.checking_accaunt)

        self.text_authorization_login.grid(row=0, column=0, padx=50, pady=10, ipadx=30, ipady=20)
        self.entry_authorization_login.grid(row=0, column=1)
        self.text_authorization_password.grid(row=1, column=0, padx=50, pady=(0, 150), ipadx=30, ipady=20)
        self.entry_authorization_password.grid(row=1, column=1, pady=(0, 150))
        self.button_authorization_creat.grid(row=2, column=1, ipadx=50, ipady=20, padx=(0, 150))

    def checking_accaunt(self):

        self.entry_login_authorization_window_value_sql = self.entry_authorization_login.get()
        self.entry_password_authorization_window_value_sql = self.entry_authorization_password.get()
        self.entry_fio_authorization_window_value_sql = self.entry_fio_new_user_value.get()
        self.entry_role_authorization_window_value_sql = self.entry_role_new_user_value.get()

        self.cursor.execute(f'''
                                                    SELECT login,password 
                                                    FROM User 
                                                    WHERE login ="{self.entry_login_authorization_window_value_sql}" AND password = "{self.entry_password_authorization_window_value_sql}"
        ''')
        self.result = self.cursor.fetchone()
        print(self.result)
        if self.result is not None:
            db_login, db_password = self.result
            print(123)
            self.main_screan()
        print(self.result)

    def main_screan (self):
        for widget in self.main_window.winfo_children():  # удаляет все прошлые элементы
            widget.destroy()

        if self.result[0] == 'admin':


            self.button_new_request = ttk.Button(text="Новая заявка",width=25, command=self.creat_new_request)

            self.button_list_request = ttk.Button(text="Посмотреть заявки",width=25)

            self.button_create_new_worker = ttk.Button(text="Создать работника",width=25, command=self.create_new_user)

            self.button_create_list_worker = ttk.Button(text="Список пользователей",width=25)

            self.button_back_authorization_window = ttk.Button(text="Назад!",command=self.authorization_window)

            self.button_new_request.grid(row=0, column=1, ipady=15)
            self.button_list_request.grid(row=1, column=2, ipady=15)
            self.button_create_new_worker.grid(row=2, column=3, ipady=15)
            self.button_create_list_worker.grid(row=3, column=4, ipady=15)
            self.button_back_authorization_window.grid(row=1, column=3, padx=(10, 10), pady=10)
        else:
            self.button_new_request = ttk.Button(text="Новая заявка",width=25,command=self.creat_new_request)

            self.button_list_request = ttk.Button(text="Посмотреть заявки",width=25)

            self.button_back_authorization_window = ttk.Button(text="Назад!",command=self.authorization_window)

            self.button_new_request.grid(row=0, column=1, ipady=15)
            self.button_list_request.grid(row=1, column=2, ipady=15)
            self.button_back_authorization_window.grid(row=1, column=3, padx=(10, 10), pady=10)
    def save_creat_new_request(self):
        print(self.data_time)
        self.broken_devices = self.listbox_application_two.get(0, tk.END)
        print(self.broken_devices)
        self.problem_description_text = self.text_problem_description.get("1.0", tk.END)
        print(self.problem_description_text)
        self.selected_fault_sql = self.selected_fault.get()
        print(self.selected_fault_sql)
        print()
        self.entry_fio_new_user_value_sql = self.entry_fio_new_user_value.get()
        print(self.entry_fio_new_user_value_sql)
        self.cursor.execute("")



    def creat_new_request(self):
        for widget in self.main_window.winfo_children():  # удаляет все прошлые элементы
            widget.destroy()

        self.device = ["Мышь", "Клавиатура", "Системный блок", "Монитор", "Инернет"]
        self.fault_options = ["в ожидании", "в работе", "выполнено"]

        self.selected_fault = StringVar()
        self.device_var = Variable(value=self.device)

        self.listbox_application = Listbox(listvariable=self.device_var, height=5, width=15)
        self.listbox_application_two = Listbox(height=6, width=15)
        self.button_get_device = ttk.Button(text="Добавить", command=self.get_device)
        self.text_what_get_device = ttk.Label(text="Выберите какое оборудование у вас не исправно и добовьте", font=18)
        self.button_delite_device = ttk.Button(text="Удалить из выбранного", command=self.delite_device)
        self.button_back_login_menu = ttk.Button(text="Назад в меню ⟸",command=self.main_screan)
        self.text_heder_window_radiobutton = ttk.Label(text="Выберите и опишите  неисправности", font=18)
        self.text_problem_description = Text(height=8, width=15)
        self.button_send_request = ttk.Button(text="Отправить заявку", command=self.save_creat_new_request)
        self.text_fio_creat_new_request = ttk.Label(text="ФИО клиента")
        self.entry_fio_creat_new_request = ttk.Entry(textvariable=self.entry_fio_new_user_value)



        self.listbox_application.grid(row=1, column=0, rowspan=2, padx=(10, 5), pady=10, )
        self.listbox_application_two.grid(row=1, column=1, rowspan=2, padx=(5, 10), pady=10)
        self.button_get_device.grid(row=1, column=2, padx=(10, 10), pady=10)
        self.text_what_get_device.grid(row=0, columnspan=3, padx=10, pady=(10, 20), sticky='w')
        self.button_delite_device.grid(row=2, column=2, padx=(10, 10), pady=10)
        self.button_back_login_menu.grid(row=1, column=3, padx=(10, 10), pady=10)
        self.text_heder_window_radiobutton.grid()
        self.text_problem_description.grid(row=9, column=0, columnspan=2, pady=10)
        self.button_send_request.grid(row=10, column=2, columnspan=2, pady=10)
        self.text_fio_creat_new_request.grid()
        self.entry_fio_creat_new_request.grid()
        i = 0
        for mistake in self.fault_options:
            button_mistakes = ttk.Radiobutton(text=mistake, value=mistake, variable=self.selected_fault,
                                              command=self.select_fuc_fault)
            button_mistakes.grid(row=i + 4, column=0, sticky='w')
            i += 1



    def get_device(self):
        index = self.listbox_application.curselection()[0]
        selected_item = self.listbox_application.get(index)
        self.listbox_application_two.insert(tk.END, selected_item)
        self.listbox_application.delete(index)

    def delite_device(self):
        index = self.listbox_application_two.curselection()
        selected_item = self.listbox_application_two.get(index)
        self.listbox_application.insert(tk.END, selected_item)
        self.listbox_application_two.delete(index)



        # broken_devices = listbox_application_two.get(0, tk.END)        здесь будет лежать весь товар который выбрали как сломанный
        # print(contents)



    def select_fuc_fault(self):
        self.text_heder_window_radiobutton.config(text=f"Выбрано: {self.selected_fault.get()}")


    def create_new_user(self):
        for widget in self.main_window.winfo_children():  # удаляет все прошлые элементы
            widget.destroy()


        self.text_login_new_user = ttk.Label(text="Login",font=20)
        self.entry_login_new_user = ttk.Entry(textvariable=self.entry_login_new_user_value)

        self.text_password_new_user = ttk.Label(text="Password",font=20)
        self.entry_password_new_user = ttk.Entry(textvariable=self.entry_password_new_user_value)

        self.text_fio_new_user = ttk.Label(text="FIO",font=20)
        self.entry_fio_new_user = ttk.Entry(textvariable=self.entry_fio_new_user_value)

        self.text_role_new_user = ttk.Label(text="ROLE",font=20)
        self.entry_role_new_user = ttk.Entry(textvariable=self.entry_role_new_user_value)

        self.button_save_new_user = ttk.Button(text="Cохранить",command=self.save_new_user)
        self.button_back_main_screan = ttk.Button(text="Назад!", command=self.main_screan)

        self.text_login_new_user.grid(row=0, column=0, sticky='e', pady=10)
        self.entry_login_new_user.grid(row=0, column=1, padx=10, pady=10)

        self.text_password_new_user.grid(row=1, column=0, sticky='e', pady=10)
        self.entry_password_new_user.grid(row=1, column=1, padx=10, pady=10)

        self.text_fio_new_user.grid(row=2, column=0, sticky='e', pady=10)
        self.entry_fio_new_user.grid(row=2, column=1, padx=10, pady=10)

        self.text_role_new_user.grid(row=3, column=0, sticky='e', pady=10)
        self.entry_role_new_user.grid(row=3, column=1, padx=10, pady=10)

        self.button_save_new_user.grid(row=4, columnspan=2, pady=10)
        self.button_back_main_screan.grid(row=1, column=3, padx=(10, 10), pady=10)

    def save_new_user(self):
        self.entry_login_new_user_value_sql = self.entry_login_new_user_value.get()
        self.entry_password_new_user_value_sql = self.entry_password_new_user_value.get()
        self.entry_fio_new_user_value_sql = self.entry_fio_new_user_value.get()
        self.entry_role_new_user_value_sql = self.entry_role_new_user_value.get()
        print(f"Login: {self.entry_login_new_user_value_sql}, Password: {self.entry_password_new_user_value_sql} ")

        self.cursor.execute(
            "INSERT INTO User (login,password,fio,role) VALUES (?,?,?,?)",
            (self.entry_login_new_user_value_sql,  self.entry_password_new_user_value_sql,self.entry_fio_new_user_value_sql,self.entry_role_new_user_value_sql)
        )
        self.conn.commit()
if __name__ == "__main__":
    app = HelloWorld()




