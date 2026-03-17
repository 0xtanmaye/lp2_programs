#include <iostream>

using namespace std;

void selectionSort(int* arr, int n) {
	for (int i = 0; i < n - 1; i++) {
		int minIndex = i;
		for (int j = i + 1; j < n; j++) {
			if (arr[j] < arr[minIndex]) {
				minIndex = j;
			}
		}
		int temp = arr[minIndex];
		arr[minIndex] = arr[i];
		arr[i] = temp;
	}
}

void printArray(int* arr, int n) {
	for (int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
}

int main() {
	int size;

	cout << "Enter the number of elements: ";
	cin >> size;

	int* arr = new int[size];

	for (int i = 0; i < size; i++) {
		cout << "Enter element " << (i + 1) << ": ";
		cin >> arr[i];
	}

	cout << "\n\nElements before sorting: \n";
	printArray(arr, size);

	selectionSort(arr, size);

	cout << "\n\nElements after sorting: \n";
	printArray(arr, size);
	cout << endl;

	delete[] arr;
	return 0;
}
