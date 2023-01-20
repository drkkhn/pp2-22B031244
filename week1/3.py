a, b, c = map(int, input().split(' '))

if c ** 2 == a ** 2 + b ** 2:
    print(f"""c is the triangle's hypotenuse
{a}² + {b}² = {c}² """)
else:
    print("c is not the triangle's hypotenuse")

