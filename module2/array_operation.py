"""Do array operations
"""

import numpy as np

def main():
    """Driven Function
    """
    numbers_lst = [2,4,6, 8, 10]
    print(f'Before list{numbers_lst}')
    for num in range(len(numbers_lst)):
        numbers_lst[num] = numbers_lst[num] + 3
    print(f'After list {numbers_lst}')

    # Convert list to an Numpy array
    numbers_arr = np.array(numbers_lst)
    print(f'Before array {numbers_arr}')
    numbers_arr += 3
    print(f'After array {numbers_arr}')


if __name__ == "__main__":
    main()