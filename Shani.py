#Code Input
from re import A

print("Shani pass changer, Changes your pass to something secure")
usercode = input("Your Pass is: ")

#Code Desphyer

usercode = usercode.replace("a", "@")
usercode = usercode.replace("A", "@")
usercode = usercode.replace("I", "1")
usercode = usercode.replace("i", "!")
usercode = usercode.replace("b", "#")
usercode = usercode.replace("B", "#")
input(usercode)