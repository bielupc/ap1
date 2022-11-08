#include <iostream>
using namespace std;

int  double_factorial(int x){
  int semifactorial = 1;

  for(int aux = x; aux >= 2; aux -= 2){
    semifactorial *= aux;
  }
  return semifactorial;
}


int main()
{
  int n;
  cin >> n;
  cout << double_factorial(n) << endl;

}
