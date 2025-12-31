

from flask import Flask, jsonify

# Create the Flask app
app = Flask(__name__)

# Define an API route
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, this is my first API!"})
@app.route('/welcome',methods=['GET'])
def welcome():
    return jsonify({"message":"hello,this is my second API!"}) 

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    
