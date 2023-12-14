from flask import Flask, request, jsonify
from validation import validate_password, password_strength_score
from generation import generate_password

app = Flask(__name__)

@app.route('/validate_password', methods=['POST'])
def validate_password_endpoint():
    data = request.get_json()
    password = data.get('password', '')
    score, message = validate_password(password)
    strength = password_strength_score(score)
    return jsonify({'strength': strength, 'message': message})

@app.route('/generate_password', methods=['GET'])
def generate_password_endpoint():
    password = generate_password()
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
