# Criador de Estrutura de Projeto

Este é um aplicativo de interface gráfica simples que permite criar estruturas de diretórios e arquivos a partir de uma definição YAML.

## Funcionalidades

- Interface gráfica amigável usando Tkinter
- Criação de estruturas de diretórios e arquivos baseada em YAML
- Seleção de diretório de destino através de um explorador de arquivos
- Feedback de status para o usuário

## Requisitos

- Python 3.x
- Biblioteca PyYAML

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Instale a biblioteca PyYAML executando o seguinte comando no PowerShell:


## Tutorial: Como Usar o Criador de Estrutura de Projeto

### Passo 1: Iniciar o Aplicativo

1. Abra o PowerShell.
2. Navegue até o diretório onde o arquivo `run.py` está localizado.
3. Execute o comando:
   ```
   python run.py
   ```

### Passo 2: Interface do Aplicativo

Após iniciar o aplicativo, você verá uma janela com os seguintes elementos:
- Uma área de texto para colar a estrutura YAML
- Um campo de entrada para o diretório de destino
- Um botão "Selecionar Pasta"
- Um botão "Criar Estrutura do Projeto"
- Uma área de status na parte inferior

### Passo 3: Inserir a Estrutura YAML

Cole a seguinte estrutura YAML na área de texto:

```yaml
meu_projeto:
  src:
    main.py:
    utils:
      helpers.py:
  docs:
    README.md:
  tests:
    test_main.py:
  config:
    settings.yaml:
``` 

### Passo 4: Selecionar o Diretório de Destino

Clique no botão "Selecionar Pasta".
Escolha o diretório onde deseja criar a estrutura do projeto.

### Passo 5: Criar a Estrutura do Projeto

Clique no botão "Criar Estrutura do Projeto".
O aplicativo criará a estrutura de diretórios e arquivos baseada na YAML fornecida.

### Passo 6: Verificar o Progresso

1. Verifique a mensagem de status na parte inferior da janela. Deve dizer "Estrutura do projeto criada com sucesso!".
2. Abra o Explorador de Arquivos e navegue até o diretório que você selecionou.

### Exemplo de Saída

Após a execução, o diretório `meu_projeto` será criado com a seguinte estrutura:

```yaml
meu_projeto/
│
├── src/
│   ├── main.py
│   └── utils/
│       └── helpers.py
│
├── docs/
│   └── README.md
│
├── tests/
│   └── test_main.py
│
└── config/
    └── settings.yaml
```

### Dicas Adicionais

1. Certifique-se de que o YAML está formatado corretamente. Use espaços para indentação, não tabulações.
2. Os diretórios são representados por chaves que contêm outras chaves ou valores nulos.
3. Os arquivos são representados por chaves com valores nulos.
4. Se ocorrer algum erro, verifique a mensagem de status para obter mais informações.

Com este tutorial, você deve ser capaz de usar o Criador de Estrutura de Projeto para gerar rapidamente estruturas de diretórios e arquivos baseadas em definições YAML.
