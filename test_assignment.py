import numpy as np
from assignment import *

def test_create_array():
    arr = create_array()
    assert isinstance(arr, np.ndarray)
    assert len(arr) == 10

def test_array_arithmetic():
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    result = array_arithmetic(a,b)
    assert (result == np.array([5,7,9])).all()

def test_slicing():
    arr = np.arange(10)
    result = slicing_example(arr)
    assert len(result) == 5

def test_matrix():
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])
    result = matrix_multiplication(a,b)
    assert result.shape == (2,2)

def test_random():
    arr = random_numbers()
    assert len(arr) == 5

def test_plot():
    # just ensure function runs
    plot_graph()
