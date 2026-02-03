from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data={"weather":"weather",
          "countdown":"coutdown",
          "timer":"tomato"
    }
    return render_template("index.html", data=data)

if __name__ == '__main__':
    # debug=True 允许你修改代码保存后，网页自动刷新
    app.run(host='0.0.0.0', port=5000, debug=True)
