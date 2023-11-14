from flask import Flask, render_template, jsonify
import get_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_message')
def get_message():
    # Call your Python function here and get the result
    message = get_data.planes()  # Replace with your actual function call
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
