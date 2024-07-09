from flask import Flask, render_template, request, redirect, url_for
import redis

app = Flask(__name__)

# Initialize Redis client
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        # Store data in Redis
        r.set('name', name)
        r.set('email', email)
        
        return redirect(url_for('success'))

@app.route('/success')
def success():
    # Retrieve data from Redis
    name = r.get('name').decode('utf-8')
    email = r.get('email').decode('utf-8')
    
    return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
