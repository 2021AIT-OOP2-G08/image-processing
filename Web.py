# request フォームから送信した情報を扱うためのモジュール
from flask import Flask, render_template, request, redirect, url_for

# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = 'imageprocessing/input'
# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png'])


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
#アップロード
def Home():
    if request.method == 'POST':
        img_file = request.files['img_file']
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

