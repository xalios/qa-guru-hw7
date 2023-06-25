import requests
from os.path import exists, join, getsize


# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
def test_download_by_requests(tmp_dir_manager):
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    downloading_filename = 'selenium_logo.png'

    path_to_file = join(tmp_dir_manager, downloading_filename)
    assert not exists(path_to_file)

    response = requests.get(url)
    assert response.status_code == 200

    with open(path_to_file, 'wb') as file:
        file.write(response.content)
    assert exists(path_to_file)

    size = getsize(path_to_file)
    assert size == 30803

