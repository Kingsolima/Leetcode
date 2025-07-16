class Solution(object):

    def kClosest(self, points, k):
        def get_distance(point):
            return point[0]*point[0] + point[1]*point[1]
        points.sort(key=get_distance)
        return points[:k]