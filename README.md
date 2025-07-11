# Employee Reports Generator

Скрипт для генерации отчётов по сотрудникам из CSV-файлов.

## 📌 Быстрый старт

### Установка
1. Клонируйте репозиторий:
   ```bash
   https://github.com/Said-Ahmed/salary_report_ts.git
   cd salary_report_ts
    ```
###
2. Запуск тестов
    ```bash
   pytest
   ```
3. Запуск скрипта Mac
    ```bash
   python3 main.py data1.csv data2.csv data3.csv --report payout
   ```
4. Запуск скрипта Windows
    ```bash
   python main.py data1.csv data2.csv data3.csv --report payout
   ```
   
### Инструкция по добавлению нового отчета
Для того чтобы добавить новый отчет необходимо создать класс для
нового отчета, который наследуется от абстрактного класса BaseReport
и реализовать у него метод generate. 

    from reports.base_report import BaseReport
    
    class NewReport(BaseReport):
        def generate(self):
            # Ваша логика генерации отчёта
            return formatted_data

У класса BaseReport уже есть атрибут
self.employers, который содержит информацию о сотрудниках в виде списка
из словарей. После того как мы создали новый класс его необходимо зарегистрировать
в reports/\_\_init__.py

    from .new_report import NewReport
    
    REPORTS = {
        'payout': PayoutReport,
        'new_report': NewReport  # Новый отчёт
    }

теперь можно вызывать

    python main.py data.csv --report new_report