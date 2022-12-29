# Merge Sort by Alessia Sarritzu
import unittest


def merge_sort(array):
    size = len(array)
    if size == 1:
        return array

    middle = size // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


def merge(left, right):
    left_index, right_index = 0, 0
    result = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


class Test(unittest.TestCase):

    def test_merge_sort_num(self):
        a = [3, -2, 11, 45, 0.9, 0]
        self.assertEqual(merge_sort(a), [-2, 0, 0.9, 3, 11, 45])

    def test_merge_sort_char(self):
        a = ['z', 'e', 'q', 'l', 'b', 'o']
        self.assertEqual(merge_sort(a), ['b', 'e', 'l', 'o', 'q', 'z'])


if __name__ == '__main__':
    unittest.main()

