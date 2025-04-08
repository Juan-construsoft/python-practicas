def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def insecure_eval(user_input):
    # Este uso de eval es inseguro y, por lo general, los analizadores lo reportan como vulnerabilidad
    return eval(user_input)

if __name__ == "__main__":
    print("Sum: ", add(5, 3))
    print("Subtract: ", subtract(5, 3))
    
    # Llamada a la función insegura con un string arbitrario
    resultado_inseguro = insecure_eval("5 + 10")
    print("Resultado inseguro: ", resultado_inseguro)
