import pytest
import psycopg2


@pytest.fixture(scope="function")
def db_connection():
    conn = psycopg2.connect(dbname='clothing_store', user='admin', password='admin')
    yield conn
    conn.close()


@pytest.fixture(scope="function")
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()


def test_order_present(db_cursor):
    db_cursor.execute("""
        SELECT COUNT(*) FROM orders
        WHERE order_date = '2024-04-11'
          AND client_id = 3
          AND item_type_id = 4
          AND items_in_order = 2;
    """)
    result = db_cursor.fetchone()[0]
    if result > 0:
        assert True, "В таблице orders есть записи с указанными значениями для всех обязательных полей."
    else:
        assert False, "В таблице orders отсутствуют записи или не все обязательные поля заполнены."


def test_order_deleted(db_cursor):
    db_cursor.execute("""
        INSERT INTO orders 
        (order_date, client_id, item_type_id, items_in_order)
        VALUES
        ('2024-04-10', 2, 2, 5);
        """)
    db_cursor.execute("""
    DELETE FROM orders
    WHERE order_date = '2024-04-10'
      AND client_id = 2
      AND item_type_id = 2
      AND items_in_order = 5;
    """)
    db_cursor.execute("""
    SELECT *
    FROM orders
    WHERE order_date = '2024-04-10'
      AND client_id = 2
      AND item_type_id = 2
      AND items_in_order = 5;
    """)
    result = db_cursor.fetchall()
    assert not result, "Данных больше нет."
