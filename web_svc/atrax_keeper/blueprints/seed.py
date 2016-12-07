import os
import tempfile
from flask import request, Blueprint
from atrax.management.crawl_job_controller import CrawlJobController


seed_api = Blueprint('seed_api', __name__)

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@seed_api.route('/seed', methods=['GET', 'POST'])
def seed():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            dest_dir_path = os.path.join(tempfile.gettempdir(), request.form['job'])
            if not os.path.exists(dest_dir_path):
                os.makedirs(dest_dir_path)
            seeds_path = os.path.join(dest_dir_path, filename)
            file.save(seeds_path)
            job = CrawlJobController(request.form['job'])
            job.seed(file_path=seeds_path)
            return '''
            <!doctype html>
            <title>Seed Crawler - Succeeded</title>
            <h1>Seed Crawler Succeeded</h1>
            <a href="/seed">Return</a>
            '''
    return '''
    <!doctype html>
    <title>Seed Crawler</title>
    <h1>Seed Crawler</h1>
    <form action="" method=post enctype=multipart/form-data>
      <span>Job Name</>
      <input type=text name=job><br />
      <input type=file name=file><br />
      <input type=submit value=Upload>
    </form>
    '''
