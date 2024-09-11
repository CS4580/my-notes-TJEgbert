""" Download data from our server
"""
from io import BytesIO
import urllib.request as request
import zipfile as ZipFile


SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'

def download_file(url, file_name):
    #TODO: Download to pwd
    downloaded_file = request.urlretrieve(url, file_name)
    return downloaded_file

def unzip_file(file_name):
    # TODO: unzip file
    print(file_name)
    with ZipFile(file_name, 'r') as zObject:
        zObject.extractAll('.')
    
def main():
    """Driven Function
    """
    data = 'pandas01Data.zip'
    pdw = download_file(SERVER_URL, data)
    unzip_file(pdw)



if __name__ == "__main__":
    main()