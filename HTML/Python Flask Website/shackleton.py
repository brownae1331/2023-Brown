from flask import Flask, app, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/endurance')
def endurance():
    return render_template('endurance.html')

@app.route('/james_caird')
def james_caird():
    return render_template('james_caird.html')

if __name__ == '__main__':
    app.run(DEBUG = True)