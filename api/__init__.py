#這是package(資料夾)裡面的主程式
# from . import index #從根目錄import index進來

from flask import Blueprint,render_template

#所有和api有關的都寫在這，不能用api要用api1是因為api是關鍵字
api1 = Blueprint("api",__name__,url_prefix="/api") # template_folder="templates",static_folder='static'



#先有api1再import youbike裡面的/youbike的程式
from . import youbike,error,stockCode

@api1.route("/")
def api():
    return render_template('api.html')

