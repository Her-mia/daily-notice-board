from flask import Flask, render_template, request, jsonify, redirect
from weather import get_day_night_single_code
from datecountdown import calculate_days_left
from datetime import datetime, timedelta
import json
import os
import uuid

filename = "timer.json"
if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        timer = json.load(f)
else:
    timer = {}

app = Flask(__name__)
target_time = None


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # 读取 timer.json
    try:
        with open("timer.json", "r", encoding="utf-8") as f:
            saved_events = json.load(f)
    except:
        saved_events = {}

    # 在这里动态计算剩余天数
    events_with_days = {}
    for name, date_str in saved_events.items():
        days_left = calculate_days_left(date_str)
        events_with_days[name] = days_left

    # 传给模板
    data = {
        "weather": get_day_night_single_code(30.58333, 114.26667, "Asia/Shanghai"),
        "events": events_with_days
    }

    print("传给模板的 events =", events_with_days, type(events_with_days))

    return render_template("index.html", data=data)


events = []   # 每个元素是 {"name": ..., "days": ...}

@app.route("/set_date", methods=["POST"])
def set_date():
    name = request.form.get("event_name")
    date_str = request.form.get("target_date")

    # 读取旧数据
    try:
        with open("timer.json", "r", encoding="utf-8") as f:
            saved_events = json.load(f)
    except:
        saved_events = {}

    # 写入新事件（只存日期，不存 days）
    saved_events[name] = date_str

    # 保存到 JSON
    with open("timer.json", "w", encoding="utf-8") as f:
        json.dump(saved_events, f, ensure_ascii=False, indent=4)

    return redirect("/")

@app.route("/delete_event/<event_name>", methods=["POST"])
def delete_event(event_name):
    try:
        with open("timer.json", "r", encoding="utf-8") as f:
            saved_events = json.load(f)
    except:
        saved_events = {}

    # 删除对应事件
    if event_name in saved_events:
        del saved_events[event_name]

    # 保存回 JSON
    with open("timer.json", "w", encoding="utf-8") as f:
        json.dump(saved_events, f, ensure_ascii=False, indent=4)

    return redirect("/")

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

for i in events:
    timer[i["name"]] = i["days"]

print(timer)

with open("timer.json", "r", encoding="utf-8") as f:
    saved_events = json.load(f)   # 这是字典

if __name__ == '__main__':
    # debug=True 允许你修改代码保存后，网页自动刷新
    app.run(host='0.0.0.0', port=5000, debug=True) 



