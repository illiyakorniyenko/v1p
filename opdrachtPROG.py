cijferICOR = 7
cijferPROG = 8
cijferCSN = 7

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) /3
beloning =   (cijferICOR + cijferPROG + cijferCSN) *30
#print(beloning)

a = "mijn cijfers (gemiddeld een "
b = ") leveren een beloning van $"
c = " op!"

print(a + str(gemiddelde) + b + str(beloning) + c)
