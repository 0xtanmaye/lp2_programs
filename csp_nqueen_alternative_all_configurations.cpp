#include <iostream>
#include <vector>

using namespace std;

bool solve_nqueen(bool **, int, int, vector<bool**>&);
bool isSafe(bool **, int n, int, int);
void print_board(bool **, int);

int main(void)
{
	vector<bool**> all_solutions;
	int n;
	cout<<"n: ";
	cin>>n;

	bool **board = new bool*[n];

	for (int i = 0; i < n; i++) {
		board[i] = new bool[n];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			board[i][j] = false;
		}
	}

	solve_nqueen(board, n, 0, all_solutions);

	for (int i = 0; i < all_solutions.size(); i++) {
		bool **solution = all_solutions[i];
		cout << "\nSolution " << (i + 1) << ": " << endl;
		print_board(solution, n);
	}

	// Clean up the dynamically allocated memory
	for (int i = 0; i < n; i++) {
		delete[] board[i];
	}
	delete[] board;

	for (int i = 0; i < all_solutions.size(); i++) {
		bool **solution = all_solutions[i];
		for (int i = 0; i < n; i++) {
			delete[] solution[i];
		}
		delete[] solution;
	}
	all_solutions.clear();
	
	return 0;
}

bool solve_nqueen(bool **board, int n, int col, vector<bool**> &all_solutions)
{
	if (col >= n) {
		bool **solution = new bool*[n];
		for (int i = 0; i < n; i++) {
			solution[i] = new bool[n];
			for (int j = 0; j < n; j++) {
				solution[i][j] = board[i][j]; // Copy the board to the solution
			}
		}
		all_solutions.push_back(solution);
		return false;
	}
	
	for (int row = 0; row < n; row++) {
		if (isSafe(board, n, row, col)) {
			// If current row, col combination is safe place the queen
			board[row][col] = true;

			// Recursively check the next col with the placed queen
			if (solve_nqueen(board, n, col + 1, all_solutions)) {
				return true;
			}

			// If the above recursive lookup doesn't return true
			// then current row and col combination is not the solution
			board[row][col] = false;
		}
	}

	return false;
}

// Check the upper/lower diagonal and horizontally left for queen
bool isSafe(bool **board, int n, int row, int col)
{
	// Check left horizontally
	for (int i = col; i >= 0; i--) {
		if (board[row][i]) {
			return false;
		}
	}

	// Check upper diagonal
	for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
		if (board[i][j]) {
			return false;
		}
	}

	// Check lower diagonal
	for (int i = row, j = col; i < n && j >= 0; i++, j--) {
		if (board[i][j]) {
			return false;
		}
	}

	return true;
}

// Print the board parsing the 'true' as queen 
void print_board(bool **board, int n)
{
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (board[i][j])
				cout << "Q ";
			else
				cout << ". ";
		}
		cout << endl;
	}
}
