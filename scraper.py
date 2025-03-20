from bs4 import BeautifulSoup
import requests
import os


def clear():
    """
    Automatically clears the terminal screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    return ("   ")


def name_verification(name: str) -> str:
    """
    Function that verifies the professor's name\n
    Parameters:
        name (str): The name of the professor
    Returns:
        name (str): The name of the professor without any special characters
    """
    return (
        name.lower()
        .replace(".", "")
        .replace("é", "e")
        .replace("ü", "u")
        .replace(" ", "-")
    )


def comments(nombreDeProfe: str):
    """
    Function that scrapes the professor's comments, and displays them in the terminal screen\n
    Parameters:
        nombreDeProfe (str): The name of the professor
    """
    clear()
    print("===      COMENTARIOS      ===")
    print(f"PROFESOR: {nombreDeProfe}" + "\n")
    nombreDeProfe = name_verification(nombreDeProfe)
    link = f"https://notaso.com/professors/{nombreDeProfe}/"
    pageToScrape = requests.get(link)
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    losComentarios = soup.find_all("p", attrs={"class": "break-word"})
    losAutores = soup.find_all("h4", attrs={"class": "submited-by"})
    comentarios, autores = [], []

    for q in losComentarios:
        for i in q:
            i = str(i)
            if i.startswith("<"):
                continue
            comentarios.append(i)

    for i in losAutores:
        for j in i:
            j = str(j)
            autores.append(j)

    if comentarios:
        for i, comment in enumerate(comentarios, start=1):
            print(f"{i}. {comment}")
            print("-" * 50)
    else:
        print("No hay comentarios para este profesor.")

    # PROMPT TO RETURN TO MENU
    print("\n")
    while True:
        try:
            inp = input("Quieres regresar al menu? (y/n) ")
            if inp.lower() == "y":
                menu()
            elif inp.lower() == "n":
                clear()
                exit()
            else:
                print("Ingresa una opcion valida.")
                continue
        except ValueError:
            print("Ingresa una opcion valida.")
            continue


def professor_grade(nombreDeProfe: str) -> str:
    """
    Function that scrapes the professor's rating\n
    Parameters:
        nombreDeProfe (str): The name of the professor
    Returns:
        nota.text (str): The professor's rating
    """
    nombreDeProfe = name_verification(nombreDeProfe)
    link = f"https://notaso.com/professors/{nombreDeProfe}/"
    pageToScrape = requests.get(link)
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    nota = soup.find("p", attrs={"class": "professor-percent"})
    return nota.text


def display_professor_info(profeList):
    """
    Function that displays the professor's name and rating\n
    Parameters:
        profeList (dict): The dictionary containing the professor's name and rating
    """
    print("Num.  Profesor                    Nota")
    print("----------------------------------------------")

    for i, (professor, _) in enumerate(profeList.items(), start=1):
        nota = professor_grade(professor)
        print(f"{i:>3}.  {professor:<30} {nota}")


def professor_search(departamento: str):
    """
    Function that scrapes the professor's name and rating, and displays them in the terminal screen\n
    Parameters:
        departamento (str): The department that the user chooses
    """
    clear()
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

    profeList = {i: num for num, i in enumerate(nombresDeProfesores, start=1)}
    display_professor_info(profeList)

    coments = input("Quieres ver los comentarios de los profesores? (y/n) ")

# After getting the user's choice about viewing comments
    if coments.lower() == "y":
        while True:
            try:
                index = int(input("Cual profesor? "))
                if index <= len(profeList):
                    break
                else:
                    print("Ese numero excede el numero de profesores")
            except ValueError:
                print("Ingresa un numero valido.")
                continue

        for key, value in profeList.items():
            if index == value:
                comments(key)
    else:
        menu()


def menu():
    """
    Function that displays the main menu
    """
    clear()
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("\n                               !!!!!BIENVENIDO!!!!!               \n ")
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("////////////////////////////////////////////////////////////////////////////////////// \n")

    try:
        inp = input("Selecciona un departamento ('CIIC' or 'ICOM'): ")
        if inp.lower() == "ciic" or inp.upper() == "CIIC":
            professor_search(inp)
        elif inp.lower() == "icom" or inp.upper() == "ICOM":
            professor_search(inp)
        else:
            print("Incorrect option, please try again")
            menu()
    except ValueError:
        menu()


if __name__ == "__main__":
    menu()
