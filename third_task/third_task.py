from random import randint

def merge_two_list(arr, start, middle, end):
    result_lst = [None] * (end - start + 1)
    i = start
    j = middle + 1
    k = 0

    while i <= middle and j <= end:
        if arr[i] < arr[j]:
            result_lst[k] = arr[i]
            i += 1
        else:
            result_lst[k] = arr[j]
            j += 1
        k += 1

    while i <= middle:
        result_lst[k] = arr[i]
        i += 1
        k += 1

    while j <= end:
        result_lst[k] = arr[j]
        j += 1
        k += 1

    for idx, val in enumerate(result_lst):
        arr[start + idx] = val

    return arr


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        for j in range(i, left, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr


def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run

    while size < n:
        for start in range(0, n, size * 2):
            middle = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            if middle > end:
                break

            merge_two_list(arr, start, middle, end)

        size *= 2

    return arr

if __name__ == '__main__':
    print(tim_sort([randint(1, 100) for i in range(66)]))


# Пояснения:
# Timsort - алгоритм, который сейчас встроен в питоне. Считается одним из лучших по сложности O большое.
# Коротко суть алгоритма и почему он хорош:
# 1. По специальному алгоритму вычисляется minrun, по которому будут разбивать исходный массив на подмассивы. Сейчас
#    установлен 32.
# 2. Каждый подмассив сортируется сортировкой вставками (def: insertion_sort) - тк в лучшем случае данная сортировка
#    показывает сложность O(n). В сравнении, если сортировать подмассивы слиянием - сложность будет O(n log n).
# 3. Собираем отсортированные подмассивы в результирующий массив, с помощью слияния двух списков по двум
#    указателям (def: merge_two_list). Сложность данной операции в лучшем случае, тоже O(n).

# Объединяя две сложности - получаем лучшую общую сложность тимсорта = O(n) в лучшем случае.
# На реальных данных - эта сложность ухудшается до O(n log n).