from yogi import read, tokens, scan

def main() -> None:
    y1 = read(int)
    y2 = read(int)

    country = scan(str)

    high_le1 = 0.0
    high_le2 = 0.0
    improv = 0.0
    best_country = country
    high_country1 = country
    high_country2 = country

    while country is not None:
        le1 = scan(float)
        le2 = scan(float)

        if le1 is not None and le2 is not None:

            improv_country = le2 - le1
            
            if le1 > high_le1:
                high_le1 = le1
                high_country1 = country

            if le2 > high_le2:
                high_le2 = le2
                high_country2 = country

            if improv_country > improv:
                improv = improv_country
                best_country = country

            country = scan(str)

    print(f"{high_country1} has the best life expectancy of {y1}.")
    print(f"{high_country2} has the best life expectancy of {y2}.")
    print(f"{best_country} has the best improvement.")

if __name__ == "__main__":
    main()
