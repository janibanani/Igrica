x = 5
print x * 6

ime = "Jani"
priimek = "Bergant"

print ime + " je model!!!!!!!!!!!!!!!!!!!!!!!"

print "Moje ime je %s %s" % (ime, priimek)

print ("Moja ime in priimek sta" + " " + ime + " " + priimek)

ime = raw_input("Vpisi svoje ime: ")

if ime == "Jure" or "jure":
    print "Zivjo Jure"
elif ime=="Marko":
    print "Zivjo Marko"
else:
    print "Zivjo, ne vem kdo si"
    print "Prosim ce poves kdo si!!!!!!!!!!!!!"

odgovor = "ja"
while odgovor == "ja":
    ime = raw_input ("Vpisi svoje ime:")
    print ime
    odgovor = raw_input("Hoces nadaljevati?(ja/ne)")
while True:
    odgovor= raw_input ("hoces nadaljevati?: (da/ne)")
    if odgovor == "ne":
        break

print "koncal"

geslo = "mojegeslo"
x = 4
while x > 0:
    vpisano_geslo = raw_input("vpisi geslo")
    if (vpisano_geslo) == geslo:
        print "Bravo"
        break
    else:
        print "Napacno"
        x = x + 1



x = 12

if x = 12:
    print "Bravoooooo!!!!"
else:
    print "Poskusi ponovno naslednjic!"
