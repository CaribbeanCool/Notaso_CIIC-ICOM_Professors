from bs4 import BeautifulSoup
import requests
import somethn


def comentarios(nombreDeProfe):
    dummy = nombreDeProfe.lower()
    nombreDeProfe = dummy.replace(" ", "-")
    link = f"https://notaso.com/professors/{nombreDeProfe}/"
    pageToScrape = requests.get(link)
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    losComentarios = soup.find_all("p", attrs={"class": "break-word"})
    comentarios = set()

    for q in losComentarios:
        for i in q:
            i = str(i)
            if i.startswith("<"):
                continue
            comentarios.add(i)

    #  printing the comments:
    for i in comentarios:
        print(i)
        print("================================"*2)


def busquedaDeProfes(departamento):
    somethn.clear()
    profeList = {}
    num = 1
    if departamento.lower() == "ciic":
        departamento = "ciencias-de-computadora"
    else:
        departamento = "ingenieria-de-computadoras"
    url = f"https://notaso.com/universities/urpm/{departamento}/"
    pageToScrape = requests.get(url)
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    queue = soup.find_all("b")
    nombresDeProfesores = set()

    for q in queue:
        for i in q:
            if i == "Marko  Schütz":  # test case 1
                i = "Marko Schütz"
                nombresDeProfesores.add(i)
            if i == "Gretchen Y Bonilla Carabal…":  # test case 2
                i = "Gretchen Y Bonilla Caraballo"
                nombresDeProfesores.add(i)
            nombresDeProfesores.add(i)

    for i in nombresDeProfesores:
        profeList.update({i: num})
        print(str(num) + ") ", i)
        num += 1

    coments = input("Quieres ver los comentarios de los profesores? (y/n) ")
    if coments.lower() == "y":
        index = int(input("Cual profesor? "))
        if index > len(profeList.items()):
            print("Ese numero excede el numero de profesores")
            elMenu()

        for key, value in profeList.items():
            if index == value:
                comentarios(key)
    else:
        elMenu()


def elMenu():
    somethn.clear()
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("\n                               !!!!!BIENVENIDO!!!!!               \n ")
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("////////////////////////////////////////////////////////////////////////////////////// \n")

    try:
        inp = input("CIIC o ICOM? ")
        if inp.lower() == "ciic" or inp.upper() == "CIIC":
            busquedaDeProfes(inp)
        elif inp.lower() == "icom" or inp.upper() == "ICOM":
            busquedaDeProfes(inp)
        else:
            print("Incorrect option, please try again")
            elMenu()
    except ValueError:
        elMenu()


elMenu()
