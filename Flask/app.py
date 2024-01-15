from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    greeting = f"Привет, {name}!"
    return jsonify({'greeting': greeting})

if __name__ == '__main__':
    app.run(debug=True)
