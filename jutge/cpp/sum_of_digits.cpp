#include <iostream>
#include <string>
using namespace std;

int sum_of_digits(int n) {
  if (n < 10) {
    return n;
  } else {
    return (n % 10) + sum_of_digits(n / 10);
  }
}

int main() {
  int n;
  while (cin >> n) {
    cout << "The sum of the digits of " << n << " is " << sum_of_digits(n)
         << "." << endl;
  }
}
