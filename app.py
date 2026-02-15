from flask import Flask, render_template
from weather import get_day_night_single_code
from countdown import countdown


app = Flask(__name__)

@app.route('/')
def home():
    data={"weather":get_day_night_single_code(30.58333, 114.26667, "Asia/Shanghai"),
          "countdown": countdown,
          "timer":"tomato"
    }
    return render_template("index.html", data=data)

if __name__ == '__main__':
    # debug=True 允许你修改代码保存后，网页自动刷新
    app.run(host='0.0.0.0', port=5000, debug=True)
