"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check
if these points make a straight line in the XY plane.
Ex. 1
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true
Ex. 2
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false
"""

co = [[0,0],[1,1],[1,1],[2,1],[5,1]]
    # [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    # [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    # [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]


def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True

    try:
        slope = ((coordinates[-1][1] - coordinates[0][1]) /
                 (coordinates[-1][0] - coordinates[0][0]))
    except ZeroDivisionError:
        slope = None

    print("Slope:", slope)
    for pt in range(1, len(coordinates) - 1):
        try:
            m = ((coordinates[pt][1] - coordinates[0][1]) /
                     (coordinates[pt][0] - coordinates[0][0]))
            if m != slope:
                return False
        except ZeroDivisionError:
            if coordinates[pt][0] == coordinates[0][0] and slope is None:
                continue
            return False

    return True


print(checkStraightLine(co))