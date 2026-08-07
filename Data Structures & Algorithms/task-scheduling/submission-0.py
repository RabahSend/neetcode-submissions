class Solution:
    def execute(self, cooldown, task, current_time, n, freq):
        freq -= 1
        if freq <= 0:
            return
        time = current_time + n + 1

        cooldown.append([task, freq, time])


    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = deque()
        counter = {}
        heap = []
        time = 0

        for elem in tasks:
            counter[elem] = counter.get(elem, 0) + 1

        for key, value in counter.items():
            heapq.heappush(heap, [-value, key])

        while heap or cooldown:
            while cooldown and cooldown[0][2] - time <= 0:
                heapq.heappush(heap, [-cooldown[0][1], cooldown[0][0]])
                cooldown.popleft()

            if heap:
                task = heapq.heappop(heap)
                self.execute(cooldown, task[1], time, n, -task[0])

            time += 1


        return time