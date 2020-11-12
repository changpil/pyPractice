class Solution:
    def merge(self, nums1,  nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i_index, j_index = 0,0;
        while i_index != len(nums1):
            while j_index != len(nums2):
                if i_index == len(nums1) or j_index == len(nums2):
                    break
                if nums1[i_index] >= nums2[j_index]:
                    nums1.insert(i_index, nums2[j_index])
                    del nums2[j_index]
                    i_index += 1
                else:
                    i_index += 1
            if i_index == len(nums1) or j_index == len(nums2):
                break

        if len(nums2) !=0:
            for c in nums2:
                nums1.append(c)