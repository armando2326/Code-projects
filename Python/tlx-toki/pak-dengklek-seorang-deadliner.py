sisa = int(input())

#hitung jam, menit, detik
jam = int(sisa/3600)
menit = int((sisa%3600)/60)
detik = (sisa%3600)%60

#print output
print(jam)
print(menit)
print(detik)