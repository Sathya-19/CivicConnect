from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample data
states = [
    {"code": "CA", "name": "California"},
    {"code": "TX", "name": "Texas"},
    {"code": "NY", "name": "New York"}
]

registration_info = {
    "CA": {"state": "California", "details": "Register online or at your local DMV."},
    "TX": {"state": "Texas", "details": "Register in person at your county's voter office."},
    "NY": {"state": "New York", "details": "Mail your application or register online."}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-states')
def get_states():
    return jsonify(states)

@app.route('/get-registration-info/<state_code>')
def get_registration_info(state_code):
    return jsonify(registration_info.get(state_code, {"state": "Unknown", "details": "No information available."}))

if __name__ == '__main__':
    app.run(debug=True)
