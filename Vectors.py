from math import sqrt
from math import acos
from math import pi
from decimal import Decimal,getcontext

getcontext().prec = 30


class Vector(object):

    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.magnitude = self.mag()

        except ValueError:
            raise ValueError('the coordinates must not be empty')
        except TypeError:
            raise TypeError('the coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def plus(self, v):
        w = []
        n = len(self.coordinates)
        for i in range(n):
            w.append(self.coordinates[i] + v.coordinates[i])
        return Vector(w)

    def sub(self, v):
        w = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(w)

    def scalar_mul(self, scalar):
        w = [scalar*x for x in self.coordinates]
        return Vector(w)

    def mag(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalise(self):
        try:
            magnitude = self.mag()
            w = [x/magnitude for x in self.coordinates]
        except ZeroDivisionError:
            raise  ZeroDivisionError('cannot normalise zero vector')
        return Vector(w)

    def dot_product(self,v):
        product = [x * y for x, y in zip(self.coordinates,v.coordinates)]
        return sum(product)

    def cross_product(self,v):
        try:
            x1,y1,z1 = self.coordinates
            x2,y2,z2 = v.coordinates

            new_coordinates = [
                y1*z2-y2*z1,
                x2*z1-x1*z2,
                x1*y2-x2*y1
            ]
            return Vector(new_coordinates)
        except Exception as e:
            raise e

    def angle_in_radians(self,v):
        angle = acos(self.dot_product(v)/(self.magnitude * v.magnitude))
        return angle

    def angle_in_degrees(self,v):
        angle = self.angle_in_radians(v)
        angle *= 180 / pi
        return angle

    def parallel_check(self,v):
        angle = self.angle_in_degrees(v)
        if angle in [0, 180]:
            print 'parallel vectors'
            return True
        else:
            print 'not parallel'
            return False

    def orthogonal_check(self,v,tolerance = 1e-10):
        dot_product = self.dot_product(v)
        if abs(dot_product) < tolerance:
            print 'orthogonal vectors'
            return True
        else:
            print 'not orthogonal'
            return False

    def projection_on(self,v):
        try:
            u = v.normalise()
            weight = (self.dot_product(u))
            return u.scalar_mul(weight)
        except Exception as e:
            raise e

    def orthogonal_to(self,v):
        try:
            projection = self.projection_on(v)
            orthogonal = self.sub(projection)
            return orthogonal
        except Exception as e:
            raise e

    def area_of_paralleogram(self,v):
        w = self.cross_product(v)
        return w.magnitude

    def area_of_triangle(self,v):
        return 0.5*self.area_of_paralleogram(v)




u = Vector([8.218,-9.314])
v = Vector([-1.219,2.111])
print u.plus(v)

u = Vector([7.119,8.215])
v = Vector([-8.223,0.878])
print u.sub(v)

v = Vector([1.671,-1.012,-0.318])
c = 7.41
print v.scalar_mul(c)

v = Vector([-0.221,7.437])
print v.mag()

v = Vector([8.813,-1.331,-6.247])
print v.mag()

v = Vector([5.581,-2.136])
print v.normalise()

v = Vector([1.996,3.108,-4.554])
print v.normalise()

u = Vector([7.887,4.138])
v = Vector([-8.802,6.776])
print u.dot_product(v)

u = Vector([-5.955,-4.904,-1.874])
v = Vector([-4.496,-8.755,7.103])
print u.dot_product(v)

u = Vector([3.183,-7.627])
v = Vector([-2.668,5.319])
print u.angle_in_radians(v)

u = Vector([7.35,0.211,5.188])
v = Vector([2.751,8.259,3.985])
print u.angle_in_degrees(v)

u = Vector([-7.579,-7.88])
v = Vector([22.737,23.64])
u.parallel_check(v)
u.orthogonal_check(v)

u = Vector([-2.029,9.97,4.172])
v = Vector([-9.231,-6.639,-7.245])
u.parallel_check(v)
u.orthogonal_check(v)

u = Vector([-2.328,-7.284,-1.214])
v = Vector([-1.821,1.072,-2.94])
u.parallel_check(v)
u.orthogonal_check(v)

u = Vector([3.039,1.879])
v = Vector([0.825,2.036])
print u.projection_on(v)

u = Vector([-9.88,-3.264,-8.159])
v = Vector([-2.155,-9.353,-9.473])
print u.orthogonal_to(v)

u = Vector([3.009,-6.172,3.692,-2.51])
v = Vector([6.404,-9.144,2.759,8.718])
print u.projection_on(v)
print u.orthogonal_to(v)

u = Vector([8.462,7.893,-8.187])
v = Vector([6.984,-5.975,4.778])
print u.cross_product(v)

u = Vector([-8.987,-9.838,5.031])
v = Vector([-4.268,-1.861,-8.866])
print u.area_of_paralleogram(v)

u = Vector([1.5,9.547,3.691])
v = Vector([-6.007,0.124,5.772])
print u.area_of_triangle(v)