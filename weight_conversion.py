#conversion from pounds to killos and vice versa

select = int(input("sellect if you want to convert from pounds to kilos type 1 if you want to convert from kilos to pounds 2 "))
weight = float(input("type weight that you want to convert: "))


if select == 1:
    equals = weight / 2.205
    print(f"{round(equals, 2)}kg")
elif select == 2:
    equals = weight * 2.205
    print(f"{round(equals, 2)}lb")
else:
    print(f"{select} is not an option")