## Execução do projeto

## Utilizando o Prompt de Comando:
Abra o Prompt de Comando digitando “cmd” na caixa de pesquisa do menu Iniciar.
```bash
Digite “python –version” e pressione Enter.
```
O prompt de comando exibirá a versão do Python instalada no seu sistema.


#### 1. Criação do ambiente virtual.
Abra um terminal dentro da pasta do projeto e execute o comando abaixo.
```bash
python -m venv venv
```

#### 2. Ativando o ambiente virtual.
Para ativar o ambiente virtual execute o comando abaixo.
```bash
.\venv\Scripts\activate
```

#### 3. Instalação das dependencias.
Para atualizar o PIP para a versão mais recente
```bash
python.exe -m pip install --upgrade pip
```

#### 4. Instalação das dependencias.
Para instalar todas as dependencias do projeto execute o comando abaixo.
```bash
pip install -r requirements.txt
```

#### 5. veja a cobertura dos tests realizados.
rode o comando o comando abaixo 
```bash
pytest --cov .\test\
```

#### Resultado

---------- coverage: platform win32, python 3.11.3-final-0 -----------
| Arquivo                   | Linhas de Código | Linhas Ausentes | Cobertura |
|---------------------------|------------------|-----------------|-----------|
| test\__init__.py          | 0                | 0               | 100%      |
| test\custom_stack_test.py | 70               | 0               | 100%      |
| **Total**                 | **70**           | **0**           | **100%**  |
