from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
#アップロード
def Home():
    return render_template('Home.html')

@app.route('/Eturan')
#ホーム画面
def Eturan():
    return render_template('Eturan.html')

@app.route('/Eturan/Grayscale', methods=["POST"])
def Grayscale():
    #この中に処理された画像を取得する処理を書く
    return render_template('Grayscale.html')

@app.route('/Eturan/Rinkaku', methods=["POST"])
def Rinkaku():
    #この中に処理された画像を取得する処理を書く
    return render_template('Rinkaku.html')

@app.route('/Eturan/Waku', methods=["POST"])
def Waku():
    #この中に処理された画像を取得する処理を書く
    return render_template('Waku.html')
