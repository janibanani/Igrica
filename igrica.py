x = 3
srecnast = 10
while x > 0:
    stevilka = raw_input("Vpisi stevilko:")
#odgovor = 10
    if stevilka == "10":
        print ("Cestitamo!!!! Uganili ste srecno stevilko!")
        break
    else:
        print ("Poskusi ponovno.")
        x = x - 1
print ("Zal ni slo. Vec srece prihodnjic!")