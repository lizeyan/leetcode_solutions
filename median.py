class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        if len(nums2) < 6:
            return self.trival_median(nums1, nums2)
        if (len(nums1) << 1) < len(nums2):
            removed_length = int((len(nums2) - len(nums1) - 1) / 2)
            return self.findMedianSortedArrays(nums1, nums2[removed_length:len(nums2) - removed_length])
        idx_s1 = int(len(nums1) / 2)
        idx_s2a = len(nums1) - idx_s1 - 1
        idx_s2b = len(nums2) - idx_s1 - 1
        if nums1[idx_s1] > nums2[idx_s2b]:
            return self.findMedianSortedArrays(nums1[:idx_s1 + 1], nums2[idx_s2a:])
        elif nums1[idx_s1] < nums2[idx_s2a]:
            return self.findMedianSortedArrays(nums1[idx_s1:], nums2[:idx_s2b + 1])
        else:
            return self.findMedianSortedArrays(nums1, nums2[idx_s1:idx_s2b + 1])

    def trival_median(self, l1, l2):
        l = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                l.append(l1[i])
                i += 1
            else:
                l.append(l2[j])
                j += 1
        if i == len(l1):
            l.extend(l2[j:])
        else:
            l.extend(l1[i:])
        if len(l) % 2 == 0:
            return (float(l[int(len(l) / 2)] + l[int(len(l) / 2) - 1])) / 2
        else:
            return l[int(len(l) / 2)]
