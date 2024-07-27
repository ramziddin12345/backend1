maxfiy_raqam = 7

guesses = 0

for attempt in range(3):
    guess = int(input("1 dan 10 gacha raqamni taxmin qiling: "))
    guesses += 1
    if guess == maxfiy_raqam:
        print("Tabriklaymiz! Siz raqamni taxmin qildingiz!", guess)
        break
    elif guess < maxfiy_raqam:
        print("Yashirin raqam kattaroq.")
    else:
        print("Yashirin raqam kichkinaroq.")

print("O'yin tugadi!")