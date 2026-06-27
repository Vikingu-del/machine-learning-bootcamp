import itertools
from typing import List, Union, Iterator, Tuple, Optional

class Vector:
    def __init__(self, values: Union[List[List[float]], int, Tuple[int, int]]):
        """Initializes the Vector and triggers shape/type validation."""
        self.values: List[List[float]] = []
        self.shape: Optional[Tuple[int, int]] = None

        if not isinstance(values, list):
            raise TypeError("Vector must be initialized with a list.")
        
        if len(values) == 0:
            raise ValueError(
                "Vector must be initialized with a non-empty list."
            )

        self.values: List[List[float]] = values
        self.shape: tuple[int, int] = None
        self._validate_and_set_shape()


    def _validate_and_set_shape(self):
        """Validates if the nested list is a true Row or Column vector of floats.

        Sets the shape or exits on error.
        """
        # Scenario A: Potential Row Vector -> Shape must be exactly [[x, y, z, ...]]
        if len(self.values) == 1:
            row_content = self.values[0]

            # Ensure the single item is a non-empty list
            if not isinstance(row_content, list) or len(row_content) == 0:
                raise TypeError(
                    "Row vector content must be stored within a nested list."
                )
            
            if len(row_content) == 0:
                raise ValueError("Row vector cannot be empty.")


            if not all(isinstance(x, (float, int)) for x in row_content):
                raise TypeError("All elements in a Row vector must be floats.")

            self.shape = (1, len(row_content))

        # Scenario B: Potential Column Vector -> Shape must be [[x], [y], [z], ...]
        else:
            # 1. Every element in the outer list must be a list of length exactly 1
            if not all(isinstance(row, list) for row in self.values):
                raise TypeError("Column vector rows must be nested lists.")

            # 2. Every single element inside those individual rows must be a float
            if not all(len(row) == 1 for row in self.values):
                raise ValueError(
                    "Column vector rows must each contain exactly one element (width = 1)."
                )
            
            if not all(isinstance(row[0], float) for row in self.values):
                raise TypeError(
                    "All elements in a Column vector must be floats."
                )

            self.shape = (len(self.values), 1)


    def _flat_v(self) -> Iterator[float]:
        """Flattens the nested vector list into a lazy iterator of floats."""
        return itertools.chain.from_iterable(self.values)

    def __str__(self) -> str:
        return f"Vector({self.values})"
    

    def __repr__(self) -> str:
        return self.__str__()

    
    def dot(self, vb: "Vector") -> float:
        """Calculates the dot product between two vectors of the identical shape.

        Returns a single scalar float.
        """
        if self.shape == vb.shape:
            va_flat = self._flat_v()
            vb_flat = vb._flat_v()
            return float(sum(a * b for a, b in zip(va_flat, vb_flat)))
        raise ValueError(
            f"Dot product requires vectors of the exact same shape. Got {self.shape} and {vb.shape}."
        )


    def T(self) -> "Vector":
        v_flat = self._flat_v()
        new_values = []
        if self.shape[0] == 1:
            new_values = [[element] for element in v_flat]
        else:
            new_values = [list(v_flat)]
        return Vector(new_values)


    def __add__(self, other: "Vector") -> "Vector":
        """Handles vector + vector (Element-wise addition)."""
        if not isinstance(other, Vector):
            raise NotImplementedError(
                "Addition is only supported between two Vector instances."
            )

        if self.shape != other.shape:
            raise ValueError("Vectors must have the exact same shape to be added.")

        flat_a = self._flat_v()
        flat_b = other._flat_v()

        if self.shape[0] == 1:
            new_values = [[a + b for a, b in zip(flat_a, flat_b)]]
        else:
            new_values = [[a + b] for a, b in zip(flat_a, flat_b)]

        return Vector(new_values)
    

    def __radd__(self, other: "Vector") -> "Vector":
        return self.__add__(other)
    

    def __mul__(self, scalar: Union[float, int]) -> "Vector":
        if isinstance(scalar, Vector):
            raise NotImplementedError(
                "Vector-Vector multiplication is undefined here."
            )
        if not isinstance(scalar, (float, int)):
            raise TypeError("Multiplication partner must be an int or float scalar.")

        flat_a = self._flat_v()
        if self.shape[0] == 1:
            new_values = [[a * scalar for a in flat_a]]
        else:
            new_values = [[a * scalar] for a in flat_a]
        return Vector(new_values)
    

    def __rmul__(self, scalar: Union[float, int]) -> "Vector":
        return self.__mul__(scalar)
    

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise NotImplementedError(
                "Subtraction is only supported between two Vector instances."
            )
        if self.shape != other.shape:
            raise ValueError(
                "Vectors must have the identical shape to be subtracted."
            )

        flat_a = self._flat_v()
        flat_b = other._flat_v()

        if self.shape[0] == 1:
            new_values = [[a - b for a, b in zip(flat_a, flat_b)]]
        else:
            new_values = [[a - b] for a, b in zip(flat_a, flat_b)]
        return Vector(new_values)


    def __rsub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise NotImplementedError(
                "Subtraction is only supported between two Vector instances."
            )
        return other.__sub__(self)


    def __truediv__(self, scalar: Union[float, int]) -> "Vector":
        if isinstance(scalar, Vector):
            raise NotImplementedError("Vector-Vector division is undefined.")
        if not isinstance(scalar, (float, int)):
            raise TypeError("Division partner must be an int or float scalar.")
        if scalar == 0:
            raise ZeroDivisionError("Vector division by zero is undefined.")

        flat_a = self._flat_v()
        if self.shape[0] == 1:
            new_values = [[a / scalar for a in flat_a]]
        else:
            new_values = [[a / scalar] for a in flat_a]
        return Vector(new_values)
    

    def __rtruediv__(self, other: Union[float, int]):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here."
        )
