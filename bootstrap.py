from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('render_template.html')

app.run(port=800, debug=True)