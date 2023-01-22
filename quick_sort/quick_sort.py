# Quick Sort by Alessia Sarritzu
import unittest

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


class Test(unittest.TestCase):
    def test_numeric(self):
        arr = [3, 82, 15, 1, 40, 37, 63]
        quickSort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 3, 15, 37, 40, 63, 82])

    def test_alphabetic(self):
        arr = ['z', 'o', 'p', 'a', 'c', 'h']
        quickSort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, ['a', 'c', 'h', 'o', 'p', 'z'])


if __name__ == "__main__":
    unittest.main()
