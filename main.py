from random import randint

random = randint(1, 100)
guess = 0

while True:
    guess += 1
    number = int(input('1-100 arası sayı giriniz :  '))
    if (number==0):
        print("Oyun sona erdi!")
        break

    elif number < random:
        print("Daha büyük bir sayı gir.")
        continue

    elif number > random:
        print("Daha küçük sayı gir.")
        continue

    else:
        print("\n\n Seçilen sayı {0} sayısıydı." .format(random))
        print("\n Tahmin sayınız : {0}" .format(guess))
        break

#Bitti!