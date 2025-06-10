import pytest
from triangle import triangle_area

def test_triangle_area_valid():
    assert triangle_area(5, 7) == 17.5

def test_triangle_area_negative_base():
    with pytest.raises(ValueError, match="Base and height must be non-negative"):
        triangle_area(-5, 7)

def test_triangle_area_negative_height():
    with pytest.raises(ValueError, match="Base and height must be non-negative"):
        triangle_area(5, -7)

def test_triangle_area_zero_base():
    with pytest.raises(ValueError, match="Base cannot be zero"):
        triangle_area(0, 7) 