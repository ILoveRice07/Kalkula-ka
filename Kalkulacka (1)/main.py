print("Vítejte v programu kalkulačka.")

while True:
  print("Napište "'konec'" při vybírání operace pro ukončení programu.")
  operace=input("Vyberte si operaci- sčítání, odčítání, násobení, dělení, umocnění, odmocnění:")
  

  hodnota1=float(input("Zadej první číslo:"))
  hodnota2=float(input("Zadej druhé číslo:"))
  
  import math
  if operace == "odmocnění":
    print("Výsledek je:", math.sqrt(hodnota1))
  
  if operace == "sčítání":
    print("Výsledek je:", hodnota1+hodnota2)
  elif operace == "umocnění":
    print("Výsledek je:", hodnota1**hodnota2)
  elif operace == "odčítání":
    print("Výsledek je:", hodnota1-hodnota2)
  elif operace == "násobení":
    print("Výsledek je:", hodnota1*hodnota2)
  elif operace == "dělení" and hodnota2 == 0:
    print("Nulou nelze dělit")
  elif operace == "dělení":
    print (hodnota1/hodnota2)
  elif operace == "konec":
    print("Konec programu.")
    break
  