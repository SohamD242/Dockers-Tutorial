from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return redirect(url_for('success', name=name, email=email))

@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
