class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def transform(x):
            return (a * x * x) + (b * x) + c
        answer = []
        left, right = 0, len(nums) - 1
        if a < 0:
            while left <= right:
                left_transformed_val = transform(nums[left])
                right_transformed_val = transform(nums[right])
                if left_transformed_val < right_transformed_val:
                    answer.append(left_transformed_val)
                    left += 1
                else:
                    answer.append(right_transformed_val)
                    right -= 1
        else:
            while left <= right:
                left_transformed_val = transform(nums[left])
                right_transformed_val = transform(nums[right])
                if left_transformed_val > right_transformed_val:
                    answer.append(left_transformed_val)
                    left += 1
                else:
                    answer.append(right_transformed_val)
                    right -= 1
            answer.reverse()
        return answer
