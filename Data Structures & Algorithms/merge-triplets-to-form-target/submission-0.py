class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # take any 2 and get max
        # filter out the the sub arr with greater values
        # check if target numbers exist in the same index

        good = set()
        for i in triplets:
            if any([i[j] > target[j] for j in range(len(target))]):
                continue
            
            for pos, v in enumerate(i):
                if v == target[pos]:
                    good.add(pos)

        return True if len(good) == 3 else False