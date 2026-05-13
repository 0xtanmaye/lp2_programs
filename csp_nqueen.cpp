#include <iostream>

using namespace std;

bool solve_nqueen(bool **, int, int);
bool isSafe(bool **, int n, int, int);
void print_board(bool **, int);

int main(void)
{
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

	if (solve_nqueen(board, n, 0)) {
		print_board(board, n);
	}

	// Clean up the dynamically allocated memory
	for (int i = 0; i < n; i++) {
		delete[] board[i];
	}
	delete[] board;

	return 0;
}

bool solve_nqueen(bool **board, int n, int col)
{
	if (col >= n) {
		return true;
	}
	
	for (int row = 0; row < n; row++) {
		if (isSafe(board, n, row, col)) {
			// If current row, col combination is safe place the queen
			board[row][col] = true;

			// Recursively check the next col with the placed queen
			if (solve_nqueen(board, n, col + 1)) {
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
