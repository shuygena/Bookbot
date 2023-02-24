from typing import Tuple

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict = {}


def _get_part_text(text: str, start: int, size: int) -> Tuple:
    chrs: str = ',.!:;?'
    pg_size: int = size
    if len(text) <= size + start:
        pg_size = len(text) - start
    else:
        for i in range(size+start-1, start, -1):
            if text[i] in chrs and text[i + 1] not in chrs:
                break
            pg_size -= 1
    return [text[start: start + pg_size], pg_size]


def prepare_book(path: str) -> None:
    f = open(path, 'r')
    text: str = f.read()
    start: int = 0
    end: int = len(text)
    i: int = 1
    while (start < end):
        pg, delta = _get_part_text(text, start, PAGE_SIZE)
        start += delta
        book[i] = pg.lstrip(' \n\t')
        i += 1


prepare_book(BOOK_PATH)
