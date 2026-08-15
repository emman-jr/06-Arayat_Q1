zodiac_name=['Rat (鼠 / Shǔ)','Ox (牛 / Niú)','Tiger (虎 / Hǔ)','Rabbit (兔 / Tù)','Dragon (龙 / Lóng)','Snake (蛇 / Shé)','Horse (马 / Mǎ)','Goat (羊 / Yáng)','Monkey (猴 / Hóu)','Rooster (鸡 / Jī)','Dog (狗 / Gǒu)','Pig (猪 / Zhū)']
def zodiac_do(x):
    print(f"\nYou're Chinese Zodiac Sign is {zodiac_name[x]}")

while True:
    birth_y = int(input("Enter your birth year: "))-1900
    if birth_y >= 0:
        zodiac_do((birth_y)%12)
        input()
        break
    else:
        print("Year must be above or equal to 1900!")