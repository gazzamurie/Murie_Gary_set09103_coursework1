from flask import Flask, url_for, render_template
import os
from PIL import Image

app = Flask(__name__)

@app.route('/images/<filename>')
def send_image(filename):
    return send_images("static/static/", filename)

@app.route("/")
def home():
    viewImages = os.listdir('static/static/')
    print(viewImages)
    return render_template("base.html", viewImages=viewImages)


@app.errorhandler(404)
def page_not_found(error):
    start = '<img src="'
    url = url_for ('static', filename ='ysnp.gif')
    end = '">'
    return "You Broke It You Idiot, Get Back Home!" + start+url+end, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
