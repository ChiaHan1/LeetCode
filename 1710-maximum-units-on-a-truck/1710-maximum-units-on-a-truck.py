class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort the box
        boxTypes.sort(key=lambda x: -x[1])
        
        current_size = 0
        max_units = 0
        
        for num_box, unit in boxTypes:
            max_units += unit * min(truckSize - current_size, num_box)
            current_size += min(truckSize - current_size, num_box)
            
        return max_units