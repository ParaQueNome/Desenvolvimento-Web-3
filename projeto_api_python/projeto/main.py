import webbrowser
import Nasa

print("Bem vindo ao aplicativo de imagens da NASA!")
print('--------------------------------------------')
print('[1] - Busca por data (formato: YYYY-MM-DD)')
print('[2] - APOD do dia')
print('[0 - Sair]')

option = int(input("Escolha uma opção: "))
while option != 0:
    if option == 1:
        data = str(input('Informe a data(YYYY-MM-DD)'))

        # Crie uma instância da classe Nasa
        image = Nasa.Nasa()

        # Obtenha a explicação da imagem da NASA
        explanation = image.get_apod_by_date(data)["explanation"]
        img = image.get_apod_by_date(data)["url"]

        # Crie um arquivo HTML temporário com a explicação
        with open("temp.html", "w", encoding="utf-8") as f:
            f.write(f"<html><body>{explanation} <img src='{img}' alt='Imagem da NASA'></body></html>")
            

        # Abra o arquivo HTML no navegador padrão
        webbrowser.open("temp.html")
    
    elif option == 2:
        image = Nasa.Nasa()
        explanation = image.get_apod()["explanation"]
        img = image.get_apod()["url"]
        with open("temp.html", "w", encoding="utf-8") as f:
            f.write(f"<html><body>{explanation} <img src='{img}' alt='Imagem da NASA'></body></html>")
            

        
        webbrowser.open("temp.html")

    print('[1] - Busca por data (formato: YYYY-MM-DD)')
    print('[0 - Sair]') 
    option = int(input("Escolha uma opção: "))

del(image)