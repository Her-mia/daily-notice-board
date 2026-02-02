from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>我的看板环境搭建成功！</h1>"

if __name__ == '__main__':
    # debug=True 允许你修改代码保存后，网页自动刷新
    app.run(debug=True, port=5000)
