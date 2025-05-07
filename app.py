from flask import Flask, request, redirect, send_file, render_template
import os
import shutil
import random

app = Flask(__name__)
filedb = {}

upload_folder = 'uploadsfile'
app.config['upload_folder'] = upload_folder

# 초기화
def booting():
    if os.path.exists(upload_folder):
        shutil.rmtree(upload_folder)
    os.makedirs(upload_folder, exist_ok=True)
    print("reset upload_folder")

# 코드 생성
def generatecode():
    while True:
        code = str(random.randint(1000, 9999))
        if code not in filedb:
            return code

booting()

# 메인 페이지
@app.route('/')
def index():
    code = generatecode()
    return render_template('index.html', code=code)

# 파일 업로드
@app.route('/upload/<code>', methods=['POST'])
def uploadfile(code):
    if 'file' not in request.files:
        return "파일이 없습니다.", 400
    file = request.files['file']
    if file.filename == '':
        return "파일 이름이 없습니다.", 400

    save_path = os.path.join(app.config['upload_folder'], f"{code}_{file.filename}")
    file.save(save_path)
    filedb[code] = save_path
    return render_template('upload_success.html', code=code)

# 파일 다운로드
@app.route('/download/<code>')
def downloadfile(code):
    if code in filedb:
        return send_file(filedb[code], as_attachment=True)
    else:
        return render_template('download_not_found.html'), 404


if __name__ == "__main__" :
    app.run(debug=False, host='0.0.0.0')