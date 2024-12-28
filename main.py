#!/usr/bin/python3

from z3 import *
import argparse
import csv

def read_level(filename):
    # Open the file
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                # int_row = [int(item) if item is not "" else -1 for item in row]  # Convert each item in the row to an integer
                coordinates_row = [(int(item.split(" ")[0]), int(item.split(" ")[1])) for item in row]  # Convert each item in the row to an integer
                data.append(coordinates_row)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(-1)

def handle_args():
    parser = argparse.ArgumentParser(description="Solve the mosaik puzzle using Z3 solver.")
    parser.add_argument("file", type=str, help="Path to the input file")

    # Parse command-line arguments
    return parser.parse_args()

def get_neighbors(matrix, row, col):
    # List of relative positions of the 8 neighbors
    neighbors = [
                (-1, 0),             # Top-left, Top, Top-right
        ( 0, -1)       , ( 0, 1),   # Left, Self, Right
                ( 1, 0)              # Bottom-left, Bottom, Bottom-right
    ]
    
    # List to store valid neighbors
    valid_neighbors = []
    
    # Iterate over each relative position
    for dr, dc in neighbors:
        new_row, new_col = row + dr, col + dc
        
        # Check if the new position is within bounds of the matrix
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            valid_neighbors.append(matrix[new_row][new_col])
    
    return valid_neighbors

def detect_level_size(level):
    highest_row = -1
    for group_id, group in enumerate(level):
        print("Group " + str(group_id + 1) + " contains the fields: ", end="")
        for coord in group:
            print("(" + str(coord[0]) + "/" + str(coord[1]) + ")", end="")
            if coord[0] > highest_row:
                highest_row = coord[0]
        print()
    highest_row += 1
    print("Detected level size: " + str(highest_row) + "x" + str(highest_row))
    return highest_row

def add_group_constraints(solver, group_vars):
    solver.add(sum(If(var, 1, 0) for var in group_vars) == 2)

def solve_level(level):
    solver = Solver()
    level_size = detect_level_size(level)
    vars = [[Bool(f"var_{i}_{o}") for i in range(level_size)] for o in range(level_size)]
    
    for group in level:
        group_vars = [vars[coord[0]][coord[1]] for coord in group]
        add_group_constraints(solver, group_vars)

    for row_index, row in enumerate(vars):
        for column_index, square in enumerate(row):
            neighbors = get_neighbors(vars, row_index, column_index)
            solver.add(Implies(square, sum(If(var, 1, 0) for var in neighbors) == 1))

    # Check satisfiability
    if solver.check() == sat:
        model = solver.model()
        return [[model[square] for square in row] for row in vars]  # Return the values of the variables
    else:
        print("No solution exists")
        exit(-1)

def main():
    args = handle_args()

    level = read_level(args.file)
    
    solution = solve_level(level)
    for row in solution:
        for square in row:
            print("X" if square else "O", end=" ")
        print()

if __name__ == "__main__":
    main()