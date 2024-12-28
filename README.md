# Norinori Solver

a solver for the popular puzzle game [Norinori](https://de.puzzle-norinori.com/).
This solver utilizes the z3 SAT-solver

## Usage

```bash
./main.py levels/test_6x6.csv
```

Output:

```
Group 1 contains the fields: (0/0)(0/1)(0/2)(0/3)(0/4)(1/2)
Group 2 contains the fields: (1/0)(1/1)(2/0)(2/1)
Group 3 contains the fields: (2/2)(2/3)(1/3)
Group 4 contains the fields: (0/5)(1/5)(2/5)(3/5)(1/4)(2/4)
Group 5 contains the fields: (3/0)(3/1)(3/2)(3/3)(3/4)(4/3)
Group 6 contains the fields: (4/0)(4/1)(4/2)(5/2)(5/3)
Group 7 contains the fields: (5/0)(5/1)
Group 8 contains the fields: (4/4)(4/5)(5/4)(5/5)
Detected level size: 6x6
O X O O X X 
O X O X O O 
X O O X O O 
X O X O O X 
O O X O O X 
X X O X X O 
```
