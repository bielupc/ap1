#include <iostream>
using namespace std;

bool is_leap_year(int y) {
  if (y % 4 == 0 and y % 100 != 0 or y % 100 == 0 and (y / 100) % 4 == 0) {
    return true;
  } else {
    return false;
  }
}

int main() {
  int y;
  cin >> y;

  if (is_leap_year(y)) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
}
