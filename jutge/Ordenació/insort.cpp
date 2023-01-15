#include <iostream>
#include <vector>
using namespace std;

void print_vector(const vector<double>& V){
  for (double x : V) cout << x << ", ";
}

void insertion_sort_meu(vector<double>& v){
  int len = int(size(v));
  for (int i = 1; i < len ; i++)
  {
    double pivot = v[i];
    int j = i;
    while (j > 0 and v[j-1] > pivot)
    {
      v[j] = v[j-1];
      j--;
    }
    v[j] = pivot;
  }

}



int main()
{
  vector<double> v = {11, 12, 13, 5, 6};
  insertion_sort(v);

}