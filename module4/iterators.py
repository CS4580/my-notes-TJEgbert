"""My template module 
"""

def main():
    """Driven Function
    """
    iterable = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    # Create an iterator
    iterator = iter(iterable)
    # Get first element
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    # print(next(iterator)) creates an error since we are out of iterator

    # TODO: ADD a function with a try: catch: to test the iterator

    # TODO: Then use a Generator

if __name__ == "__main__":
    main()