from flask import Flask, jsonify
import os

app = Flask(__name__)
COUNTER_FILE = "visits.txt"

def read_count():
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'w') as f:
            f.write("0")
    with open(COUNTER_FILE, 'r') as f:
        return int(f.read())

def write_count(count):
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(count))

@app.route('/visits')
def visits():
    count = read_count() + 1
    write_count(count)
    return jsonify({"visits": count})

if __name__ == '__main__':
    app.run()
