class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        avg = 0
        finish = 0
        count = len(customers)
        for arrive, time in customers:
            finish = max(finish, arrive) + time
            wait = finish - arrive
            avg += wait
        return avg / count