import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import os

# Имя файла для хранения дат
DATE_FILE = "books_date.json"

def save_current_date():
    # Получаем текущую дату и время
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Сохраняем дату в словарь
    data = {"current_date": current_date}
    
    # Записываем данные в файл JSON
    with open(DATE_FILE, "w") as file:
        json.dump(data, file)
    
    # Показываем сообщение об успешном сохранении
    messagebox.showinfo("Информация", f"Текущая дата сохранена: {current_date}")

# Создаем основное окно приложения
root = tk.Tk()
root.title("Пример Tkinter")

# Кнопка для сохранения даты
button = ttk.Button(root, text="Сохранить текущую дату", command=save_current_date)
button.pack(pady=20)
