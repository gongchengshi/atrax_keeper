from flask import Flask

from atrax_keeper.constants import PACKAGE_REPO_BASE_DIR, CONFIG_REPO_BASE_DIR
from atrax_keeper.blueprints.upload_config import upload_config_api
from atrax_keeper.blueprints.upload_package_file import upload_package_file_api
from atrax_keeper.blueprints.seed import seed_api


app = Flask(__name__)
app.config['PACKAGE_REPO_BASE_DIR'] = PACKAGE_REPO_BASE_DIR
app.config['CONFIG_REPO_BASE_DIR'] = CONFIG_REPO_BASE_DIR


app.register_blueprint(upload_package_file_api)
app.register_blueprint(upload_config_api)
app.register_blueprint(seed_api)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <title>Atrax Commander Web Service</title>
    <a href="/upload_package_file">Upload Package File</a><br />
    <a href="/upload_config">Upload Crawl Job Configuration File</a><br />
    <a href="/seed">Seed Crawler</a>
    '''

import platform
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=True)
