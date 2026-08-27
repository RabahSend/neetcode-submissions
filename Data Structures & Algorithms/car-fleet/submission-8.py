class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = {}

        for pos, spd in zip(position, speed):
            cars[pos] = spd

        position.sort(reverse=True)

        def path(pos, spd, trgt):
            return (trgt - pos) / spd

        for i in range(len(position)):
            hours = path(position[i], cars[position[i]], target)

            if stack and stack[-1] >= hours:
                continue
            
            stack.append(hours)

        return len(stack)