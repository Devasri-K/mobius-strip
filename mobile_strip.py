import math

class SimpleMobiusStrip:
    def __init__(self, R=1, w=0.4, n=50):
        self.R = R
        self.w = w
        self.n = n
        self.u_list = [2 * math.pi * i / (n - 1) for i in range(n)]
        self.v_list = [(-w/2) + w * i / (n - 1) for i in range(n)]
        self.points = [[self._compute_point(u, v) for u in self.u_list] for v in self.v_list]

    def _compute_point(self, u, v):
        x = (self.R + v * math.cos(u / 2)) * math.cos(u)
        y = (self.R + v * math.cos(u / 2)) * math.sin(u)
        z = v * math.sin(u / 2)
        return (x, y, z)

    def surface_area(self):
        area = 0
        for i in range(self.n - 1):
            for j in range(self.n - 1):
                p1 = self.points[i][j]
                p2 = self.points[i][j+1]
                p3 = self.points[i+1][j]

                v1 = (p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2])
                v2 = (p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2])

                cross = (
                    v1[1]*v2[2] - v1[2]*v2[1],
                    v1[2]*v2[0] - v1[0]*v2[2],
                    v1[0]*v2[1] - v1[1]*v2[0]
                )
                triangle_area = math.sqrt(cross[0]**2 + cross[1]**2 + cross[2]**2) / 2
                area += triangle_area
        return area * 2

    def edge_length(self):
        length = 0
        # Bottom edge
        for j in range(self.n - 1):
            p1 = self.points[0][j]
            p2 = self.points[0][j+1]
            length += self._distance(p1, p2)
        # Top edge
        for j in range(self.n - 1):
            p1 = self.points[-1][j]
            p2 = self.points[-1][j+1]
            length += self._distance(p1, p2)
        return length

    def _distance(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)


mobius = SimpleMobiusStrip()
print("Surface Area ≈ {:.4f}".format(mobius.surface_area()))
print("Edge Length ≈ {:.4f}".format(mobius.edge_length()))
