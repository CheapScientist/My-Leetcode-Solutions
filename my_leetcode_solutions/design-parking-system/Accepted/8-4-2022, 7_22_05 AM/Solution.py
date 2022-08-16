// https://leetcode.com/problems/design-parking-system

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1: 
            ans = True if self.big else False
            self.big -= 1 if ans else 0
            return ans
        elif carType == 2: 
            ans = True if self.medium else False
            self.medium -= 1 if ans else 0
            return ans
        else:
            ans = True if self.small else False
            self.small -= 1 if ans else 0
            return ans


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)