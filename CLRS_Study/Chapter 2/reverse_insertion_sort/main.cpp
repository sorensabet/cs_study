#include <iostream>

using namespace std;

void print_array(int A[], int n){
    // Inputs:
    // A: The array to be printed
    // n: The length of the array

    for (int i = 0; i < n; i++){
        if (i != n - 1 ){
            cout << A[i] << ',';
        } else {
            cout << A[i] << endl;
        }
    }

}

void reverse_insertion_sort(int A[], int n){
    // Inputs
    //  A: The array to be sorted
    //  n: The length of the array
    // Returns: The array sorted in non-increasing order
    for (int j = 1; j < n; j++){
        int key = A[j];
        int i = j - 1;
        while (i >= 0 && A[i] < key){
            A[i+1] = A[i];
            A[i] = key;
            i = i - 1;
        }
    }
}

int main()
{
    int arr[] = {1,5,2,6,5,4,2};
    int len_arr = sizeof(arr)/sizeof(*arr);

    reverse_insertion_sort(arr, len_arr);
    print_array(arr, len_arr);

    return 0;
}
