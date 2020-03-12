# # def Factorial(x):
# #     print("X:",x)
# #     if x == 1:
# #         return 1
# #     else:
# #         resultado = Factorial(x-1) * x
# #         print("X: {} Resultado: {}".format(x,resultado))
# #         return resultado
# vector = [0,1,2,6,4,5]

# def forSimulado(vector,cont):
#     if cont == len(vector)-1:
#         return vector[cont]
#     else:
#         print("X: ",vector[cont])
#         return vector[cont] + forSimulado(vector,cont+1)

# def buscarNumeroMayor(vector,cont,numMayor,pos):
#     if cont == len(vector):
#         return numMayor,pos
#     else:
#         if numMayor < vector[cont]:
#             numMayor = vector[cont]
#             pos = cont
#         return buscarNumeroMayor(vector,cont+1,numMayor,pos)

# # for x in range(len(vector)):
# #     print("x:",vector[x])

# print("----------------------")
# print(forSimulado(vector,0))
# print("----------------------")
# print(buscarNumeroMayor(vector,0,-9999,-1))
# # print(fib(10))

# # print("Factorial:",Factorial(5))

# # acum = 1
# # numero = int(input("Ingrese un numero"))
# # for x in range(1,numero+1):
# #     acum = acum*x

# # print(acum)

# # forSimulado(vector,0)

# # for x in range(len(vector)):
# #     print("x:",vector[x])


# # for x in range(5,0,-1):
# #     print(x)

matriz = [[1,2,3],[4,5,6],[7,8,9]]



for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        print(matriz[x][y])
        adyacentes = []
        for x1 in range(x-1,x+2):
            for y1 in range(y-1,y+2):
                if x1 >= 0 and x1 < len(matriz) and y1 >=0 and y1 <len(matriz):
                    if x == x1 and y == y1:
                        pass
                    else:
                        adyacentes.append(matriz[x1][y1])
        print("Adyacentes: ", adyacentes )
# 1 2 3
# 4 5 6
# 7 8 9