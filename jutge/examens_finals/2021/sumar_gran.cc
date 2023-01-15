#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;



void change_lengths(string &x, string &y) 
{
  int diff = y.size() - x.size();
    
  string z(diff, '0');
    
  int i;
  for (i = 0; i < x.size(); i++)
    z.push_back(x[i]);
  x = z;
    
}

int convertir(char n){
    switch (n) {
        case '1':
            return 1;
            break;
        case '2':
            return 2;
            break;
        case '3':
            return 3;
            break;
        case '4':
            return 4;
            break;
        case '5':
            return 5;
            break;
        case '6':
            return 6;
            break;
        case '7':
            return 7;
            break;
        case '8':
            return 8;
            break;
        case '9':
            return 9;
            break;
        case 'A':
            return 10;
            break;
        case 'B':
            return 11;
            break;
        case 'C':
            return 12;
            break;
        case 'D':
            return 13;
            break;
        case 'E':
            return 14;
            break;
        case 'F':
            return 15;
            break;
        case 'G':
            return 16;
            break;
        case 'H':
            return 17;
            break;
        case 'I':
            return 18;
            break;
        case 'J':
            return 19;
            break;
        case 'K':
            return 20;
            break;
        case 'L':
            return 21;
            break;
        case 'M':
            return 22;
            break;
        case 'N':
            return 23;
            break;
        case 'O':
            return 24;
            break;
        case 'P':
            return 25;
            break;
        case 'Q':
            return 26;
            break;
        case 'R':
            return 27;
            break;
        case 'S':
            return 28;
            break;
        case 'T':
            return 29;
            break;
        case 'U':
            return 30;
            break;
        case 'V':
            return 31;
            break;
        case 'W':
            return 32;
            break;
        case 'X':
            return 33;
            break;
        case 'Y':
            return 34;
            break;
        case 'Z':
            return 35;
            break;
        default:
            return 0;
        } 
}


string traduir_invers(string n){
  if (n == "10") {
    return "A";
  } else if (n == "11") {
    return "B";
  } else if (n == "12") {
    return "C";
  } else if (n == "13") {
    return "D";
  } else if (n == "14") {
    return "E";
  } else if (n == "15") {
    return "F";
  } else if (n == "16") {
    return "G";
  } else if (n == "17") {
    return "H";
  } else if (n == "18") {
    return "I";
  } else if (n == "19") {
    return "J";
  } else if (n == "20") {
    return "K";
  } else if (n == "21") {
    return "L";
  } else if (n == "22") {
    return "M";
  } else if (n == "23") {
    return "N";
  } else if (n == "24") {
    return "O";
  } else if (n == "25") {
    return "P";
  } else if (n == "26") {
    return "Q";
  } else if (n == "27") {
    return "R";
  } else if (n == "28") {
    return "S";
  } else if (n == "29") {
    return "T";
  } else if (n == "30") {
    return "U";
  } else if (n == "31") {
    return "V";
  } else if (n == "32") {
    return "W";
  } else if (n == "33") {
    return "X";
  } else if (n == "34") {
    return "Y";
  } else if (n == "35") {
    return "Z";
  } else {
    return n;
  }

}

string suma(int b, string x, string y)
{
    // Agafem com a X el nombre més curt
    int len_x = x.length();
    int len_y = y.length();

    if (len_y < len_x){
        swap(x, y);
    }

    // Revertim els strings per sumar un a un
    reverse(y.begin(), y.end());

    // Afegim zeros perquè tinguin la mateixa longitud
    change_lengths(x, y);
    reverse(x.begin(), x.end());


    // Iterem, convertim, sumem un a un, anotem carry i suma total
    int c = 0;
    int carry = 0;
    int r = 0;
    string s = "";

    
    for (int i = 0; i < y.length(); i++)
    {
        r = (convertir(x[i]) + convertir(y[i]) + carry) % b;
        c = (convertir(x[i]) + convertir(y[i]) + carry) / b;
        carry = c;
        s += traduir_invers(to_string(r));
    }

    // si el carry també es diferent de zero l'afegim.
    if (carry != 0){
        s += traduir_invers(to_string(c));
    }

    // donem la volta a la suma
    reverse(s.begin(), s.end());

    return s;
}


int main() {
    int b;
    string x, y;
    while (cin >> b >> x >> y) {
        cout << suma(b, x, y) << endl;
    }
}
