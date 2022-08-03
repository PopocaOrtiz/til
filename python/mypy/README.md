# mypy
- you can asign a value of type Any to a variable with a more precise type

## tuples
- `tuple[int, float]`  # tuple with two elements, one float a-
nd the other float
- `tuple[int, ...]`  # tuple with a variable number of elements of type int
**Question:** When returning a basic generator, the function's return value ca-
n be typed as Iterable or Iterator, but what's the difference between both of 
them?
- you can use Sequence instead of tuple

## Callable types and lambdas
- `Callable[[A1, ..., An], Rt]`  # function that accepts An arguments an retur-
ns Rt
- Only positional arguments without default value
- `Callable[..., T]`  # arbitrary number and type of arguments, just define the
return type
- `Optional[...]` does not mean a function argument with a default value

## Union
- can be also defined with | 

## TypeAlias
- Type to define an explicit type aliases

## namedtuple
```python
from typing import NamedTuple
Point = NamedTuple('Point',[('x', int), ('y', int)]
# or
class Point(NamedTuple):
    x: int
    y: int
```
