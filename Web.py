# request フォームから送信した情報を扱うためのモジュール
from flask import Flask, render_template, request
import cv2
# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = 'imageprocessing/input'

app = Flask(__name__)
@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/upload', methods=['POST'])#アップロード
def Upload():
    if request.method == 'POST':
        img_file = request.files['img_file']
    return render_template('Home.html')

@app.route('/eturan')
def Eturan():
    return render_template('Eturan.html')

@app.route('/grayscale')
def Grayscale():
    #この中に処理された画像を取得する処理を書く
    return render_template('Grayscale.html')

@app.route('/rinkaku')
def Rinkaku():
    #この中に処理された画像を取得する処理を書く
    return render_template('Rinkaku.html')

@app.route('/waku')
def Waku():
    #この中に処理された画像を取得する処理を書く
    return render_template('Waku.html')

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)

