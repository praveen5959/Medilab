import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.static_folder = 'static'
UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['file']
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('index.html')

    # if image and allowed_file(image.filename):
    #             filename = secure_filename(image.filename)
    #             image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         imagename = filename


if __name__ == '__main__':
    app.run(debug=True)
