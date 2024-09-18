""" Download data from our server
"""
from urllib.parse import urlparse
import urllib.request as request
import zipfile as ZipFile

SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'


def valid_url(url, file_name):
    """ Checks if the url is a valid url

    Args:
        url (str): The url of file to download
        file_name (str): The file name to download

    Returns:
        bool: Returns True if the url is valid
              Returns False is the url is not valid
    """
    try:
        urlparse(url + file_name)
        return True
    except ValueError:
        return False
  

def download_file(url, file_name):
    """ Downloads the file from the passed in arguments

    Args:
        url (str): The url of file to download
        file_name (str): The file name to download
    """
    #TODO: Download to pwd
    if valid_url(url, file_name):
        whole_path = url +  file_name
        request.urlretrieve(whole_path, file_name)
        # add a check to make it downloaded correctly
        unzip_file(file_name)
    else:
        print("URL is invalid")


def unzip_file(file_name):
    """ Unzips the passed in file name

    Args:
        file_name (str): Name of file to be unzipped 
    """
    # TODO: unzip file
    with ZipFile.ZipFile(file_name, 'r') as zObject:
        zObject.extractall('.')
    

#TODO: Create a function to download the files
# from Kaggle directly by passing the data set

#TODO: do error checking and display information 

def main():
    """Driven Function
    """
    #data = 'pandas02Data.zip'
    #download_file(SERVER_URL, data)
    unzip_file('hotel-booking-demand.zip')


if __name__ == "__main__":
    main()