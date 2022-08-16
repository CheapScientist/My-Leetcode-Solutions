// https://leetcode.com/problems/design-a-number-container-system

class NumberContainers:

    def __init__(self):
        self.container = defaultdict(int) # index: num
        self.heap_memo = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.container[index] = number
        heapq.heappush(self.heap_memo[number], index)
        # print(self.heap_memo)
        # print(self.container)

    def find(self, number: int) -> int:
        if number not in self.heap_memo:
            return -1
        if not self.heap_memo[number]:
            return -1
        while self.container[self.heap_memo[number][0]] != number:
            heapq.heappop(self.heap_memo[number])
            if not self.heap_memo[number]:
                return -1
        return self.heap_memo[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)