from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the game
@app.route('/game')
def game():
    return render_template('index.html')

@app.route('/canada')
def canada():
    return render_template('info/canada.html')

@app.route('/guyana')
def guyana():
    return render_template('info/guyana.html')

@app.route('/us')
def us():
    return render_template('info/us.html')

@app.route('/mexico')
def mexico():
    return render_template('info/mexico.html')

@app.route('/russia')
def russia():
    return render_template('info/russia.html')

@app.route('/greece')
def greece():
    return render_template('info/greece.html')

@app.route('/greenland')
def greenland():
    return render_template('info/greenland.html')

@app.route('/france')
def france():
    return render_template('info/france.html')

if __name__ == '__main__':
    app.run(debug=True)
