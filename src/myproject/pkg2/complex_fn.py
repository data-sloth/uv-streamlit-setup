from myproject.pkg1 import simple_fn

def square_of_sum(a: float, b: float) -> float:
    c = simple_fn.add(a, b)
    return c * c