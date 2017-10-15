from flask import Flask, url_for, render_template, request
import os #Manipulates files
from PIL import Image

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    #viewImages = os.listdir('static/images/')
    return render_template("base.html")

@app.route("/uploaded", methods=['POST','GET'])
def uploaded():

    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/images/upload.gif')
        return "File Uploaded"
    else:
        page='''
        <html>
        <body>
        <form action="" method="POST" enctype="multipart/form-data">
            <input type="file" name="datafile" accept="image/gif">
            <input type="submit" value="send">
        </form>
        </body>
        </html>
        '''
        return page, 200

#Handles the error is user goes to link in our domain that doesnt exsist
@app.errorhandler(404)
def page_not_found(error):
    start = '<img src="'
    url = url_for ('static', filename ='ysnp.gif')
    end = '">'
    return "You Broke It You Idiot, Get Back Home!" + start+url+end, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
