from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def index():
    info = {
        "version":"Flask App v1.0",
        "python":"Python 3.12.13",
        "status":"服务运行正常",
        "name":"张蕴仪",
        "studentId":"2440664338",
        "update_time":time.strftime("%Y-%m-%d %H:%M:%S"),
        "env":"Development"
    }
    html = f"""
    <html>
    <body style="background:#4267cb">
        <div style="width:400px;margin:150px auto;background:white;padding:30px;border-radius:12px;text-align:center">
            <h3>🚀CI/CD部署成功！</h3>
            <p>{info['version']}</p >
            <p>{info['python']}</p >
            <p>✅{info['status']}</p >
            <hr>
            <p>姓名：{info['name']}</p >
            <p>学号：{info['studentId']}</p >
            <p>部署时间：{info['update_time']}</p >
            <p>环境：{info['env']}</p >
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)