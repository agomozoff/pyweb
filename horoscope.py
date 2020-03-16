import random
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generated_prophecies():
    generated_prophecies = []
    i = 0
    while i < 5:
        generated_prophecies.append(times[random.randrange(0, len(times))].capitalize() + " " + advices[random.randrange(
            0, len(advices))] + " " + promises[random.randrange(0, len(promises))] + ".")
        i = i+1
    return generated_prophecies


# generated_prophecies()


def output_terminal():
    i = 0
    print("Вот что получилось:")
    while i < 5:
        print(i+1, generated_prophecies()[i])
        i = i+1


# output_terminal()

cyc = ['1', '2', '3', '4']
for i in range(len(cyc)):
    print(cyc[i])
