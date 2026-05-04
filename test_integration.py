import sqlite3
import tempfile
import os
import pytest


@pytest.fixture
def db_connection():
    """Crée une base SQLite temporaire pour chaque test."""
    db_fd, db_path = tempfile.mkstemp()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Créer la table
    cursor.execute("""
        CREATE TABLE items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)

    conn.commit()

    yield conn  # on fournit la connexion au test

    # Cleanup après le test
    conn.close()
    os.close(db_fd)
    os.unlink(db_path)


def test_insert_item(db_connection):
    """Tester qu'on peut insérer un item."""
    cursor = db_connection.cursor()

    cursor.execute("INSERT INTO items (name) VALUES (?)", ("Item A",))
    db_connection.commit()

    cursor.execute("SELECT name FROM items")
    result = cursor.fetchone()

    assert result[0] == "Item A"


# def test_multiple_items(db_connection):
#     """Tester l'insertion de plusieurs items."""
#     cursor = db_connection.cursor()

#     items = [("Item 1",), ("Item 2",), ("Item 3",)]
#     cursor.executemany("INSERT INTO items (name) VALUES (?)", items)
#     db_connection.commit()

#     cursor.execute("SELECT COUNT(*) FROM items")
#     count = cursor.fetchone()[0]

#     assert count == 3


# def test_item_structure(db_connection):
#     """Tester que les colonnes retournées sont correctes."""
#     cursor = db_connection.cursor()

#     cursor.execute("INSERT INTO items (name) VALUES (?)", ("Test Item",))
#     db_connection.commit()

#     cursor.execute("SELECT id, name FROM items")
#     row = cursor.fetchone()

#     assert isinstance(row[0], int)  # id
#     assert isinstance(row[1], str)  # name


# def test_empty_table(db_connection):
#     """Tester qu'une table vide retourne aucun résultat."""
#     cursor = db_connection.cursor()

#     cursor.execute("SELECT * FROM items")
#     rows = cursor.fetchall()

#     assert rows == []
