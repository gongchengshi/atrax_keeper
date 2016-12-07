import os

from flask import current_app, request, Blueprint


upload_config_api = Blueprint('upload_config_api', __name__)

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'job', 'scope'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@upload_config_api.route('/upload_config', methods=['GET', 'POST'])
def upload_config():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            dest_dir_path = os.path.join(current_app.config['CONFIG_REPO_BASE_DIR'], request.form['job'])
            if not os.path.exists(dest_dir_path):
                os.makedirs(dest_dir_path)
            file.save(os.path.join(dest_dir_path, filename))
            return '''
            <!doctype html>
            <title>Upload Crawl Job Configuration - Succeeded</title>
            <h1>Upload Configuration Succeeded</h1>
            <a href="/upload_config">Return</a>
            '''
    return '''
    <!doctype html>
    <title>Upload Crawl Job Configuration</title>
    <h1>Upload Configuration</h1>
    <form action="" method=post enctype=multipart/form-data>
      <span>Job Name</>
      <input type=text name=job><br />
      <input type=file name=file><br />
      <input type=submit value=Upload>
    </form>
    '''
