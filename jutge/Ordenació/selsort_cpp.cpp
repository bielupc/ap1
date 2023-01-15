#include <vector>
#include <iostream>
using namespace std;


void print_vector(const vector<double>& V){
  for (double x : V) cout << x << ", ";
}


void selsort(vector<double>& V){
  int len = int(V.size());
  for (int i = 0; i < len-1; i++)
  {
    // trobem el mínim a partir de la posició i
    int pos_min = i;
    for (int j = i+1; j < len; j++)
    {
      if (V[j] < V[pos_min]){
        pos_min = j;
      }
    }
    // swap de variables
    if (pos_min != i){
    int aux = V[i];
    V[i] = V[pos_min];
    V[pos_min] = aux;
    }
  }
  print_vector(V);
}


int main() 
{
  vector<double> V = {0,0, 0, 0, 4};
  selsort(V);
}