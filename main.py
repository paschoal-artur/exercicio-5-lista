#Input para usuário digitar o valor que deseja converter
valor = float(input("Digite o valor em metros que deseja converter: "))

#Conversão de metros para centímetros = multiplicar o valor por 100
operação = float(valor * 100)

#Printando o valor de volta para o usuário
print("Em centímetros esse valor é " + str(operação) + ".")