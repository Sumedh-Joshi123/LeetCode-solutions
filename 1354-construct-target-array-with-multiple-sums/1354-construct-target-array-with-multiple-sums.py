class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxHeap, hasOnes, currentSum = [], 0, False
        for num in target:
            currentSum += num
            if num == 1:
                hasOnes = True
            else:
                maxHeap.append(-num)
        if hasOnes:
            maxHeap.append(-1) 
        heapify(maxHeap)

       
        while True:
            maxNum = -maxHeap[0]

            if maxNum == 1:
                return True

            if len(maxHeap) == 1:
                return False

            sumOfOtherNums = currentSum - maxNum

            if sumOfOtherNums == 1:
                return True

            if maxNum <= sumOfOtherNums:
                return False

            previousNum = maxNum % sumOfOtherNums
            if previousNum == 0:
                return False

            heapreplace(maxHeap, -previousNum)
            currentSum = sumOfOtherNums + previousNum