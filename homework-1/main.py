"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


def get_data_from_csv(file_path) -> list:
    """Функция для получения из файла csv списка с данными."""
    data_list = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            data_list.append(tuple(line))

    return data_list[1:]


with psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='5462') as conn:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO customers_data VALUES (%s, %s, %s)',
                        get_data_from_csv('north_data/customers_data.csv'))

        cur.executemany('INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)',
                        get_data_from_csv('north_data/employees_data.csv'))

        cur.executemany('INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)',
                        get_data_from_csv('north_data/orders_data.csv'))

conn.close()
