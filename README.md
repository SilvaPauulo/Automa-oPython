# Automacao de Leitura de preenchimento de formulario

- Nesta resolução de problemas tinhamos um funcionario que gostaria de automatizar, o preenchimento de alguns formulario devido ser uma tarefa repetitiva.

 ## Resolução do problema:
 
- O seu problema era que todos os dias ele recebia uma planilha com inumeros produtos, e dessa planilha ele tinha que estar pegando informações de 15 colunas com as seguintes descrições.
  
  - Nome do produto
  - Descrição
  - Categoria
  - Código do produto	Peso (em kg)
  - Dimensões (L x A x P)
  - Preço
  - Quantidade em estoque
  - Data de validade
  - Cor
  - Tamanho	Material
  - Fabricante
  - País de origem
  - Observações
  - Código de barras
  - Localização no armazém

- Desses produtos ele tinha 3 paginas estaticas de preenchimento, ele tinha que inserir esses produtos e ir seguindo para as proximas etapas de preenchimento.  


# Resolução do problema

- Entrar na planilha
- Copiar informações de um compo e colar no seu campo correspondente
- Repetir esses passos para os outros campos até preencher campos daquela página
- clicar em proximo
- Repetir os mesmo passos e ir para a proxima pagina(pagina 2)
- Repetir os mesmo passps e finalizar o cadastro daquele produto e clicar em concluir.
- Clicar em ok, para finalr o processo
- Clicar no ok mais um vez na mensagem de confirmação de salvamento no banco de dados.
- Clicar em adicionar mais um e repetir o processo até finalizar a planilha de produtos.

# Bibliotecas para resolver o problemas

Segue algumas bibliotecas que utilizei para resolver o seguinte problema:

- PyAutoGUI(automação de clicks e teclados)
- Openpyxl (Para a automação e leitura de planilhas)
- mouseinfo (Para entender a posição do maouse)
 - Detalhes de uso, para poder usar a seguinte ferramenta use os steps abaixo:
 1. abra o terminal e digite python e da um enter.
 2. Apos o passo de cima digite o seguinte comando from mouseInfo import mouseinfo
 3. E feito o que esta acima digite o seguinte comando novamente mouseInfo(), ele vai abrir uma caixa com as informações de localização. lembrando que vai ter uma opção de delay de 3s você podera desmarcar se quiser.

