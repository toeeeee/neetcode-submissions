class Solution:
    def countBits(self, n: int) -> List[int]:
        bitArray = [0 for i in range(n+1)]
        for i in range(n+1):
            index = i
            print(i)
            ones = 0
            while i > 0:
                print(i)
                if (i%2==1):
                    ones += 1
                i = i // 2
                print(i)
            print()
            bitArray[index] = ones
        return bitArray
        