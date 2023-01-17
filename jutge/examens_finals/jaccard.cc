#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
using namespace std;


double jaccard(const vector<int>& A, const vector<int>& B){
  int m = A.size();
  int n = B.size();
  int i=0, j=0;
  int c = 0;
  
  while (i < m and j < n){
    if (A[i] < B[j]){
      i++;
    }
    else if (B[j] < A[i]){
      j++;
    }
    else{
      c+=1;
      i++;
      j++;
    }
  }

  int res = c / (m + n) - c;

  return double(c)/double((m+n-c));
}


int main(){
  cout.setf(ios::fixed);
  cout.precision(3);
  int m1;
  while(cin >> m1){
    int m2;
    vector<int> A;
    vector<int> B;
    for (int i = 0; i < m1; i++)
    {
      int n;
      cin >> n;
      A.push_back(n);
    }

    cin >> m2;
    for (int j = 0; j < m2; j++)
    {
      int n;
      cin >> n;
      B.push_back(n);
    }
    cout << jaccard(A, B) << endl;
  }
}