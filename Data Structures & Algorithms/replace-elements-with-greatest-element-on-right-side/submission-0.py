class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        largest = arr[length-1]
        pos = length-1
        arr[pos] = -1
        pos -= 1
        while pos >= 0 :
            temp = arr[pos]
            arr[pos] = largest
            largest = max(largest, temp)
            pos -= 1
        return arr