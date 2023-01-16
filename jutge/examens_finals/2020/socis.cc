#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Data {
    int dia;
    int mes;
    int any;
};

void llegir_data(Data& data)
{
    int dia;
    cin >> dia;
    data.dia = dia;
    int mes;
    cin >> mes;
    data.mes = mes;
    int any;
    cin >> any;
    data.any = any;
}

struct Persona {
    string nom;
    int dni;
    Data naixament;
    string municipi;
};

void llegir_persona(Persona& persona)
{
    string nom; 
    cin >> nom;
    persona.nom = nom;

    int dni;
    cin >> dni;
    persona.dni = dni;

    llegir_data(persona.naixament);

    string municipi;
    cin >> municipi;
    persona.municipi = municipi;
}

struct Soci {
    int dni;
    bool junta;
    Data inscripcio;
};

void llegir_soci(Soci& soci)
{
    int dni;
    cin >> dni;
    soci.dni = dni;

    string junta;
    cin >> junta;
    if (junta == "S"){
        soci.junta = true;
    }
    else{
        soci.junta = false;
    }
    
    llegir_data(soci.inscripcio);
}

using Persones = vector<Persona>;

using Socis = vector<Soci>;

// Retorna el nombre de socis que siguin a la junta i
// visquin en un municipi donat i hagin nascut a
// l'any donat o més tard.
//
// Precondició: persones i socis ordenats per dni
//
int nombre_de_socis_joves_a_la_junta_en_un_municipi(const Persones& persones, const Socis& socis, int any, const string& municipi)
{
    int c = 0;
    int len_persones = persones.size();
    int len_socis = socis.size();

    for (int i = 0; i < len_persones; i++)
    {
        if (persones[i].municipi == municipi and persones[i].naixament.any >= any)
        {
            for (int j = 0; i < len_socis; j++)
            {
                if (socis[j].dni == persones[i].dni and socis[j].junta == true){
                    c+=1;
                    break;
                }
            }
        }
    }
    return c;
}

int main()
{
    // llegir persones
    int np;
    cin >> np;
    Persones persones(np);
    for (Persona& persona : persones) {
        llegir_persona(persona);
    }


    // llegir socis
    int ns;
    cin >> ns;
    Socis socis(ns);
    for (Soci& soci : socis) {
        llegir_soci(soci);
    }

    
    // llegir paràmetres
    int any;
    cin >> any;
    string municipi;
    cin >> municipi;

    // escriure el resultat
    cout << nombre_de_socis_joves_a_la_junta_en_un_municipi(persones, socis, any, municipi);
}