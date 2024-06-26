# 1. O Usuario vai ter que abrir o navegador.
# 2. O usuario vai identificar a caixa de pesquisa
# 3. O usuario vai digitar a sua pesquisa na caixa de pesquisa pela url:
    #https://lna.roglobal.com/
# 4. Dentro do site o usuario vai clicar no botão com seguinte selector:
    #root > div > div > div.swiper.swiper-initialized.swiper-vertical.swiper-autoheight.index-module__homeSwiper___-qv3f.swiper-backface-hidden > div > div.swiper-slide.swiper-slide-active > div > div.btn-container > div:nth-child(2) > a:nth-child(1) > img
# 5. Quando ele clicar o arquivo ja vai estar baixando ele vai precisar acessar o seu computador na pasta:
  #Downloads
# 6. Vai clicar no item ira ser baixado e então severa ser aberto o diretorio downloads mostrando o arquivo.


# Configurar as opções do Chrome
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# # chrome_options.add_argument("--headless")  # Comentar essa linha para abrir o navegador normalmente
# chrome_options.add_argument("--window-size=1920,1080")






# 5. Verificar se o arquivo está sendo baixado na pasta Downloads
# downloads_folder = os.path.expanduser("~") + "/Downloads"
# wait = WebDriverWait(driver, 10)
# file_found = False
# for filename in os.listdir(downloads_folder):
#     if filename.endswith(".pdf") or filename.endswith(".xlsx") or filename.endswith(".docx") or filename.endswith(".exe"):
#         file_found = True
#         break
# if file_found:
#     print(f"O arquivo foi baixado com sucesso na pasta Downloads.")

#     # 6. Acessar o diretório de downloads e abrir o arquivo
#     download_path = os.path.join(downloads_folder, filename)
#     os.startfile(download_path)
# else:
#     print("O arquivo não foi encontrado na pasta Downloads.")

# # Fechar o navegador
# driver.quit()