import random
# tady bude seznam s různým typem úloh
assignments = [1, 2, 3]
def main():
    print("""
    Vítejte v generátoru zadání úloh pro ZŠ!
    Vyberte všechny možnosti, které chcete zahrnout do svého zadání:
    [1]Měsíční příjem rodiny (dělení)
    [2] Druhá možnost
    [3] Třetí možnost
    """)
    while input("Generovat zadání?  ").lower() != "s":
        #spíš to bude chtít for cyklus
        if input("Vaše volba: ") == "1":
            pocet_zadani = int(input("Kolik toho bude, paninko? "))
            print (monthly_income(pocet_zadani))
        if  input("Vaše volba: ") == "2": #aby se netestovala jen jedna?
            print("Prošlo to")
            #pocet_zadani = int(input("Kolik toho bude, paninko? "))
            #pass  

def monthly_income(pocet_zadani=1):
    for zadani in range(pocet_zadani):
        income = random.randint(100000, 1000000)
        assignment = "Finanční příjem čtyřčlenné rodiny za 1. pololetí roku je {} Kč. Jaký je průměrný měsíční příjem?".format(income)
        
        print(income)
        average_monthly_income = income/6
        print(assignment)
        print(f"Průměrný měsíční příjem rodiny je: {average_monthly_income}")


if __name__ == "__main__":
    main()