#!/usr/bin/python3

class Research:
    @staticmethod
    def file_reader():
        with open('data.csv', 'r', encoding='utf-8') as file:
            return file.read()


def main():
    researcher = Research()
    print(researcher.file_reader())


if __name__ == "__main__":
    main()
