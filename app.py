from flask import Flask, render_template, redirect, url_for, session
import ticket_info
import process

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/")
def generate():
    return render_template('GENERATE.html')

@app.route('/generate_ticket', methods=['GET', 'POST'])
def generate_ticket():
    ticket_info_arr = ticket_info.scrape()
    processed_ticket_info_arr = process.main(ticket_info_arr)  # Process the ticket info array
    session['ticket_info_arr'] = processed_ticket_info_arr  # Store the array in session
    return redirect(url_for('show_ticket'))

@app.route('/show_ticket')
def show_ticket():
    info_arr = session.get('ticket_info_arr')  # Retrieve the array from session
    if not info_arr:
        return "Ticket info not found in session"  # Handle if session data is missing
    
    print(info_arr[0])
    return render_template('TIX.html', info_arr=info_arr)

if __name__ == '__main__':
    app.debug = True
    app.run()