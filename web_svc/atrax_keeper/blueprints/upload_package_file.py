import os

from flask import current_app, request, Blueprint


upload_package_file_api = Blueprint('upload_package_file_api', __name__)

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'tar', 'sh'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@upload_package_file_api.route('/upload_package_file', methods=['GET', 'POST'])
def upload_package_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            dest_dir_path = os.path.join(current_app.config['PACKAGE_REPO_BASE_DIR'], request.form['package_name'])
            if not os.path.exists(dest_dir_path):
                os.makedirs(dest_dir_path)
            file.save(os.path.join(dest_dir_path, filename))
            return '''
            <!doctype html>
            <title>Upload Package File - Succeeded</title>
            <h1>Upload Package File Succeeded</h1>
            <a href="/upload_package_file">Return</a>
            '''
    return '''
    <!doctype html>
    <title>Upload Package File</title>
    <h1>Upload Package File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <input type="radio" name="package_name" value="keeper">Keeper<br />
      <input type="radio" name="package_name" value="frontier">Frontier<br />
      <input type="radio" name="package_name" value="fetcher">Fetcher<br />
      <input type="radio" name="package_name" value="redis">Redis<br />
      <input type="radio" name="package_name" value="velum">Velum<br />
      <input type=file name=file><br />
      <input type=submit value=Upload>
    </form>
    '''
