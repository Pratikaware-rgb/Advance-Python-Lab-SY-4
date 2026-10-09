
# Read data from the input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Count the total number of lines
print("Total number of lines:", len(lines))

# Extract the first two lines
first_two_lines = lines[:2]

# Write the extracted lines into a new file
with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("First two lines written to output.txt successfully!")
