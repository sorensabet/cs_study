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

int* bin_addition(int A[], int B[], int n){
    int C[n+1] = {};
    int sum = 0;
    int carry = 0;

    for (int j = n; j >= 0; j--){
        if (j-1 >= 0){
            sum = A[j-1] + B[j-1];
        }else{
            sum = 0;
        }
        if (carry > 1){
            carry = 1;
        }

        if (sum + carry == 1){
            C[j] = 1;
        } else if (sum+carry == 2){
            C[j] = 0;
            carry += 1;
        } else if (sum + carry == 3){
            C[j] = 1;
            carry += 1;
        }

        cout << "j: " << j << endl;
        cout << "s: " << sum << endl;
        cout << "c: " << carry << endl;
        print_array(C, n);
        cout << endl;
    }

    cout << "The sum of the two arrays is: " << endl;
    print_array(C, sizeof(C)/sizeof(*C));

    return C;
}

int main()
{
    int a[] = {1};
    int b[] = {1};

    cout << "A: ";
    print_array(a, sizeof(a)/sizeof(*a));
    cout << "B: ";
    print_array(b, sizeof(b)/sizeof(*b));

    bin_addition(a,b, sizeof(a)/sizeof(*a));
}
