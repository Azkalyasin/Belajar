    
n = int(input('masukkan batas bilangan fibonaci: '))
def fibonaci (n):
  count = [0, 1] 
  while len(count) < (n):
     count.append(count[-2]+count[-1])
  return count
print ('fibonaci number are: ',fibonaci(n))
