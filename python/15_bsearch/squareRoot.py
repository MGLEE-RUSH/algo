# 1.求一个数的平方根，精确度到小数点后6位
#
# Author:Lee

def square_root(num):
    '''求一个数的平方根，精确到小数点后6位.
    参数:
        num:待求解的数
    '''
    if num < 0:  # 如果输入不正确，则直接返回-1
        return -1

    low = 0
    high = num
    mid = low + (high - low) / 2

    while (abs(mid ** 2 - num)) > (1e-7):
        if (mid ** 2 < num):
            low = mid
            mid = mid + (high - mid) / 2
        else:
            high = mid
            mid = low + (mid - low) / 2

    return round(mid, 6)
