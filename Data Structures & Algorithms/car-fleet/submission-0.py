class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed))
        for p, v in cars:
            t = (target - p) / v
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
            
        return len(stack)