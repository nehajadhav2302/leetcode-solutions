class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Pair each number with its original index and sort by value
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        n = len(nums)
        ans = [0] * n
        
        # Group elements into components
        curr_component_vals = []
        curr_component_indices = []
        
        for i in range(n):
            # If starting a new component
            if not curr_component_vals or sorted_nums[i][0] - curr_component_vals[-1] <= limit:
                curr_component_vals.append(sorted_nums[i][0])
                curr_component_indices.append(sorted_nums[i][1])
            else:
                # Process the previous component: place sorted values into sorted original indices
                curr_component_indices.sort()
                for idx, val in zip(curr_component_indices, curr_component_vals):
                    ans[idx] = val
                
                # Start new component with current element
                curr_component_vals = [sorted_nums[i][0]]
                curr_component_indices = [sorted_nums[i][1]]
        
        # Process the last component
        curr_component_indices.sort()
        for idx, val in zip(curr_component_indices, curr_component_vals):
            ans[idx] = val
            
        return ans