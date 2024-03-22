from flask import Flask, render_template, redirect, url_for
import ticket_info

app = Flask(__name__)

@app.route("/")
def ticket():
    # return html
    return render_template('GENERATE.html')

@app.route('/generate_ticket', methods=['GET', 'POST'])
def generate_ticket():
    # Put your ticket generation logic here
    # For demonstration purposes, let's just return a message
    # Redirect to TIX.html after generating the ticket
    return redirect(url_for('show_ticket'))

@app.route('/show_ticket')
def show_ticket():
    # Render TIX.html with ticket information
    info_arr = ticket_info.main()
    return render_template('TIX.html', info_arr=info_arr)

if __name__ == '__main__':
    app.run(debug=True)