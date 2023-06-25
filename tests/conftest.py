import shutil

import pytest
from selenium import webdriver
from selene import browser
from os.path import join, abspath, dirname, exists, isfile, islink
from os import unlink, makedirs


def __remove_dir(path):
    if not exists(path):
        return
    if isfile(path) or islink(path):
        unlink(path)
    else:
        shutil.rmtree(path)

@pytest.fixture
def tmp_dir_manager(scope='function'):
    tmp_path = (
        abspath(join(dirname(__file__), './tmp/'))
    )
    if not exists(tmp_path):
        makedirs(tmp_path)
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": tmp_path,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    yield tmp_path

    __remove_dir(tmp_path)

