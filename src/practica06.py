#!/src/bin/python
PI=3.1415926535897931159979634685441852

def aproximacion(n):
  if(n!=0):
   suma=0
   for i in range(1,n+1):
     x_i=(i-0.5)/float(n)
     fx_i=4/(1+x_i**2)
     b=i/float(n)
     a=b-(1/float(n))
     suma=suma+fx_i
   pi=suma/n
   return pi
     
n= int(raw_input('Introduce el numero de intervalos: '))
m=int(raw_input('Introduce el numero de veces que quiera que se repita la funcion: '))
l=[]
print aproximacion(n)
for j in range(1, m+1):
  pi=aproximacion(j*m)
  l=l+[pi]
print l

