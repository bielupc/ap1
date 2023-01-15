#include <iostream>
#include <vector>
using namespace std;


int position(double x, const vector<double>& v, int left, int right){
  if (right >= left){
    int i = (left + right) / 2;
    if (v[i] == x)
    {
      return i;
    }
    else{
      if (x < v[i]){
        return position(x, v, left, i-1);
      }
      else {
        return position(x, v, i+1, right);
      }
    }
 }
 return -1;
}


int main(){
  vector<double> llista = {1, 2, 4, 5, 7, 9};

  int right = int(llista.size()) - 1;
  int x = 7;
  int left = 0;

  cout << position(x, llista, left, right)<< endl;
}