def task(array, start=0, stop=0):
    if stop == 0:
        stop = len(array)
    middle = (start + stop) // 2
    if array[middle] == '1':
        if array[middle + 1] == '0':
            return middle + 1
        else:
            return task(array, middle, stop)
    else:
        if array[middle - 1] == '1':
            return middle
        else:
            return task(array, start, middle)


if __name__ == '__main__':
    print(task("111111111111111111111111100000000"))
