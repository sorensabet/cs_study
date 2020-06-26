#include <iostream>

using namespace std;

void print_array(int A[], int n){
    for (int i = 0; i < n; i++){
        if (i != n - 1 ){
            cout << A[i] << ",";
        } else {
            cout << A[i] << endl;
        }
    }
}

int* selection_sort(int A[], int n){

    for (int i = 0; i < n; i++){
        int curr = A[i];
        int smallest_idx = i;
        for (int j = i + 1; j < n; j++){
            if (A[j] < A[smallest_idx]){
                smallest_idx = j;
            }
        }
        A[i] = A[smallest_idx];
        A[smallest_idx] = curr;
    }

    print_array(A, n);

    return A;
}

int main()
{
    int A[] = {42, 9, 17, 54, 602, -3, 54, 999, -11};
    int n = sizeof(A)/sizeof(*A);

    print_array(A,n);
    selection_sort(A, n);

    return 0;
}
