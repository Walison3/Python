# km > hm > dam > m > dm > cm > mm

m = float(input('Digite uma distância em metro: '))
km = m / 10**3
hm = m / 10**2
dam = m / 10**1
dm = m * 10*1
cm = m * 10*2
mm = m * 10*3
print(f'A medida de {m} metros corresponde a \n {km} km \n {hm} hm \n {dam} dam \n {dm} dm \n {cm} cm \n {mm} mm')