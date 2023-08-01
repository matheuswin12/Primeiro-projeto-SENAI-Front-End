VRPESO1 = 2
VRPESO2 = 3
VRPESOS = VRPESO1+VRPESO2

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

vrMedia = ((nota1*VRPESO1)+(nota2*VRPESO2))/VRPESOS

print("Resultado da média: ", vrMedia)
