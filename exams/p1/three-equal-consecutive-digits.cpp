#include <iostream>
using namespace std;

int len(int n) {
  if (n < 10) {
    return 1;
  } else {
    return 1 + len(n / 10);
  }
}

bool three_equal_consecutive_digits(int n, int c, int l) {
  if (len(n) == 2) {
    return false;
  } else if (c == 3) {
    return true;
  } else {
    if (l == n % 10) {
      return three_equal_consecutive_digits(n / 10, c++, (n / 10) % 10);
    } else {
      return three_equal_consecutive_digits(n / 10, 1, (n / 10) % 10);
    }
  }
}

int main() {
  int n, c, l;
  while (cin >> n) {
    c = 0;
    l = n % 10;
    cout << three_equal_consecutive_digits(n, c, l);
  }
}
