x = 3
while x > 0:
    stevilka = raw_input("Vpisi stevilko:")
#odgovor = 10
    if stevilka == "10":
        print ("Cestitamo!!!! Uganili ste srecno stevilko!")
        break
    else:
        if x == "3":
            print("Poskusi ponovno. Imas se 2 poskusa")
        elif x == "2":
            print("Poskusi ponovno. Imas se 1 poskus")
        else:
            print ("Zal ni slo. Vec srece prihodnjic!")
    x = x - 1
