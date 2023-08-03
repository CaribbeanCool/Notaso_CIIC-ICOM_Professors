from bs4 import BeautifulSoup
import requests
import somethn

# Helper function to process professor names


def verificacionNombreDeProfe(name):
    name = name.lower().replace(".", "").replace(
        "é", "e").replace("ü", "u").replace(" ", "-")
    return name


def comentarios(nombreDeProfe):
    dummy = nombreDeProfe.lower()
    test = dummy.replace(".", "")
    test2 = test.replace("é", "e")
    test3 = test2.replace("ü", "u")
    nombreDeProfe = test3.replace(" ", "-")
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


def notaDeProfesor(nombreDeProfe):
    dummy = nombreDeProfe.lower()
    test = dummy.replace(".", "")
    test2 = test.replace("é", "e")
    test3 = test2.replace("ü", "u")
    nombreDeProfe = test3.replace(" ", "-")
    link = f"https://notaso.com/professors/{nombreDeProfe}/"
    pageToScrape = requests.get(link)
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    nota = soup.find("p", attrs={"class": "professor-percent"})
    return nota.text


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
            if i == "Gretchen Y Bonilla Carabal…":  # test case 2
                i = "Gretchen Y Bonilla Caraballo"
            if i == "Pedro  Rivera Vega":
                i = "Pedro Rivera Vega"
            if i == "Amir  Chinaei":
                i = "Amir Chinaei"
            nombresDeProfesores.add(i)

    for i in nombresDeProfesores:
        profeList.update({i: num})
        print(str(num) + ") ", i + ": " + notaDeProfesor(i))
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
