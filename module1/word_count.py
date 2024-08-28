"""Read file from web and do analysis of data
"""

from urllib.request import urlopen


def count_words_from_web_file(url_address):
    """Reads file from the passed in url_address

    Args:
        url_address (string): The url of the file the user wants to read

    Returns:
        int: The total number of the words from the url file
    """
    words = 0
    with urlopen(url_address) as data: # reads the file from the url
        for line in data:
            # print(line, type(line))
            line = line.decode('utf-8') # convert bytes to string
            line_words = line.split()
            for word in line_words: # counts the number of words in a line
                words += 1

    return words


def main():
    """Driven Function
    """
    file_address = 'http://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    total_words = count_words_from_web_file(file_address)
    print(f'There are a total of {total_words} in the file')


if __name__ == "__main__":
    main()