class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for i in hand:
            if count[i]:
                for i in range(i, i+groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True

