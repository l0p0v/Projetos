# FORCA

from selenium import webdriver
from selenium.webdriver.common.by import By
from unidecode import unidecode

# opções do navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# abrir navegador
navegador = webdriver.Chrome(options=options)
# gerar palavra
navegador.get('https://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1&fs2=0&Submit=Nova+palavra')
palavra = navegador.find_element(By.XPATH, '/html/body/center/center/table[1]/tbody/tr/td/div').text
# tirar acentos palavra
palavra = unidecode(palavra).lower()
# fechar navegador
navegador.quit()

# jogo
digitadas = []
erros = []
vidas = 6

while vidas > 0:
    letra = input('Digite uma letra: ').lower()[0]

    if letra in palavra:
        if digitadas.count(letra) == 0:
            print(f'wow, a letra "{letra}" existe na palavra secreta.')
            digitadas.append(letra)
        else:
            print(f'ops, a letra "{letra}" já foi dita, escolha uma diferente.\n')
            continue
    else:
        if letra not in erros:
            print(f'aff, a letra "{letra}" não existe na palavra secreta.')
            erros.append(letra)
            vidas -= 1
            print(f'\033[31mvidas: {vidas}\033[m\n')
        else:
            print(f'ops, a letra "{letra}" já foi dita, escolha uma diferente.\n')
        continue

    palavra_temp = ''
    for letra_temp in palavra:
        if letra_temp in digitadas:
            palavra_temp += letra_temp
        else:
            palavra_temp += '_'

    print(f'\033[32m{palavra_temp}\033[m', end='\n\n')
    if palavra_temp == palavra:
        print('\033[32mVocê conseguiu acertar a palavra. Parabéns!\033[m')
        break
else:
    print(f'\033[31mSuas chances acabaram. A palavra escolhida era "{palavra}"\033[m')
