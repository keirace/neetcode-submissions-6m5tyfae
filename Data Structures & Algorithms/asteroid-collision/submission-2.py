class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # moving in diff directions
            while a < 0 and stack and stack[-1] >= 0:
                diff = a + stack[-1]
                # size of a >= prev; destroy the smaller or equal sized ones
                if diff <= 0:
                    # equal size: both explode
                    if stack.pop() == -a:
                        a = 0
                else:
                    a = 0
            if a:
                stack.append(a)

        return stack