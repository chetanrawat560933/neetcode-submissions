class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_so_far = -1

        for i in reversed(range(len(arr))):
            current = arr[i]
            arr[i] = max_so_far
            max_so_far = max(current,max_so_far)
        
        return arr