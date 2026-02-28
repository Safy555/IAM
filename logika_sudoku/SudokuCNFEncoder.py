# file: SudokuCNFEncoder.py
# VUT FIT - [IAM] Logika úkol 1. - Sudoku (harder, bonus)
# author: Jakub Králik <xkralij00>
# date: 28.2.2026

# usage: see README.md

import sys

class SudokuCNFEncoder:
    def __init__(self, N: int = 9, block_size: int = 3):
        self.block_size = block_size
        self.N = N
        self.clauses = []
        
    def var(self, row: int, col: int, value: int):
        return 100 * row + 10 * col + value
    
    def add_clause(self, literals: list):
        self.clauses.append(list(literals))
        
    def add_exactly_one(self, literals: list):
        self.add_clause(literals)
        for i in range(len(literals)):
            for j in range(i + 1, len(literals)):
                self.add_clause([-literals[i], -literals[j]])
                
    def add_filled_cell(self, row: int, col: int, value: int):
        self.add_clause([self.var(row, col, value)])
        
    def encode_cells(self):
        for row in range(1, self.N + 1):
            for col in range(1, self.N + 1):
                literals = [self.var(row, col, value) for value in range(1 , self.N + 1)]
                self.add_exactly_one(literals)
                
    def encode_rows(self):
        for row in range(1, self.N + 1):
            for value in range(1, self.N + 1):
                literals = [self.var(row, col, value) for col in range(1 , self.N + 1)]
                self.add_exactly_one(literals)
    
    def encode_cols(self):
        for col in range(1, self.N + 1):
            for value in range(1, self.N + 1):
                literals = [self.var(row, col, value) for row in range(1 , self.N + 1)]
                self.add_exactly_one(literals)
                
    def encode_blocks(self):
        for block_row in range(0, self.N // self.block_size):
            for block_col in range(0, self.N // self.block_size):
                for value in range(1, self.N + 1):
                    block_cells = []
                    for row_offset in range(1, self.block_size + 1):
                        for col_offset in range(1, self.block_size + 1):
                            row = block_row * self.block_size + row_offset
                            col = block_col * self.block_size + col_offset
                            block_cells.append(self.var(row, col, value))
                    self.add_exactly_one(block_cells)
                    
    def encode_all(self):
        self.encode_cells()
        self.encode_cols()
        self.encode_rows()
        self.encode_blocks()
        
    def num_vars(self):
        max_var = max(abs(literal) for clause in self.clauses for literal in clause)
        return max_var
    
    def to_dimacs(self):
        print(f"p cnf {self.num_vars()} {len(self.clauses)}")
        for clause in self.clauses:
            print(" ".join(str(literal) for literal in clause), "0")
        
        
def read_cells(stdin):
    cells = []
    line_num = 0
    for line in stdin:
        line_num += 1
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 3:
            sys.stderr.write(f"Warning: Skipping invalid line {line_num}: '{line}' (expected 3 values)\\n")
            continue
        try:
            row, col, value = map(int, parts)
            cells.append((row, col, value))
        except ValueError:
            sys.stderr.write(f"Warning: Skipping invalid line {line_num}: '{line}' (values must be integers)\\n")
            continue
    return cells

def main():
    encoder = SudokuCNFEncoder(N=9, block_size=3)
    cells = read_cells(sys.stdin)
    
    for row, col, value in cells:
        encoder.add_filled_cell(row, col, value)
        
    encoder.encode_all()
    encoder.to_dimacs()

if __name__ == "__main__":
    main()
