#include <iostream>
using namespace std;

void table(int t) {
  for (int i = 1; i <= 10; i++) {
    cout << t << "*" << i << " = " << t * i << endl;
  }
}

int main() {
  int t;
  cin >> t;
  table(t);
}
