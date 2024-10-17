'''
Gurleen Kaur jassal (100942372)
TPRG 2131 Fall 2024 Assignment 1
16,October,2024
TPRG 2131 Fall 2024 Assignment 1, Test file template.
Phil J <philip.jarvis@durhamcollege>

This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).

# test_A_V_calc.py
import pytest  # Import pytest for testing
# Import the functions to be tested from A_V_calc module
from A_V_calc import calculate_area_of_rectangle, calculate_area_of_circle, calculate_volume_of_cylinder, calculate_area_of_triangle, calculate_volume_of_cube

# Test function for calculating the area of a rectangle
def test_calculate_area_of_rectangle():
    assert calculate_area_of_rectangle(4, 5) == 20.0  # Test with length=4, width=5
    assert calculate_area_of_rectangle(10, 2) == 20.0  # Test with length=10, width=2
    assert calculate_area_of_rectangle(2, 5) == 10.0  # Test with length=2, width=5

# Test function for calculating the area of a circle
def test_calculate_area_of_circle():
    assert calculate_area_of_circle(5) == 78.5  # Test with radius=5
    assert calculate_area_of_circle(10) == 314.2  # Test with radius=10
    assert calculate_area_of_circle(20) == 1256.6  # Test with radius=20

# Test function for calculating the volume of a cylinder
def test_calculate_volume_of_cylinder():
    assert calculate_volume_of_cylinder(5, 10) == 785.4  # Test with radius=5, height=10
    assert calculate_volume_of_cylinder(6, 12) == 1357.2  # Test with radius=6, height=12
    assert calculate_volume_of_cylinder(7, 14) == 2155.1  # Test with radius=7, height=14

# Test function for calculating the area of a triangle
def test_calculate_area_of_triangle():
    assert calculate_area_of_triangle(4, 5) == 10.0  # Test with base=4, height=5
    assert calculate_area_of_triangle(10, 2) == 10.0  # Test with base=10, height=2
    assert calculate_area_of_triangle(28, 4) == 56.0  # Test with base=28, height=4

# Test function for calculating the volume of a cube
def test_calculate_volume_of_cube():
    assert calculate_volume_of_cube(5) == 125.0  # Test with side length=5
    assert calculate_volume_of_cube(10) == 1000.0  # Test with side length=10
    assert calculate_volume_of_cube(50) == 125000.0  # Test with side length=50
