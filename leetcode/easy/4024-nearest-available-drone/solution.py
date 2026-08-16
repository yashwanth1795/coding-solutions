class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        min_distance=float('inf')
        answer=-1
        for i in range(len(drones)):
            do=drones[i]
            m=abs(do[0]-target[0])+abs(do[1]-target[1])
            if m<=do[2]:
                 if m<min_distance:
                    min_distance=m
                    answer=i
        return answer