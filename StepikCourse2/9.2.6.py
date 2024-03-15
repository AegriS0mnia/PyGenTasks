nums1 = {int(i) for i in input().split()}
nums2 = {int(j) for j in input().split()}
nums3 = sorted(nums1 & nums2, reverse=True)

if nums3:
    print(*nums3)
else:
    print('BAD DAY')