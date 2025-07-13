from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_BASE_URL = 'https://sirekap-obj-data.kpu.go.id/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nik = request.form['nik']
        try:
            response = requests.get(f"{API_BASE_URL}api/nik/{nik}")
            if response.status_code == 200:
                data = response.json()
                return render_template('index.html', data=data, nik=nik)
            else:
                return render_template('index.html', error="Data tidak ditemukan!", nik=nik)
        except Exception as e:
            return render_template('index.html', error=str(e), nik=nik)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
