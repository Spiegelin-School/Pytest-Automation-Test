def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    if base == 0:
        raise ValueError("Base cannot be zero")
    return (base * height) / 2 