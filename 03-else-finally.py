# In python we have different level of exception execution:
# except will handle all exception no matter it's type
# else: will only execute if there are no exceptions
# finally: will always execute
try:
    n1 = int(input("Ingresa primer número: "))
except Exception as e:
    print("Ocurrio un error!")
else:
    print("No ocurrió ningún error")
finally:
    print("se ejecuta siempre")
