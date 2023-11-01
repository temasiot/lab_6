#include <iostream>
#include <iomanip>
#include <time.h> 
#include <windows.h>

using namespace std;

template <typename T>
T sort(T* r, T size) {
    for (int i = 0; i < size-1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (r[j] > r[j + 1]) {
                T temp = r[j];
                r[j] = r[j + 1];
                r[j + 1] = temp;
            }
        }
    }
    return 0;
}
void reverse(int* r, const int size, const int cycle_size) {
    for (int i = 0; i < cycle_size; i++) {
        int temp = r[i];
        r[i] = r[size-i -1];
        r[size - i -1] = temp;
    }
}
void Create(int* r, const int size)
{
    for (int i = 0; i < size; i++)
        r[i] = rand() / 100;
}
void Print(int* r, const int size)
{
    for (int i = 0; i < size; i++)
        cout << setw(4) << r[i] << " ";
    cout << endl;
}
int main()
{
    setlocale(LC_CTYPE, "ukr");
    srand((unsigned)time(NULL));
    const int n = 10;
    int r[n];
    Create(r, n);
    cout << "початковий масив = ";
    Print(r, n);
    sort(r, n);
    reverse(r, n, n/2);
    cout << "масив пiсля змiн = ";
    Print(r, n);
    return 0;
}