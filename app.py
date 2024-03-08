from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def chatbot():
    #return html 
    return render_template('TIX.html')