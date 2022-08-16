// https://leetcode.com/problems/design-a-food-rating-system

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.memo_rating = defaultdict(int)
        self.cuisine = defaultdict(str)
        self.heap = defaultdict(list)
        n = len(foods)
        for i in range(n):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.memo_rating[food] = rating
            self.cuisine[food] =(cuisine)
            heapq.heappush(self.heap[cuisine], [-rating, food])


    def changeRating(self, food: str, newRating: int) -> None:
        self.memo_rating[food] = newRating
        heapq.heappush(self.heap[self.cuisine[food]], [-newRating, food])
        return 

    def highestRated(self, cuisine: str) -> str:
        # the highest rating in the heap is -self.heap[cuisine][0][0], the name of the food is self.heap[cuisine][0][1]
        # we pop off elements that are not correct by comparing the rating with memorized ones
        while self.heap and self.memo_rating[self.heap[cuisine][0][1]] != -self.heap[cuisine][0][0]:
            heapq.heappop(self.heap[cuisine])
        ans = self.heap[cuisine][0][1] if self.heap else -1
        return ans


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)