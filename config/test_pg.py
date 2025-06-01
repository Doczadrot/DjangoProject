import psycopg2

try:
    conn = psycopg2.connect(
        dbname="django_project",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    print("Подключение успешно!")
    conn.close()
except Exception as e:
    print(f"Ошибка: {e}")