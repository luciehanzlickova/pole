pole = [5, 2, 8, 1, 9, 3]

print("delka poleje:", len(pole))

print("hodnoty v poli:")
for hodnota in pole:
    print(hodnota)

novy_prvek = int(input("zadejte novy prvek: "))
pole.append(novy_prvek)

odstranen = pole.pop(0)
print(f"odstraneny prvek: {odstranen}")

pole.sort()
print("serazeny pole:", pole)

pole.reverse()
print("vypis pole v obracenem poradi:")
for hodnota in pole:
    print(hodnota)