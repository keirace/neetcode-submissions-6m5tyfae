class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        count = Counter(hand)
        minheap = list(count.keys())
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    # handler for a case that number > min is popped first
                    # can return false right away (eg. 2 is popped before 1, creating a gap and won't work anyway)
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)

        return True