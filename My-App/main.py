# from selenium import webdriver
# import os
# import time
# # automatização de downloads
# # from selenium.webdriver.chrome.service import Service

# # # 1. Abrir o navegador
# driver = webdriver.Edge()




# # # 2. Ir para a URL da pesquisa
# ragnarok = 'https://lna.roglobal.com/'
# driver.get(f'{ragnarok}')
# log = driver.get_log('browser')
# print(f'abrindo e acessando o navegador .....{log}')



# # Clicar no botão de Download
# seletor_do_botao = 'root > div > div > div.swiper.swiper-initialized.swiper-vertical.swiper-autoheight.index-module__homeSwiper___-qv3f.swiper-backface-hidden > div > div.swiper-slide.swiper-slide-active > div > div.btn-container > div:nth-child(2) > a:nth-child(1) > img'
# driver.find_element(By.ID).SELECTOR, seletor_do_botao)


# # # 3.Clicar no notão download
# # try:
# #     clickNoBotaoDownload = driver.find_element(By.CSS_SELECTOR, site)
# #     clickNoBotaoDownload.click()
# #     print(f'O botão download foi clicado !\nComeçando Download...') 
     
# # except:
# #     print(f'Botão não acionado verifique o nome do selector no back-end.')

# # 4. Verificar se o arquivo está sendo baixado na pasta Downloads
# # downloads_folder = os.path.expanduser("~") + "/Downloads"
# # wait = WebDriverWait(driver, 10)
# # file_found = Falses
# # for filename in os.listdir(downloads_folder):
# #     if filename.endswith(".pdf") or filename.endswith(".xlsx") or filename.endswith(".docx") or filename.endswith(".exe"):
# #         file_found = True
# #         break
# # if file_found:
# #     print(f"O arquivo foi baixado com sucesso na pasta Downloads.")

# #     # 5. Acessar o diretório de downloads e abrir o arquivo
# #     download_path = os.path.join(downloads_folder, filename)
# #     os.startfile(download_path)
# # else:
# #     print("O arquivo não foi encontrado na pasta Downloads.")

# # 6. Fechar o navegador

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.service import Service

# Esta linha vai instalar a versão mais recente do google:
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)