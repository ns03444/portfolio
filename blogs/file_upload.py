import os
from flask import flash, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
from flask import current_app
UPLOAD_FOLDER = '/static/'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def add_file(filename):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.root_path + UPLOAD_FOLDER, filename))
            flash('Upload Completed!')


            return filename


# @app.route('/uploads/<name>')
# def download_file(name):
#     return send_from_directory(current_app.root_path + UPLOAD_FOLDER, name)

# @app.route('/uploads/')
# def open_file():
#     return render_template('uploads.html')

# if __name__ == '__main__':
#     app.run(debug=True)