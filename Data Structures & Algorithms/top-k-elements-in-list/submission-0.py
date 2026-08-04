class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        #print(h)

        top_k = []
        for i in range(k):
            m = -1
            m_num = None
            for num, amt in h.items():
                if amt > m:
                    m = amt
                    m_num = num
            del h[m_num]
            top_k += [m_num]

        return top_k

            

