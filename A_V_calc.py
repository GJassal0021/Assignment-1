'''
Gurleen Kaur jassal (100942372)
TPRG 2131 Fall 2024 Assignment 1
16,October,2024
Phil J <philip.jarvis@durhamcollege>

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

(Level 1)
    1.First Area/Volume* calulation
    2.Second Area/Volume* calculation
    3.Third Area/Volume* calculation
    4.Fourth Area/Volume* calculation
    5.Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).
# A/V Calculator
# This program calculates areas and volumes of various geometric shapes.
# It includes functions for rectangles, circles, cylinders, triangles, and cubes.

import math  # Import math module for mathematical operations

# Function to request positive input from the user
def request_positive_input(message):
    while True:  # Start an infinite loop for input validation
        value = input(message)  # Prompt the user for input
        # Check if the input is a digit and greater than zero
        if value.isdigit() and float(value) > 0:
            return float(value)  # Convert the input to float and return it
        print("Please enter a value greater than zero.")  # Error message for invalid input

# Function to calculate the area of a rectangle
def calculate_area_of_rectangle(length, width):
    """Calculate the area of a rectangle."""
    area_rectangle1 = length * width  # Formula for area of rectangle
    area_rectangle = round(area_rectangle1, 1)  # Round the result to 1 decimal
    return area_rectangle  # Return the calculated area

# Function to calculate the area of a circle
def calculate_area_of_circle(radius):
    """Calculate the area of a circle."""
    area_circle1 = math.pi * (radius ** 2)  # Formula for area of circle
    area_circle = round(area_circle1, 1)  # Round the result to 1 decimal
    return area_circle  # Return the calculated area

# Function to calculate the volume of a cylinder
def calculate_volume_of_cylinder(radius, height):
    """Calculate the volume of a cylinder."""
    volume_cylinder1 = math.pi * (radius ** 2) * height  # Formula for volume of cylinder
    volume_cylinder = round(volume_cylinder1, 1)  # Round the result to 1 decimal
    return volume_cylinder  # Return the calculated volume

# Function to calculate the area of a triangle
def calculate_area_of_triangle(base, height):
    """Calculate the area of a triangle."""
    area_triangle1 = 0.5 * base * height  # Formula for area of triangle
    area_triangle = round(area_triangle1, 1)  # Round the result to 1 decimal
    return area_triangle  # Return the calculated area

# Function to calculate the volume of a cube
def calculate_volume_of_cube(side):
    """Calculate the volume of a cube."""
    volume_cube1 = side ** 3  # Formula for volume of cube
    volume_cube = round(volume_cube1, 1)  # Round the result to 1 decimal
    return volume_cube  # Return the calculated volume

# Main function to run the A/V calculator
def main():
    while True:  # Start an infinite loop for the main menu
        # Display the calculator menu options
        print("A/V calculator Menu")
        # Prompt the user to enter choice for quitting or view mode
        choice = input("Enter Q/q to quit, V/v to change the calculated view, D/d for default view: ").strip().lower()
        
        # Break the loop if user chooses to quit
        if choice == 'q':
            break
        elif choice == 'v':  # Set view mode to True for detailed view
            view = True
        elif choice == 'd':  # Set view mode to False for default view
            view = False
        else:
            print("Invalid input. Please try again.")  # Handle invalid input
            continue  # Return to the beginning of the loop
        
        while True:  # Start an infinite loop for calculation options
            # Display the options for different area/volume calculations
            print("1. Area of Rectangle")
            print("2. Area of Circle")
            print("3. Volume of Cylinder")
            print("4. Area of Triangle")
            print("5. Volume of Cube")
            print("6. Main Menu")
            
            option = input("Select an option (1-6): ")  # Prompt the user to select an option
            
            # Option for calculating the area of a rectangle
            if option == '1':
                length = request_positive_input("Enter the length of the rectangle: ")  # Get length input
                width = request_positive_input("Enter the width of the rectangle: ")  # Get width input
                result = calculate_area_of_rectangle(length, width)  # Calculate area
                print(f"{length} * {width} = {result} {'(length * width = area)' if view else ''}")  # Display result
            
            # Option for calculating the area of a circle
            elif option == '2':
                radius = request_positive_input("Enter radius: ")  # Get radius input
                result = calculate_area_of_circle(radius)  # Calculate area
                print(f"{radius}^2 * π = {result} {'(radius^2 * π = area)' if view else ''}")  # Display result
            
            # Option for calculating the volume of a cylinder
            elif option == '3':
                radius = request_positive_input("Enter radius: ")  # Get radius input
                height = request_positive_input("Enter height: ")  # Get height input
                result = calculate_volume_of_cylinder(radius, height)  # Calculate volume
                print(f"{radius}^2 * π * {height} = {result} {'(radius^2 * π * height = volume)' if view else ''}")  # Display result
            
            # Option for calculating the area of a triangle
            elif option == '4':
                base = request_positive_input("Enter base: ")  # Get base input
                height = request_positive_input("Enter height: ")  # Get height input
                result = calculate_area_of_triangle(base, height)  # Calculate area
                print(f"0.5 * {base} * {height} = {result} {'(0.5 * base * height = area)' if view else ''}")  # Display result
            
            # Option for calculating the volume of a cube
            elif option == '5':
                side = request_positive_input("Enter side length: ")  # Get side length input
                result = calculate_volume_of_cube(side)  # Calculate volume
                print(f"{side}^3 = {result} {'(side^3 = volume)' if view else ''}")  # Display result
            
            # Option to return to the main menu
            elif option == '6':
                print(" Back to the A/V calculator Menu ")  # Print returning to main menu message
                break  # Break out of the loop to return to the main menu
            
            else:
                print("Invalid option. Please try again.")  # Handle invalid option input

# Entry point of the program
if __name__ == "__main__":
    main()  # Run the main function when script is executed
