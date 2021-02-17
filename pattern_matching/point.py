from dataclasses import dataclass
from math import sqrt
from typing import Tuple, Union

@dataclass
class Point2D:
    x: float
    y: float

@dataclass
class Point3d:
    x: float
    y: float
    z: float


Point = Union[Point2D, Point3d, Tuple[float, float], Tuple[float, float, float]]


def get_distance(a: Point, b: Point) -> float:
    match a, b:
        case a:= Point3D(), b:= Point3D():
            return sqrt((b.x-a.x)**2 + (b.y-a.y)**2 + (b.z-a.z)**2)
        case a:= Point2D(), b:= Point2D():
            return sqrt((b.x-a.x)**2 + (b.y-a.y)**2)
        case tuple(ax, ay), tuple(bx, by):
            return sqrt((bx-ax)**2 + (by-ay)**2)
        case tuple(ax, ay, az), tuple(bx, by, bz):
            return sqrt((bx-ax)**2 + (by-ay)**2 + (bz-az)**2)