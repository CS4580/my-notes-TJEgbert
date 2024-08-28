"""Read file from web and do analysis of data
"""

from urllib.request import urlopen


def count_words_from_web_file(url_address):
    words = 0
    # TODO: Read file from web
    with urlopen(url_address) as data:
        for line in data:
            print(line, type(line))
            line = line.decode('utf-8') # convert bytes to string
            line_words = line.split()
            for word in line_words:
                words += 1

    # TODO: Count number of words
    return words


def main():
    """Driven Function
    """
    file_address = 'http://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    total_words = count_words_from_web_file(file_address)
    print(f'There are a total of {total_words} in the file')


if __name__ == "__main__":
    main()