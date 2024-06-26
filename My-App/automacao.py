import pyautogui
import openpyxl
import pyperclip #Utilizada para quando temos textos com caracteres especiais, lembrando que a bliblioteca do pygui não vai funcionar sobre os elemento com caracteres especiais.
from time import sleep

# - Entrar na planilha
wb = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = wb['Produtos']# Selecione a aba de Produtos:

# - Copiar informações de um compo e colar no seu campo correspondente
# Ou seja ele vai interar sobre as linhas da sheet_coluna apartir da linha 2.
# - Repetir esses passos para os outros campos até preencher campos daquela página
for linha in sheet_produtos.iter_rows(min_row=2): 

    nome_produto = linha[0].value
    #Isto vai colar o nome do produto !
    pyperclip.copy(nome_produto)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1116,369,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')
    
    descricao = linha[1].value
    #Isto vai colar o nome da descrição !
    pyperclip.copy(descricao)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1158,460,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    categoria = linha[2].value
    #Isto vai colar o nome da categoria !
    pyperclip.copy(categoria)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1150,586,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    codigo_do_produto = linha[3].value
    #Isto vai colar o nome da codigo_do_produto !
    pyperclip.copy(codigo_do_produto)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1186,675,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    peso_kg = linha[4].value
    #Isto vai colar o nome da peso !
    pyperclip.copy(peso_kg)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1154,763,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')
    
    dimensoes = linha[5].value
    #Isto vai colar o nome da dimensoes !
    pyperclip.copy(dimensoes)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1154,842,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    # - clicar em proximo
    # A automatização vai até o local do botão para fazer o click em proximo
    pyautogui.click(1135,906)
    sleep(2)


    # - Repetir os mesmo passos e ir para a proxima pagina(pagina 2)
    preco = linha[6].value
    #Isto vai colar o nome do preco !
    pyperclip.copy(preco)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1135,409,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    quantidade_em_estoque = linha[7].value
    #Isto vai colar o nome do quantidade !
    pyperclip.copy(quantidade_em_estoque)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1156,497,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    data_de_validade = linha[8].value
    #Isto vai colar o nome do data_de_validade !
    pyperclip.copy(data_de_validade)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1145,576,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    cor = linha[9].value
    #Isto vai colar o nome do cor !
    pyperclip.copy(cor)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1110,672,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    tamanho = linha[10].value
    #Isto vai colar o nome do tamanho !
    pyperclip.copy(tamanho)
    pyautogui.click(1112,755, duration=1)
    pequeno = 1204,786
    medio = 1193,809
    grande = 1169,820
    
    if tamanho == 'Pequeno':
        pyautogui.click(pequeno,duration=1)
    elif tamanho == 'Médio':
        pyautogui.click(medio,duration=1)
    else:
        pyautogui.click(grande,duration=1)

    material = linha[11].value
    #Isto vai colar o nome do material !
    pyperclip.copy(material)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1109,833,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    # - clicar em proximo
    # A automatização vai até o local do botão para fazer o click em proximo
    pyautogui.click(1138,897)
    sleep(2)

    fabricante = linha[12].value
    #Isto vai colar o nome do fabricante !
    pyperclip.copy(fabricante)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1111,426,duration=1)
    #Em seguida ele vai estar col1.67ando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    pais_origem = linha[12].value
    #Isto vai colar o nome do pais de origem !
    pyperclip.copy(pais_origem)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1162,511,duration=1)
    #Em seguida ele vai estar col1.67ando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    observacoes = linha[13].value
    #Isto vai colar o nome do observações !
    pyperclip.copy(observacoes)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1110,599,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')


    codigo_de_barras = linha[15].value
    #Isto vai colar o nome do codigo de barras !
    pyperclip.copy(codigo_de_barras)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1109,735,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    localizacao_armazem = linha[16].value
    #Isto vai colar o nome do local de armazem !
    pyperclip.copy(localizacao_armazem)
    #Vai clicar no campo com as seguintes coordenadas:
    pyautogui.click(1107,823,duration=1)
    #Em seguida ele vai estar colando a informação dentro do campo
    pyautogui.hotkey('ctrl','v')

    # - clicar em proximo
    # A automatização vai até o local do botão para fazer o click em proximo
    pyautogui.click(1130,878,duration=1)
    sleep(2)
    #confirmação banco de dados
    pyautogui.click(1624,183,duration=1)
    #Adicionar mais um !
    pyautogui.click(1463,635,duration=1)
# - Repetir os mesmo passos e finalizar o cadastro daquele produto e clicar em concluir.
# - Clicar em ok, para finalizar o processo
# - Clicar no ok mais um vez na mensagem de confirmação de salvamento no banco de dados.
# - Clicar em adicionar mais um e repetir o processo até finalizar a planilha.