# 502. IPO

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        pool = list(zip(capital, profits)); heapify(pool)
        available = []

        cap = w
        for _ in range(k):
            while pool and pool[0][0] <= cap:
                _, p = heappop(pool)
                heappush(available, -p)
            if not available: break
            cap += -heappop(available)
        return cap
