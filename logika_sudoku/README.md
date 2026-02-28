# Sudoku CNF Encoder

This project implements a Sudoku to CNF (Conjunctive Normal Form) encoder. It takes a Sudoku puzzle as input and generates a DIMACS CNF formula that can be solved by a SAT solver (like MiniSat).

## Prerequisites

- **Python 3**: Required to run the encoder script.
- **MiniSat** (Optional but recommended): Required for the test script to verify satisfiability.

## Project Structure

- `SudokuCNFEncoder.py`: The main Python script that encodes Sudoku puzzles.
- `run_tests.sh`: A shell script to run automated tests.
- `tests/`: Directory containing test input files.
- `sudoku_input.txt`: A sample input file.

## How to Run

### Using Make

To run the program with the default `sudoku_input.txt`:

```bash
make run
```

This will generate `sudoku.cnf`.

### Manual Execution

You can run the script manually by redirecting input and output:

```bash
python3 SudokuCNFEncoder.py < input_file.txt > output.cnf
```

## How to Test

The project includes a test suite that checks various scenarios (easy, minimal, unsolvable, etc.).

### Using Make

To run the full test suite:

```bash
make test
```

### Manual Execution

Ensure the script is executable and run it:

```bash
chmod +x run_tests.sh
./run_tests.sh
```

## Cleaning Up

To remove all generated `.cnf` and `.out` files:

```bash
make clean
```
