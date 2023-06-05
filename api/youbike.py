from . import api1 #從根目錄import api1進來，用from就沒有交互import的問題


@api1.route("/youbike")
def youbike():
    return "<h1>Hello! Youbike</h1>"