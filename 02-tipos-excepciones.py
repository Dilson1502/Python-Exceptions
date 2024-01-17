# there are many exceptions depending on error type
# as ValueError or NameError
# even if user enter a number, me have and undefined variable
try:
    n1 = int(input("Ingresa primer número: "))
    dfdsfdsf
except ValueError as e:
    print("Ingrese un valor que corresponda")
except NameError as e:
    print("Ocurrio un error!")
