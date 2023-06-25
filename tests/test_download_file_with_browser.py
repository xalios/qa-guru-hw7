from selene import browser
from time import sleep
from os.path import exists, join


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp
def test_pytest_download_browser(tmp_dir_manager):
    downloading_filename = 'pytest-main.zip'

    assert not exists(join(tmp_dir_manager, downloading_filename))

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    # TODO переписать на проверку есть ли файл в дериктории
    sleep(5)

    assert exists(join(tmp_dir_manager, downloading_filename))







