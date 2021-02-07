age = int(input('Hány éves vagy? '))

if age < 18:
  print('Sajnáljuk, de ez a cikk csak 18 éven felüliek számára érhető el.')
elif age == 18:
  print('Pont 18? Gratulálunk, üdv a felnőttek között! Jó szórakozást a cikkhez!')
else:
  print('Köszönjük! Elolvashatod ezt a cikket.')
