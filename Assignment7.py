import re

# Open the file in read mode
file = open("input.txt", "r")

# Read the file
text = file.read()

# Close the file
file.close()

# Pattern for email addresses
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# Find all email addresses
emails = re.findall(pattern, text)

print("Emails found:", emails)
