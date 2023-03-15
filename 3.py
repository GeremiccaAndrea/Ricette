from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # L'utente richiede l'home page
def home():
  return render_template("ricette3.html")

@app.route('/pizza') # L'utente richiede l'home page
def pizza():
  return render_template("ricettaPizza.html")

@app.route('/cotoletta') # L'utente richiede l'home page
def cotoletta():
  return render_template("ricettaCotoletta.html")

@app.route('/lasagna') # L'utente richiede l'home page
def lasagna():
  return render_template("ricettaLasagna.html")

@app.route('/pastiera') # L'utente richiede l'home page
def pastiera():
  return render_template("ricettaPastiera.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)