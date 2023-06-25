import os
import shutil
import zipfile
from os.path import join, abspath, dirname

resources_path = abspath(
    join(dirname(__file__), './resources/')
)


def test_zip(tmp_dir_manager):
    resources_zip_path = abspath(
        join(tmp_dir_manager, 'resources')
    )

    shutil.make_archive(
        resources_zip_path,
        'zip',
        root_dir=resources_path,
    )

    zip_path = join(tmp_dir_manager, 'resources.zip')

    with zipfile.ZipFile(zip_path, mode="r") as archive:
        for fileinfo in archive.infolist():
            original_file = abspath(
                join(resources_path, fileinfo.filename)
            )
            original_file_size = os.stat(original_file).st_size
            zipped_file_size = fileinfo.file_size

            assert original_file_size == zipped_file_size




