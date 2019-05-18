other={"city":"Москва","temperature":20}
print(other['city'])
other['temperature']=other['temperature']-5
print(other)
print(other.get('country'))
print(other.get('country','Россия'))
