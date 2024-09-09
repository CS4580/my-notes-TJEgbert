"""1D arrays
"""
import numpy as np

def main():
    """Driven Function
    """
    # Generate a 1D array with values from 0 to 2
    arr_1d = np.array([-2, 1, -5, 10]) # list form so the [1,3,4]
    print(arr_1d, type(arr_1d)) #[1 3 4] array

    numbers = [2, 1, 5, 10]
    print(numbers, type(numbers))

    #Convert list into array
    new_array = np.array(numbers)
    print(new_array, type(new_array))

    # 2D array
    matrix = np.array([[-1, 0, 4], [-3, 6, 9]])
    print(matrix, type(matrix))

    # 3D array
    array3d = np.array([[[-1, 2, 3], 
                [3,5,7]],
                [[3, 2, 5], 
                [3, 2, 5]]
                ])
    print(f'3D array {array3d}')

    # Using the dtype optional argument to explicitly 
    # call the data type of the array
    numbers = [2, 1, 5, -10]
    new_array = np.array(numbers, dtype=np.short)
    print(new_array, new_array.dtype)

    # unsigned data
    pos_numbers = [2, 1, 5, 10]
    new_array = np.array(pos_numbers, dtype=np.ushort)
    print(new_array, new_array.dtype)

    # Floats
    new_array = np.array(pos_numbers, dtype=np.float32)
    print(new_array, new_array.dtype)

    

if __name__ == "__main__":
    main()