class Solution:
    def verticleLine(self, coordinates: List[List[int]]) -> bool:
        for j in range(len(coordinates) - 1):
            if coordinates[j][0] != coordinates[j+1][0]:
                return False
        return True
        
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:        
        for i in range(1,len(coordinates)):
            if (coordinates[i][0] == coordinates[0][0]):
                return self.verticleLine(coordinates)
                 
            if ((coordinates[i][1] - coordinates[0][1])/ (coordinates[i][0] - coordinates[0][0]) != (coordinates[1][1] - coordinates[0][1])/ (coordinates[1][0] - coordinates[0][0])):
                return False
        return True
 #1