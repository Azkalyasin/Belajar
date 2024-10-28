#nomor 1
evaluate = float(input('masukkan nilai evaluasi: '))
if evaluate >= 90:
    print ('excelent prformance')
elif evaluate >= 80:
    print ('very good performance')
elif evaluate >= 70:
    print('good performance')
elif evaluate >= 60:
    print('avg pervormance')
else:
    print ('bed perfomance')


#nomor 2
angka1 = int(input('masukkan angka1: '))
angka2 = int(input('masukkan angka2: '))
angka3 = int(input('masukkan angka3: '))

bilangan_terbesar = max(angka1,angka2,angka3)

print(f'bilangan terbesar adalah {bilangan_terbesar}')

#nomor 3

    
n = int(input('masukkan batas bilangan fibonaci: '))
a, b = 0, 1
print('deret fibonaci hingga',n,":")
while a <= n:
    print ( a , end = '')
    a, b = b, a + b 
    print("\n")

#nomor 4
sampai_bearpa = int(input('masukkan niali n: '))
for i in range(1,sampai_bearpa+1, 2):
    print(i, end='')
    print ("\n")

#nomor 5
n = int(input('masukkan jumlah: '))
for i in range(1, n+1):
    print(str(i) * i)