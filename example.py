def greet(name: str) -> str:
    return f"Здравей, {name}! 👋"

# this is function for adding two numbers
def sum_numbers(a: float, b: float) -> float:
    return a + b


#creating conflict here
#creating conflict here 2
def main():
    #test
    #test
    #test
    print("=== Примерна Python програма ===")
    
    name = input("Как се казваш? ")
    print(greet(name))

    x = float(input("Въведи число X: "))
    y = float(input("Въведи число Y: "))

    result = sum_numbers(x, y)
    print(f"Сборът на {x} + {y} = {result}")


if __name__ == "__main__":
    main()
