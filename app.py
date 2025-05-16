from flask import Flask, jsonify
import time

app = Flask(__name__)

count = 0

@app.route('/time')
def get_time():
    """
    Обработчик для маршрута /time
    Возвращает текущее время в формате Unix timestamp
    """
    global count
    count += 1
    return jsonify({"time": int(time.time())})

@app.route('/metrics')
def get_count():
    global count
    return jsonify({"count": count})

if __name__ == '__main__':
    # Запускаем сервер на порту 3030 на всех интерфейсах
    app.run(host='0.0.0.0', port=3030)
