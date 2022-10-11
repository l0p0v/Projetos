# JOGO DA FORCA

from selenium import webdriver
from selenium.webdriver.common.by import By
from unidecode import unidecode  # remover acento da palavra

# opções do navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# abrir navegador
navegador = webdriver.Chrome(options=options)
# gerar palavra
navegador.get('https://www.palavrasque.com/palavra-aleatoria.php?Submit=Nova+palavra')
palavra = navegador.find_element(By.XPATH, '/html/body/center[2]/font/font/b').text
# formatar a palavra
palavra_backup = palavra.strip().lower()
palavra = unidecode(palavra).strip().lower()
# fechar navegador
navegador.quit()

# jogo
digitadas = []
erros = []
chances = 6

while chances > 0:
    letra = input('Digite uma letra: ').lower()

    if letra:
        letra = letra[0]
    else:
        continue

    if letra in palavra and digitadas.count(letra) == 0:
        print(f'\033[32mwow, a letra "{letra}" exista na palavra secreta.\033[m')
        digitadas.append(letra)
    elif letra not in erros:
        print(f'\033[31maff, a letra "{letra}" não existe na palavra secreta.\033[m')
        chances -= 1
        erros.append(letra)
    else:
        print(f'\033[33mops, a letra "{letra}" já foi dita, escolha uma diferente.\033[m')
    print(f'você ainda tem {chances} chances.')

    palavra_temp = ''

    for letra_temp in palavra:
        if letra_temp in digitadas:
            palavra_temp += letra_temp
        else:
            palavra_temp += '_'

    print(f'a palavra secreta está assim: \033[1;7m{palavra_temp}\033[m\n')

    if palavra_temp == palavra:
        print(f'\033[1;32mVocê conseguiu acertar a palavra! A palavra secreta era "{palavra_backup}"\033[m')
        break
else:
    print(f'\033[1;31mSuas chances acabaram. A palavra secreta era "{palavra_backup}"\033[m')
