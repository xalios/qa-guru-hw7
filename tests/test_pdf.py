from pypdf import PdfReader
from os.path import join, abspath, dirname

pdf_path = abspath(
    join(dirname(__file__), './resources/docs-pytest-org-en-latest.pdf')
)


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_pdf():
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    assert number_of_pages == 412

    page = reader.pages[0]
    assert 'pytest Documentation' in page.extract_text()
