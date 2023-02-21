from typing import Dict, Tuple

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict = {}


def _get_part_text(text: str, start: int, page_size: int) -> Tuple:
    ttext = text + ' '
    pos1 = ttext.rfind(' ', start, start + page_size + 1)
    pos2 = ttext.rfind('\n', start, start + page_size + 1)
    sub_text = ttext[start:max(pos1, pos2)]
    list_signs_positions = list()
    list_signs_positions.append(sub_text.rfind(","))
    list_signs_positions.append(sub_text.rfind("."))
    list_signs_positions.append(sub_text.rfind("!"))
    list_signs_positions.append(sub_text.rfind(":"))
    list_signs_positions.append(sub_text.rfind(";"))
    list_signs_positions.append(sub_text.rfind("?"))
    pos = max(list_signs_positions) + 1
    page = sub_text[:pos]
    return page, len(page)


def prepare_book(path: str) -> None:
    pass


prepare_book(BOOK_PATH)
