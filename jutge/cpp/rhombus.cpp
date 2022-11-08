#include <iostream>
using namespace std;

void rhombus(int n) {

  for (int i = 1; i <= n; i += 1) {
    for (int t = 0; t < n - i; t++) {
      cout << " ";
    }
    for (int j = 1; j <= (2 * i) - 1; j++) {
      cout << "*";
    }
    cout << endl;
  }
  for (int i = n - 1; i > 0; i--) {
    for (int t = 0; t < n - i; t++) {
      cout << " ";
    }
    for (int j = 1; j <= (2 * i) - 1; j++) {
      cout << "*";
    }
    cout << endl;
  }
}

int main() {
  int n;
  cin >> n;
  rhombus(n);
}
