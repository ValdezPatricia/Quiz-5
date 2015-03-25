#Valdez,Patricia

def find_theres(x):
	suma = 0
	div = []
	for elemento in x:
		if(elemento % 3 == 0):
			suma = suma + elemento
	return suma
	
x =[0,2,7,3,6,9,12,5,15]
result = list(filter(lambda elemento: (elemento % 3 == 0), x))

print(find_theres(x), result)
