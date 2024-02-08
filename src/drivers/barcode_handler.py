# Use a linter and code formatter (e.g., autopep8) to improve code quality and consistency.

from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        path_from_tag = f'{tag}'.encode('utf-8')
        tag.save(path_from_tag)

        return path_from_tag
