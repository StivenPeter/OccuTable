from flask import Flask, render_template
import Occupations
Occupations.OccPrep()
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello' 

@app.route('/chooser')
def JobChooser():
    randJob = Occupations.randOcc()
    return render_template('main.html', RandJob = randJob, occDict = Occupations.occDict)

if __name__ == '__main__':
    app.debug = True
    app.run()
