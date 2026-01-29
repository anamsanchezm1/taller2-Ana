def calculadora():
    print("=== Calculadora de Suma y Resta ===")
    
    while True:
        try:
            num1 = float(input("Ingresa el primer número: "))
            operacion = input("¿Qué operación deseas? (+, -): ")
            num2 = float(input("Ingresa el segundo número: "))
            
            if operacion == "+":
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}\n")
            elif operacion == "-":
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}\n")
            else:
                print("Operación no válida. Intenta de nuevo.\n")
                continue
            
            continuar = input("¿Deseas realizar otra operación? (s/n): ")
            if continuar.lower() != "s":
                print("¡Hasta luego!")
                break
                
        except ValueError:
            print("Error: Ingresa números válidos.\n")

if __name__ == "__main__":
    calculadora()