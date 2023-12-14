# Используем базовый образ Python
FROM python:3.8

# Устанавливаем рабочую директорию
WORKDIR /calc

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы в рабочую директорию
COPY . .

# Открываем порт 5000
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "api-calc.py"]
