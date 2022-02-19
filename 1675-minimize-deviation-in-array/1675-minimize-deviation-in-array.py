class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq=[]
        minimum=float('inf')
        for num in nums:
            if num%2==0:
                ele=num
            else:
                ele=2*num
            minimum=min(minimum,ele)
            heapq.heappush(pq,-ele)

        currMax=float('inf')
        while pq:
            curr=-heapq.heappop(pq)
            currMax=min(currMax,curr-minimum)
            if curr%2==0:
                ele=curr//2
                minimum=min(minimum,ele)
                heapq.heappush(pq,-ele)
            else:
                return currMax
