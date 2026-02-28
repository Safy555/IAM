# file: queens.py
# VUT FIT - [IAM] Logika úkol 1. - The Eight Queens Problem
# author: Jakub Králik <xkralij00>
# date: 28.2.2026

# usage: ${python_version} {this_file_name} {cheesboard_size} > {DIMACS_format_file}
# e.g. $python3 queens.py 8 > queens.in
# $minisat queens.in queens.out

import sys

def var_num(row: int, column: int, N: int):
    return (row - 1) * N + column

def at_leat_one(vars_list: list):
    return [vars_list]

def at_most_one(vars_list: list):
    clauses = []
    k = len(vars_list)
    for i in range(k):
        for j in range(i + 1, k):
            clauses.append([-vars_list[i], -vars_list[j]])
    return clauses

def exactly_one(vars_list: list):
    clauses = []
    clauses += at_leat_one(vars_list)
    clauses += at_most_one(vars_list)
    return clauses

def generate_clauses(N: int):
    clauses = []
    
    # exactly one queen in each row
    for row in range(1, N + 1):
        row_vars = [var_num(row, column, N) for column in range(1, N + 1)]
        clauses += exactly_one(row_vars)
    
    # exactly one queen in each column
    for column in range(1, N + 1):
        col_vars = [var_num(row, column, N) for row in range(1, N + 1)]
        clauses += exactly_one(col_vars)
    
    # at most one queen on each diagonal down-right --> row - column == const
    for d in range(-(N - 1), N):
        diag_vars = []
        for row in range(1, N + 1):
            column = row - d
            if 1 <= column <= N:
                diag_vars.append(var_num(row, column, N))
        if len(diag_vars) > 1:
            clauses += at_most_one(diag_vars)
    
    # at most one queen on each diagonal down-left --> row + column == const
    for d in range(2, N * 2 + 1):
        diag_vars = []
        for row in range(1, N + 1):
            column = d - row
            if 1 <= column <= N:
                diag_vars.append(var_num(row, column, N))
        if len(diag_vars) > 1:
            clauses += at_most_one(diag_vars)
            
    return clauses


def main():
    if len(sys.argv) != 2: 
        print("Usage: python queens.py N") # python queens.py 8 > queens.in
        
    N = int(sys.argv[1])
    num_vars = N * N
    clauses = generate_clauses(N)
    num_clauses = len(clauses)
    
    print(f"c N Queens problem with N = {N}")
    print(f"c Number of variables {num_vars} == (N * N)")
    print(f"p cnf {num_vars} {num_clauses}")
    for clause in clauses:
        print(" ".join(str(literal) for literal in clause), "0")

if __name__ == "__main__":
    main()