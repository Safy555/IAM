PYTHON = python3
SCRIPT = SudokuCNFEncoder.py

all: test

run:
	$(PYTHON) $(SCRIPT) < sudoku_input.txt > sudoku.cnf
	@echo "Generated sudoku.cnf"

test:
	chmod +x run_tests.sh
	./run_tests.sh

clean:
	rm -f *.cnf *.out
	rm -rf __pycache__
	rm -f tests/*.cnf tests/*.out

.PHONY: all run test clean
