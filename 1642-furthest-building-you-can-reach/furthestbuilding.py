from bisect import insort
def furthestBuilding(heights, bricks, ladders):
    """
    :type heights: List[int]
    :type bricks: int
    :type ladders: int
    :rtype: int
    """
    biggest_jumps = []
    ladders_used = 0
    pos = 0
    while pos < len(heights) - 1:
        jump = heights[pos+1]-heights[pos]
        if jump > 0:
            if ladders_used < ladders:
                insort(biggest_jumps, jump)
                ladders_used += 1
            else:
                if ladders > 0 and jump >= biggest_jumps[0]:
                    if bricks >= biggest_jumps[0]:
                        bricks = bricks - biggest_jumps.pop(0)
                        insort(biggest_jumps, jump)
                    else:
                        return pos
                else:
                    if bricks >= jump:
                        bricks = bricks - jump
                    else:
                        return pos
        pos = pos + 1
    return pos

#heights, bricks, ladders = [4,12,2,7,3,18,20,3,19], 10, 2
#heights, bricks, ladders = [14,3,19,3], 17, 0
#heights, bricks, ladders = [4,2,7,6,9,14,12], 5, 1
#print(furthestBuilding(heights, bricks, ladders))
