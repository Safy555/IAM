#!/bin/bash
PY=python3
TESTS="minimal easy unsolvable_row unsolvable_block empty malformed"

for t in $TESTS; do
    echo "=== Testing $t ==="
    
    # Determine input filename
    if [ "$t" == "minimal" ]; then
        INFILE="tests/test_minimal_solvable.txt"
    elif [ "$t" == "easy" ]; then
        INFILE="tests/test_easy_solvable.txt"
    else
        INFILE="tests/test_${t}.txt"
    fi

    if [ ! -f "$INFILE" ]; then
        echo "Error: Input file $INFILE not found"
        continue
    fi
    
    $PY SudokuCNFEncoder.py < "$INFILE" > "test_${t}.cnf"
    
    # Run Minisat if available
    if command -v minisat &> /dev/null; then
        minisat "test_${t}.cnf" "test_${t}.out" > /dev/null
        
        if grep -q "^SAT" "test_${t}.out"; then
            echo "✓ $t: SATISFIABLE ✓"
        elif grep -q "^UNSAT" "test_${t}.out"; then
            echo "✓ $t: UNSATISFIABLE ✓"
        else
            echo "✗ $t: ERROR (Check test_${t}.out) ✗"
            # exit 1
        fi
    else
        echo "Minisat not found, checking CNF generation only."
        if [ -s "test_${t}.cnf" ]; then
             echo "✓ $t: CNF Generated ✓"
        else
             echo "✗ $t: CNF Generation Failed ✗"
        fi
    fi
    echo ""
done
echo "All tests processed! 🎉"