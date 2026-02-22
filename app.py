from flask import Flask, render_template, request, jsonify
from weather import get_day_night_single_code
from datecountdown import datecountdown
from datetime import datetime, timedelta


app = Flask(__name__)
target_time = None

@app.route('/')
def home():
    data={"weather":get_day_night_single_code(30.58333, 114.26667, "Asia/Shanghai"),
          "date": datecountdown,
    }
    return render_template("index.html", data=data)

@app.route("/get_time")
def get_time():
    global target_time
    if target_time is None:
        return jsonify({"target": None})
    return jsonify({"target": target_time.isoformat()})

@app.route("/set_countdown", methods=["POST"])
def set_countdown():
    global target_time
    minutes = request.json.get("minutes")

    if not (1 <= minutes <= 180):
        return jsonify({"status": "error", "msg": "倒计时必须在 1 到 180 分钟之间"}), 400

    target_time = datetime.now() + timedelta(minutes=minutes)
    return jsonify({"status": "ok", "target": target_time.isoformat()})



if __name__ == '__main__':
    # debug=True 允许你修改代码保存后，网页自动刷新
    app.run(host='0.0.0.0', port=5000, debug=True)


