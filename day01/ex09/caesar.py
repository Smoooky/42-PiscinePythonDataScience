#!/usr/bin/python3
import sys


def get_type(type_raw: str) -> bool:
    if type_raw == 'encode':
        return True
    elif type_raw == 'decode':
        return False
    else:
        raise RuntimeError("First argument must be \"decode\" or \"encode\"")


def get_offset(raw_offset: str) -> int:
    try:
        return int(raw_offset)
    except ValueError:
        print("Third argument must be integer")
        return None


def get_new_char(char: str, offset: int, is_encode: bool) -> str:
    alphabet = tuple(map(chr, range(97, 123)))
    if char in alphabet:
        if is_encode:
            return alphabet[(alphabet.index(char) + int(offset)) % 26]
        else:
            return alphabet[(alphabet.index(char) - int(offset)) % 26]
    return char


def encode(text: str, offset: int, is_encode: bool) -> str:
    res = ''
    for i in text:
        if ord(i) >= 128:
            raise RuntimeError("The script does not support your language yet.")
        if i.isupper():
            res += get_new_char(i.lower(), int(offset), is_encode).upper()
        else:
            res += get_new_char(i, int(offset), is_encode)
    print(res)


def main():
    if len(sys.argv) == 4:
        offset = get_offset(sys.argv[3])
        if offset is not None:
            encode(sys.argv[2], offset, get_type(sys.argv[1]))


if __name__ == '__main__':
    main()
