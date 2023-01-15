#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

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

int main(){
    string x = "233";
    string y = "BB";
    int b = 14;


    // Agafem com a X el nombre més curt
    int len_x = x.length();
    int len_y = y.length();

    if (len_y < len_x){
        swap(x, y);
    }

    // Afegim zeros perquè tinguin la mateixa longitud
    int diff = len_y - len_x;
    x.insert(0, diff, '0');

    // Revertim els strings per sumar un a un
    reverse(x.begin(), x.end());
    reverse(y.begin(), y.end());

    // Iterem, convertim, sumem un a un, anotem carry i suma total
    int c = 0;
    int carry = 0;
    int r = 0;
    string s = "";
    
    for (int i = 0; i < len_y; i++)
    {
        r = (convertir(x[i] + convertir(y[i])) + carry) % b;
        c = (convertir(x[i] + convertir(y[i])) + carry) / b;
        carry = c;
        s += to_string(r);
    }

    // si el carry també es diferent de zero l'afegim.
    if (carry != 0){
        s += to_string(c);
    }

    // donem la volta a la suma
    reverse(s.begin(), s.end());

    cout << s;
}

