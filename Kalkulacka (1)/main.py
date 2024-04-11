print("Vítejte v programu kalkulačka.")

while True:
  print("Napište "'konec'" při vybírání operace pro ukončení programu.")
  operace=input("Vyberte si operaci- sčítání, odčítání, násobení, dělení, umocnění, odmocnění:")
  
  hodnota1=float(input("Zadej první číslo:"))
  hodnota2=float(input("Zadej druhé číslo:"))

  def sčítání(hodnota1, hodnota2):
   print("Výsledek je:", hodnota1+hodnota2)

  def umocnění(hodnota1, hodnota2):
   print("Výsledek je:", hodnota1**hodnota2)

  def odčítání(hodnota1, hodnota2):
   print("Výsledek je:", hodnota1-hodnota2)

  def násobení(hodnota1, hodnota2):
    print("Výsledek je:", hodnota1*hodnota2)
  
  def dělení(hodnota1, hodnota2):
    print("Výsledek je:", hodnota1/hodnota2)

  import math

  def odmocnění(hodnota1):
    print("Výsledek je:", math.sqrt(hodnota1))

  if operace == "odmocnění":
    odmocnění(hodnota1)
  
  if operace == "sčítání":
    sčítání(hodnota1, hodnota2)
  elif operace == "umocnění":
    umocnění(hodnota1, hodnota2)
  elif operace == "odčítání":
    odčítání(hodnota1, hodnota2)
  elif operace == "násobení":
    násobení(hodnota1, hodnota2)
  elif operace == "dělení" and hodnota2 == 0:
    print("Nulou nelze dělit")
  elif operace == "dělení":
    dělení(hodnota1, hodnota2)
  elif operace == "konec":
    print("Konec programu.")
    break
  