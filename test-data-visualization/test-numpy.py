# 测试numpy库提供的科学计算功能
import numpy as np


def main():
    ndarray = np.arange(1, 9)
    result = ndarray.reshape((2, 4), order='F')
    print(f'{result}')


if __name__ == '__main__':
    main()
