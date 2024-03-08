from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def chatbot():
    return render_template('TIX.html')

if __name__ == '__main__':
    app.run(debug=False, port='0.0.0.0')