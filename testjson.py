from flask import Flask, render_template
import os, json

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():

    jsonData = os.path.join( "static/", "info.json")
    data = json.load(open(jsonData))
    return render_template('base.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
