#include <iostream>
#include <iomanip>
#include <time.h> 

using namespace std;

template <typename T>
T sort(T* r, T size,T i, T j) {
    if (r[j] > r[j + 1]) {
        T temp = r[j];
        r[j] = r[j + 1];
        r[j + 1] = temp;
    }
    if (j < size - i - 1-1)
        sort(r,size,i,j+1);
    if (i < size - i-1)
        sort(r, size, i+1, j);
    return 0;
}
void reverse(int* r, const int size, const int cycle_size, int i) {
    int temp = r[i];
    r[i] = r[size - i - 1];
    r[size - i - 1] = temp;
    if (i < cycle_size-1)
        reverse(r, size, cycle_size, i + 1);
}
void Create(int* r, const int size,int i)
{
        r[i] = rand() / 100;
        if (i < size-1)
            Create(r, size, i + 1);
}
void Print(int* r, const int size, int i)
{
    cout << setw(4) << r[i] << " ";
    if (i < size-1)
        Print(r, size, i + 1);
    if (i == size-1 )
        cout << endl;
}
int main()
{
    setlocale(LC_CTYPE, "ukr");
    srand((unsigned)time(NULL));
    const int n = 10;
    int r[n];
    Create(r, n,0);
    cout << "початковий масив = ";
    Print(r, n,0);
    sort(r, n,0,0);
    reverse(r, n, n / 2 , 0);
    cout << "масив пiсля змiн = ";
    Print(r, n, 0);
    return 0;
}