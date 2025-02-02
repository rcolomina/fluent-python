from math import hypot
from typing import Self


class Vector:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return "Vector(%r, %r)" % (self.x, self.y)  # %r placeholder is classic formatting with % operator
    
    def __add__(self, other: Self) -> Self:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
        
    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __abs__(self) -> bool:
        return hypot(self.x, self.y)
    
    def __mul__(self, scalar: float) -> Self:
        return Vector(self.x * scalar, self.y * scalar)
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    # alternative faster implementation of __bool__
    # def __bool__(self) -> bool:
    #     return bool(self.x or self.y)
    
if __name__ == "__main__":
    
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    
    r = v1+v2
    expected = Vector(4,5)
    print(r, expected)

    
    assert r == expected
    
    v = Vector(3,4 )
    
    assert abs(v) == 5.0
    assert v * 3 == Vector(9,12)  # WARNING! product of vector by scalar can only done from the right
    assert abs(v*3) == 15.0
    
    # notice that 3 * v is not possible
    
    #  if statement is False if module of Vector(0,0) is 0
    assert True if not Vector(0,0) else False
