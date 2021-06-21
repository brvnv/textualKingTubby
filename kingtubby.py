import sys
def vocalDub (dubplate):
    print(dubplate+dubplate[len(dubplate)-3:]*25)

def skankDub (dubplate):
    print(dubplate+dubplate[len(dubplate)-4:]*25)

def solomonDub(dubplate):
    print(dubplate+dubplate[len(dubplate)-2:]*25)

while True:
    userString=input("Digite uma frase ou /q para sair")
    if userString=="/q":
        sys.exit()
    elif len(userString)==5:
        skankDub(userString)
    elif len(userString)==3:
        solomonDub(userString)
    else:
        vocalDub (userString)