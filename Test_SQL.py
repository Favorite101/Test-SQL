import mysql.connector
from mysql.connector import Error
import sqlite3

x = int(input("как подключаем базу данных? (1 - через сервер, 2 - через файл): "))
if x == 1:
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=input("Пароль: "),
        )
        y = int(input("Напишите цифру соотвествующую вашему запросу: 1 - SELECT, 2 - CREATE, 3 - UPDATE, 4 - INSERT, "
                      "5 - DROP: "))

        if y == 5:
            try:
                first_cursor = conn.cursor()
                sql_delete_query = input("Введите запрос: ")
                first_cursor.execute(sql_delete_query)
                conn.commit()
                print("Запись успешно удалена")
                first_cursor.close()
            except Error as e:
                print("Ошибка при работе с Mysql", e)
            finally:
                if conn:
                    conn.close()
                    print("Соединение с Mysql закрыто")

        if y == 4:
            try:
                first_cursor = conn.cursor()
                sqlite_insert_query = input("Введите запрос: ")
                count = first_cursor.execute(sqlite_insert_query)
                conn.commit()
                print("Запись успешно вставлена в таблицу", first_cursor.rowcount)
                conn.cursor().close()
            except Error as e:
                print("Ошибка при работе с Mysql", e)
            finally:
                if conn:
                    conn.close()
                    print("Соединение с Mysql закрыто")

        if y == 3:
            try:
                first_cursor = conn.cursor()
                sql_update_query = input("Введите запрос: ")
                first_cursor.execute(sql_update_query)
                conn.commit()
                print("Запись успешно обновлена")
                first_cursor.close()
            except Error as e:
                print("Ошибка при работе с Mysql", e)
            finally:
                if conn:
                    conn.close()
                    print("Соединение с Mysql закрыто")

        if y == 2:
            try:
                first_cursor = conn.cursor()
                first_cursor.execute(input("Введите запрос: "))
                print("База данных успешно была создана")
            except Error as e:
                print("Ошибка при работе с Mysql", e)
            finally:
                if conn:
                    conn.close()
                    print("Соединение с Mysql закрыто")

        if y == 1:
            try:
                first_cursor = conn.cursor()
                first_cursor.execute(input("Введите запрос: "))
                print(first_cursor.fetchall())
            except Error as e:
                print("Ошибка при работе с Mysql", e)
            finally:
                if conn:
                    conn.close()
                    print("Соединение с Mysql закрыто")

    except Error as e:
        print(e)

elif x == 2:

    con = input("введите название и формат файла, с базой данных: ")
    conn = sqlite3.connect(con)
    y = int(input("Напишите цифру соотвествующую вашему запросу: 1 - SELECT, 2 - CREATE, 3 - UPDATE, 4 - INSERT, "
                  "5 - DROP: "))

    if y == 5:
        try:
            second_cursor = conn.cursor()
            sql_delete_query = input("Введите запрос: ")
            second_cursor.execute(sql_delete_query)
            conn.commit()
            print("Запись успешно удалена")
            second_cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if conn:
                conn.close()
                print("Соединение с SQLite закрыто")

    if y == 4:
        try:
            second_cursor = conn.cursor()
            sqlite_insert_query = input("Введите запрос: ")
            count = second_cursor.execute(sqlite_insert_query)
            conn.commit()
            print("Запись успешно вставлена в таблицу", second_cursor.rowcount)
            conn.cursor().close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if conn:
                conn.close()
                print("Соединение с SQLite закрыто")

    if y == 3:
        try:
            second_cursor = conn.cursor()
            sql_update_query = input("Введите запрос: ")
            second_cursor.execute(sql_update_query)
            conn.commit()
            print("Запись успешно обновлена")
            second_cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if conn:
                conn.close()
                print("Соединение с SQLite закрыто")

    if y == 2:
        try:
            second_cursor = conn.cursor()
            second_cursor.execute(input("Введите запрос: "))
            print("База данных успешно была создана")
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if conn:
                conn.close()
                print("Соединение с SQLite закрыто")

    if y == 1:
        try:
            second_cursor = conn.cursor()
            second_cursor.execute(input("Введите запрос: "))
            print(second_cursor.fetchall())
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if conn:
                conn.close()
                print("Соединение с SQLite закрыто")

