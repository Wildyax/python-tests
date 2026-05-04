import sqlite3
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Initialize database and create table if it doesn't exist
conn = sqlite3.connect('items.db')  # this will create 'items.db' if it doesn't exist
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
# Insert some sample data if the table is empty
cursor.execute("SELECT COUNT(*) FROM items")
count = cursor.fetchone()[0]
if count == 0:
    cursor.execute("INSERT INTO items (name) VALUES ('Sample Item 1')")
    cursor.execute("INSERT INTO items (name) VALUES ('Sample Item 2')")
    cursor.execute("INSERT INTO items (name) VALUES ('Sample Item 3')")
    cursor.execute("INSERT INTO items (name) VALUES ('Sample Item 4')")
    conn.commit()
conn.close()

# Define the GET /items endpoint
@app.route('/items', methods=['GET'])
def get_items():
    # Connect to the database and fetch all items in it
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM items")
    rows = cursor.fetchall()
    conn.close()
    # Convert the query result into a list of dictionaries
    items = []
    for row in rows:
        items.append({"id": row[0], "name": row[1]})
    # Return the list of items as JSON
    return jsonify(items)

# Run the app on local development server
if __name__ == '__main__':
    app.run(debug=True)
