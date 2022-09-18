#!/usr/bin/python3

def read_file(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def write_file(filename: str, lines: list) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def get_csv_string_value(csv_line: str, begin_pos: int, sep=',') -> str:
    if csv_line[begin_pos] != '"':
        raise ValueError("Can't get csv string value: the value is not a string")
    end_pos = csv_line.find('"', begin_pos + 1)
    while end_pos != -1:
        if (end_pos - begin_pos > 1) and (csv_line[end_pos - 1] == '\\'):  # escape quote
            end_pos = csv_line.find('"', end_pos + 1)  # find next
        else:
            break
    if end_pos == -1:
        raise RuntimeError("Syntax error: unclosed quote")
    end_pos += 1
    if (end_pos + 1 != len(csv_line)) and (csv_line[end_pos] != sep):
        raise RuntimeError("Syntax error: separator after quote is missing")
    return csv_line[begin_pos:end_pos]


def get_csv_any_value(csv_line: str, begin_pos: int, sep=',') -> str:
    end_pos = csv_line.find(sep, begin_pos + 1)
    if end_pos == -1:
        return csv_line[begin_pos:]
    return csv_line[begin_pos:end_pos]


def split_csv_line(csv_line: str, sep=',') -> list:
    splitted_line = []
    begin_pos = 0
    while begin_pos < len(csv_line):
        if csv_line[begin_pos] == sep:
            begin_pos += 1
        if csv_line[begin_pos] == '"':  # field is "string"
            value = get_csv_string_value(csv_line, begin_pos)
        else:
            value = get_csv_any_value(csv_line, begin_pos)
        splitted_line.append(value)
        begin_pos += len(value)
    return splitted_line


def join_scv_fields(fields: list, sep=',') -> str:
    return sep.join(fields)


def main():
    input_lines = read_file('ds.csv')
    output_lines = []

    for line in input_lines:
        output_lines.append(join_scv_fields(split_csv_line(line), '\t'))

    write_file("ds.tsv", output_lines)


if __name__ == '__main__':
    main()
