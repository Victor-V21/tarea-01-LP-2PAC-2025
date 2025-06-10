
# Declaración de funciones

def header():
    print("\nIngrese la operacion que desea realizar: ")
    print("\n\t1. Retiro")
    print("\n\t2. Realizar deposito")
    print("\n\t3. Consulta de saldo")
    print("\n\t4. Salir")
    pass

totalAmount = float(1500.00)
def withdrawMoney():
    global totalAmount
    removeQuantity = float(input("Ingrese la cantidad que desea retirar: "))

    if removeQuantity > totalAmount:
        print("Dinero insuficiente")
    else:
        totalAmount = totalAmount - removeQuantity
        print("Dinero retirado correctamente, recoja el dinero")
    pass

def depositMoney():
    global totalAmount
    depositQuantity = float(input("Ingrese la cantidad a depositar:"))

    totalAmount = totalAmount + depositQuantity
    pass

def consultAmount():
    global totalAmount
    print("Su cantidad de dinero es: ", totalAmount)
    pass

# Comienzo del programa

print("Bienvenido al ATM")

totalAmount = float(1500.00)
pointer = 1

while pointer<=3 and pointer>=1:
    header()
    pointer = int(input("Su selección: "))

    match pointer:
        case 1:
            print("Retirando dinero")
            withdrawMoney()
        case 2:
            print("Realizando deposito")
            depositMoney()
        case 3:
            print("Consultando saldo")
            consultAmount()
    
    input("Presione enter para continuar... ")

    pass
