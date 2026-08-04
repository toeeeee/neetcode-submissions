class Solution:
    def hammingWeight(self, n: int) -> int:
        numOnes = 0
        while n > 0:
            if n % 2 == 1:
                numOnes += 1
            n = n // 2
        return numOnes
        