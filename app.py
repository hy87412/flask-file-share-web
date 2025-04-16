from flask import Flask, request, redirect

from flask import Flask, request
import os
import shutil
import random

app = Flask(__name__)
filenamelist = []
filecodelist = []

upload_folder = 'uploadsfile'
app.config['upload_folder'] = upload_folder

def booting():
    if os.path.exists(upload_folder):
        shutil.rmtree(upload_folder)
    os.makedirs(upload_folder, exist_ok=True)
    print("reset upload_folder")

def generatecode():
    while True:
        outputcode = random.randint(100000, 999999)
        if not(outputcode in filecodelist):
            return outputcode




booting()
print(generatecode())

@app.route('/upload', method=['POST'])
def uploadfile():
    if 'file' not in request.files:
        return "not file", 400
    file = request.files['files']
    if file.filename == '':
        return "not file name", 400
    filepath = os.path.join(app.config['upload_folder'], file.filename)
    file.save(filepath)
    return redirect('/')