class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # sorted(boxTypes, key=lambda x: x[1])
        boxTypes.sort(key=lambda x:x[1])
        count = 0 
        boxTypes.reverse()
        for box in boxTypes:
                if box[0] < truckSize and truckSize>0:
                    count += box[0] * box[1]
                    truckSize -= box[0]
                else:
                    count += truckSize * box[1]
                    break

        return count
