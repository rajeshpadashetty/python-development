class werehouse:
    purpose="storage of goods"
    area="west"
w1=werehouse()
print(w1.purpose)
w2=werehouse()
w2.area="east"
print(w2.area)
w3=werehouse()
w3.purpose="cold weight"
print(w3.purpose)
print(w1.purpose,w2.area,w3.purpose)