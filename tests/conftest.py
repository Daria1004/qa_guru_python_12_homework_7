import zipfile
import os
import pytest
import shutil

from paths import RESOURCE_DIR, TEMP_DIR

@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists(RESOURCE_DIR):
        os.mkdir(RESOURCE_DIR)
    with zipfile.ZipFile(os.path.join(RESOURCE_DIR, 'files.zip'),'w') as zf:
        for file in os.listdir(TEMP_DIR):
            add_file = os.path.join(TEMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    yield
    shutil.rmtree(RESOURCE_DIR)
