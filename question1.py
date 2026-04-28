import sys
if len(sys.argv) != 3:
        raise ValueError

total_load = float(sys.argv[1])
num_supports = float(sys.argv[2])
print("Error: Invalid input! Enter numeric values only.")
