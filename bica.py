import math



def funcao (xo):
   return pow(xo,4) - 16

a = float(raw_input("Intervalo a: "))
b = float(raw_input("Intervalo b: "))
iteracao = float(raw_input("Iteracoes: "))


while (interacao != 0):
	if ((funcao (a) * funcao((a+b)/2)) > 0):
		a = (a+b)/2
		b=b
	elif ((funcao (b) * funcao((a+b)/2)) > 0):
		b = (a+b)/2
		a=a
	elif ((funcao ((a+b)/2)) == 0):
		print ("Raiz aproximada e" + str((a+b)/2))
		break
	iteracao = interacao -1 
print ("Raiz aproximada e " + str((a+b)/2))