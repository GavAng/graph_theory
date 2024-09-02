from typing import Hashable

type Point2d = tuple[float, float]
# consider type Point = tuple[float, ...]
type Vertex = Hashable
type Edge[T: Vertex] = tuple[T, T]
