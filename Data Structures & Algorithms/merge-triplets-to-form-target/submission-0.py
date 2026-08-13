class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        present = [False, False, False]

        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue

            if triplets[i][0] == target[0] and not present[0]:
                present[0] = True
            if triplets[i][1] == target[1] and not present[1]:
                present[1] = True
            if triplets[i][2] == target[2] and not present[2]:
                present[2] = True

        return present[0] and present[1] and present[2]


