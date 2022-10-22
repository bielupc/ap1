#include <iostream>
#include <ostream>
using namespace std;

int convertir(int b, int n) { return n; }

bool creixent(int n) {
  // Retorna si té digits en ordre creixent en les posicions imparelles
  if (n > 10) {
    return n;
  } else {
    return n % 10 >= creixent(n / 100);
  }
}

bool decreixent(int n) { return true; }

bool es_creixent_decreixent(int b, int n) {
  n = convertir(b, n);
  return creixent(n) and decreixent(n);
}

int main() {
  int b, n;

  while (cin >> b >> n) {
    if (es_creixent_decreixent(b, n)) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}
