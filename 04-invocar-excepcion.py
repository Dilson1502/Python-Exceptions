# let's make a function that validates if we are dividing by zero
# if input number is equal to 0 then we are gping to raise a ZeroDivisionError
# if there exist an error we are going to use a custom ZeroDivisionError
# to custom the output message, we have to define it inside the function definition, this in order to manipulate function parameters
def division(n=0):
    if n == 0:
        raise ZeroDivisionError(
            "No se puede dividir por 0", f"estas dividiendo por {n}")
    return 5/n


try:
    division()
except ZeroDivisionError as e:
    print(e)
