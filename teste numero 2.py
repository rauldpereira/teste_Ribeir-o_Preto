def vericar(x):
    a = 0
    b = 1
    if x == a or x == b:
        return print(f"O Numero {x} foi encontrado na sequencia de Fibonacci!")
    while b <= x:
        a, b = b, a + b

        if b == x:
            return print(f"O Numero {x} foi encontrado na sequencia de Fibonacci!")
        
    return print(f"O numero {x} nao foi encontrado na sequencia de Fibonacci!")

numero = int(input("digite um numero que deseja saber se pertence a sequencia de Fibonacci: "))

vericar(numero)