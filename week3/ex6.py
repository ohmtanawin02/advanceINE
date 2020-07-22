from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=['POST']) #process อันนี้ไม่ใช่หน้า แต่เป็น process ที่ทำงานอยู่เบื้องหลัง
def process():
    name = request.form['name']
    comment = request.form['comment']

    return render_template('index.html', name=name, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)