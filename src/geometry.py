""" Geometry related questions """

def checkStraightLine(coordinates: list[list[int]]) -> bool:
    """ check coordinateds makes a straight line or not
        https://leetcode.com/problems/check-if-it-is-a-straight-line
        [Datadog]
    """
    n = len(coordinates)
    if n <= 2:
        return True
    # as there is no duplicate, we use two points to get slope and intercept
    (x1, y1), (x2,y2) = coordinates[0], coordinates[1]
    # slope is infinity
    if x1 == x2:
        for p in coordinates:
            if p[0] != x1:
                return False
    elif y1 == y2:
        # slop is zero
        for p in coordinates:
            if p[1] != y1:
                return False
    else:
        # other cases
        slope = (y2-y1)/(x2-x1)
        intercept = y1 - slope * x1
        for p in coordinates:
            if p[1] != slope * p[0] + intercept:
                return False
    return True