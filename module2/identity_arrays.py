"""Practice some of numpy array identities
"""
import numpy as np

def main():
    """Driven Function
    """
    # Create a 2D 3x3 identity matrix
    identity_3x3 = np.eye(3, 3)
    print(identity_3x3)

    # Create a 3x5 identity matrix
    identity_3x5 = np.eye(3, 5)
    print(identity_3x5)

    # 2D diagonal array, with given entries
    diagonal_2D = np.diag([2, 3, 4, 5])
    print(f'diagonal_2D {diagonal_2D}')

    # Create a 5x3 2D array of unsigned integers filled with zeros
    arr_5x3_zeros = np.zeros((5,3), dtype=np.uint)
    print(f'arr_5x3_zeros {arr_5x3_zeros}') 

    # Create a 5x3 2D array of unsigned integers filled with ones
    arr_5x3_ones = np.ones((5,3), dtype=np.uint)
    print(f'arr_5x3_ones {arr_5x3_ones}') 

    # Create a 5x3 2D array of unsigned integers filled with another value
    arr_5x3_full = np.full((5,3), np.pi)
    print(f'arr_5x3_full {arr_5x3_full}') 

    # Create a 5x3 2D array of unsigned integers filled with random numbers
    arr_5x3_random = np.random.random((5,3))
    print(f'arr_5x3_random {arr_5x3_random}') 





if __name__ == "__main__":
    main()