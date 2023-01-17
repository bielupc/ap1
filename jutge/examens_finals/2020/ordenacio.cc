#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;


bool comprovar(string a, string b){
  if ((a[0] >= 'A' and a[0] <= 'Z') and (b[0] >= 'a' and b[0] <= 'z')){
    return true;
  } 
  else{
    if (a.size() > b.size()){
      return true;
    }
    else{
      if (a > b){
        return true;
      }
      else{
        return false;
      }
    }
  }
}

// procediment que cal implementar
void ordenar(vector<string>&paraules){
    
  for (int i = 1; i < paraules.size(); i++) {
    string pivot = paraules[i];
    int j = i - 1;

    while (comprovar(paraules[j], pivot) && j >= 0) {
      paraules[j + 1] = paraules[j];
      --j;
    }
    paraules[j + 1] = pivot;
  }
}

int main()
{
    // llegir paraules en un vector
    vector<string> paraules;
    {
        string paraula;
        while (cin >> paraula) {
            paraules.push_back(paraula);
        }
    }

    // ordenar el vector amb la funció que cal implementar
    ordenar(paraules);

    // escriure el vector
    for (const string& paraula : paraules) {
        cout << paraula << endl;
    }
}

