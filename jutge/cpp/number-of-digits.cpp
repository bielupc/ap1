#include <iostream>
using namespace std;

int numberOfDigits(int n) {
  if (n < 10) {
    return 1;
  } else {
    return 1 + numberOfDigits(n / 10);
  }
}

int main() {
  int n;
  cin >> n;
  cout << "The number of digits of " << n << " is " << numberOfDigits(n) << "."
       << endl;
}
