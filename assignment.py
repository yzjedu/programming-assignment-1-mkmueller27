# Name: Kristina Mueller
# Course: CS701/GB735, Dr. Yalew
# Date: August 4, 2024
# Programming Assignment: 1
# Program Inputs: Dimensions of the room (length, width, height) in feet
# Program Outputs: Total area to be painted (in square feet), amount of primer (in gallons), amount of paint (in gallons)

def main():
    
    '''This program Computes the amount of paint needed one more'''
    # Step 1: Ask the user for the dimensions of the room
    # The three dimensions are length - height - width 
UserInputLength = float((input("Enter the length of the room: ")))
UserInputHeight = float((input("Enter the height of the room: ")))
UserInputWidth = float((input("Enter the width of the room: ")))


    # Step 2: Compute the total area of the four walls and ceiling
    # Area of walls = 2 * (length * height + width * height)
area_walls = 2 * (UserInputLength *  UserInputHeight + UserInputWidth * UserInputHeight)
print (area_walls)
   
    # Area of ceiling = length * width
area_ceiling = UserInputLength * UserInputWidth
print (area_ceiling)

    # Total area = Area of walls + Area of ceiling
total_area = area_walls + area_ceiling
print(total_area)

    # Step 3: Calculate the amount of primer and paint needed
    # Primer coverage = 200 square feet per gallon
primer_needed = float(total_area / 200)
    # Paint coverage = 350 square feet per gallon
paint_needed = float(total_area / 350)

    # Step 4: Output the total area and the amount of primer and paint needed
    # Uncomment the three lines below for the output
print(f"Total area to be painted: {total_area:.2f} square feet")

print(f"Amount of primer needed: {primer_needed:.2f} gallons")

print(f"Amount of paint needed: {paint_needed:.2f} gallons")

if __name__ == "__main__":
    main()