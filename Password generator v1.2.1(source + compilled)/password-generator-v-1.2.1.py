import random
import string
import tkinter as tk
import os

def generate_password():
    # Получаем значения из полей ввода
    password_length = int(password_length_entry.get())
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_punctuation = punctuation_var.get()

    # Составляем строку с символами, которые могут использоваться в пароле
    allowed_chars = ''
    if use_lowercase:
        allowed_chars += string.ascii_lowercase
    if use_uppercase:
        allowed_chars += string.ascii_uppercase
    if use_digits:
        allowed_chars += string.digits
    if use_punctuation:
        allowed_chars += string.punctuation

    # Проверяем, что были выбраны хотя бы один тип символов
    if not allowed_chars:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Ошибка: нужно выбрать хотя бы один тип символов")
        return

    # Генерируем пароль
    password = ''.join(random.choices(allowed_chars, k=password_length))

    # Выводим пароль на экран
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# Создаем окно
window = tk.Tk()
icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "icon.ico"))
window.iconbitmap(icon_path)
window.title("Pass Generator by Pushkin v1.2.1")

# Создаем метку для выбора длины пароля
password_length_label = tk.Label(window, text="Длина пароля:")
password_length_label.grid(column=0, row=0, sticky="W", padx=10, pady=10)

# Создаем поле для ввода длины пароля
password_length_entry = tk.Entry(window)
password_length_entry.insert(0, "12")
password_length_entry.grid(column=1, row=0, padx=10, pady=10)

# Создаем метку для выбора типов символов
password_chars_label = tk.Label(window, text="Типы символов:")
password_chars_label.grid(column=0, row=1, sticky="W", padx=10, pady=10)

# Создаем флажок для выбора символов в нижнем регистре
lowercase_var = tk.BooleanVar()
lowercase_var.set(True)
lowercase_checkbox = tk.Checkbutton(window, text="Буквы нижнего регистра", variable=lowercase_var)
lowercase_checkbox.grid(column=0, row=2, sticky="W", padx=10)

# Создаем флажок для выбора символов в верхнем регистре
uppercase_var = tk.BooleanVar()
uppercase_var.set(True)
uppercase_checkbox = tk.Checkbutton(window, text="Буквы верхнего регистра", variable=uppercase_var)
uppercase_checkbox.grid(column=0, row=3, sticky="W", padx=10)

# Создаем флажок для выбора цифр
digits_var = tk.BooleanVar()
digits_var.set(True)
digits_checkbox = tk.Checkbutton(window, text="Цифры", variable=digits_var)
digits_checkbox.grid(column=1, row=2, sticky="W", padx=10)

# Создаем флажок для выбора знаков препинания
punctuation_var = tk.BooleanVar()
punctuation_var.set(True)
punctuation_checkbox = tk.Checkbutton(window, text="Знаки препинания", variable=punctuation_var)
punctuation_checkbox.grid(column=1, row=3, sticky="W", padx=10)

# Создаем кнопку для генерации пароля
generate_button = tk.Button(window, text="Сгенерировать пароль", command=generate_password)
generate_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Создаем метку для вывода пароля
password_label = tk.Label(window, text="Сгенерированный пароль:")
password_label.grid(column=0, row=5, sticky="W", padx=10, pady=10)

# Создаем поле для вывода пароля
password_entry = tk.Entry(window)
password_entry.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

# Запускаем главный цикл обработки событий
window.mainloop()