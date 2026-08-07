class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        mapping = {}

        for i in range(len(position)):
            mapping[position[i]] = speed[i]

        position = sorted(position, reverse=True)

        for car in position:
            if len(fleets) == 0:
                fleets.append(car)

            else:
                hours = (target - car) / mapping[car]
                hours_last_fleet = (target - fleets[-1]) / mapping[fleets[-1]]
                
                if hours > hours_last_fleet:
                    fleets.append(car)

        return len(fleets)