# Given Coordinate of N points on a 2D plane .Count no of right angle triangle using the set of points such that two small side of right angle triangle should be parallel to x axis and y axis
from itertools import count
from typing import List
class Solution():
    def countRightAngle1(self,coordinate:List[tuple]):
        count = 0
        # Considering the all three pairs of point and check for that these point can make triangle
        # this will take the Time Complexity 
        for middle in range(len(coordinate)):
            for vertical in range(len(coordinate)):
                # to avoid the taking the same point
                if vertical == middle:
                    continue
                for horizontal in range(len(coordinate)):
                    if middle == horizontal or vertical == horizontal:
                        continue
                    # check for right angle
                    if coordinate[middle][0] == coordinate[vertical][0] and coordinate[middle][1] == coordinate[horizontal][1]:
                        count +=1
        return count

    def countRightAngle2(self,coordinate:List[tuple]):
        """
            We will now consider only two pairs of points using that pair we will find the third points that make the right angle triangle.

            Time Complexity ==> O(n^2)
        """
        count = 0 
        hashset = set(coordinate)
        # print(hashset)
        for vertical in range(len(coordinate)):
            for horizontal in range(vertical+1,len(coordinate)):
                
                # to avoid the hypotenuse to be parallel to the any axis
                if coordinate[vertical][0] == coordinate[horizontal][0] or coordinate[vertical][1] == coordinate[horizontal][1]:
                    continue

                
                if (coordinate[vertical][0],coordinate[horizontal][1]) in hashset:
                    count +=1

                if (coordinate[horizontal][0],coordinate[vertical][1]) in hashset:
                    count +=1

                
        return count

    def countRightAngle3(self,coordinate):
        """
            Now we try to choose point and the other two point that will make the right angle triangle 

            Time Complexity ==> O(n)
        """

        count = 0 
        x_hashmap ={}
        y_hashmap ={}
        # print(coordinate)
        for coord in coordinate:
            # for the x coordinate
            if coord[0] in x_hashmap:
                x_hashmap[coord[0]] += 1
            else:
                x_hashmap[coord[0]] = 1

            # for the y coordinate
            if coord[1] in y_hashmap:
                y_hashmap[coord[1]] += 1
            else:
                y_hashmap[coord[1]] = 1

        # print(x_hashmap)
        # print(y_hashmap)
        
        # take each point as the middle point and find number of vertical and horizontal point are there.
        for middle in coordinate:
            number_x = x_hashmap[middle[0]]
            number_y = y_hashmap[middle[1]]  
                                      
            count += ((number_x-1) *(number_y-1)) 
            
        return count
            





    


if __name__ == "__main__":
    test =Solution()
    coordinate = [(1,1),(1,3),(3,3),(5,1),(5,3)]
    print(test.countRightAngle1(coordinate))
    print(test.countRightAngle2(coordinate))
    print(test.countRightAngle3(coordinate))