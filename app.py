## 執行指令：flask --app app run --debug (--debug有打才會更新) 其實打flask run就可以
## 執行指令：flask --A app run --debug
## .\venv\Scripts\activate.bat (忘記就打這個flask --help或flask run --help)

from flask import Flask
from api import api1


app = Flask(__name__)
app.register_blueprint(api1) #註冊


# @ => decrator後面接function
@app.route("/")
def index():
    return "<h1>Hello! Ash!</h1>"