"""
Giovanna Revito Roz
RM 558981
Luiz Wanderley Tavares
"""


def print_lista():
    """
    LISTAS

    Lista é um conjunto mutável de elementos ordenados, que podem armazenar multiplos tipos de valores e dados em uma única variável

    """

    #Exercicio 1
    fruits = ["banana","maça","morango","uva verde", "lichia"]
    print(fruits[1])
    print(fruits[-1])

    #Exercicio 2
    fruits.append("manga")
    fruits.remove("banana")
    print(fruits)

    #Exercicio 3
    fruits[2] = "abacaxi"
    print(fruits)

    #Exercicio 4
    def contador(*args):
        print(len(*args))

    lista = list(range(1,11))

    contador(lista)

    #Exercicio 5
    print(sum(lista))

def print_dict():
    """
    DICIONÁRIOS

    É um tipo de dado que armazena pares chave-valo, cada chave precisa ser única e é usada para acessar o valor associado a ela.

    Servem pra armazenar informações relacionadas que podem ser acessadas rapidamente.

    """

    #Exercicio 1:
    dados_pessoais = {"nome": "Seu Nome", "idade": 20, "cidade": "Sua Cidade"}
    print(dados_pessoais["nome"])

    #Exercicio 2:
    dados_pessoais["profissão"] = "Sua Profissão"
    del dados_pessoais["cidade"]

    #Exercicio 3:
    dados_pessoais["idade"] = 21

    #Exercicio 4:
    notas = {"João": 8.5, "Maria": 9.0, "Pedro": 7.0}
    for nome, nota in notas.items():
        print(f"{nome}: {nota}")

    #Exercicio 5:
    if "endereço" not in dados_pessoais:
        dados_pessoais["endereço"] = "Avenida XYZ, 123"
        #ou implementando um input para digitar o endereço
        print(dados_pessoais)

def print_set():

    """SETS
    É um tipo de dado que armazena uma coleção não ordenada de objetos

    Podem resolver problemas de verificação de duplicatas, operações de conjuntos e otimização de desempenho.

    """
    #Exercicio 1:
    fruits = {"maçã", "banana", "laranja", "uva"}
    print(fruits)

    #Exercicio 2:
    fruits.add("manga")
    print(fruits)
    fruits.remove("laranja")
    print(fruits)

    #Exercicio 3:
    if "banana" in fruits:
      print("A fruta 'banana' está presente no conjunto frutas.")
    if "abacaxi" in fruits:
      print("A fruta 'abacaxi' está presente no conjunto frutas.")

    #Exercicio 4:
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    uniao = set1.union(set2)
    print(uniao)

    #Exercicio 5:
    intersecao = set1.intersection(set2)
    print(intersecao)


def print_tuplas():

    """
    TUPLAS

    É uma estrutura de dado imutável e que armazena uma sequência ordenada de elementos.

    São parecidos com listas, porém seus elementos não podem ser modificados após a criação da tupla.

    Podem ser usados quando você precisa armazenar uma sequência de dados que não podem ou devem ser alterados,
    quando precisa usar uma sequência como uma chave em um dicionário e também para permitir uma maior integridade e consistência

    """


    #Exercicio 1:
    coordenadas = (23.55, -46.63)
    latitude = coordenadas[0]
    longitude = coordenadas[1]
    print(f"Latitude: {latitude}, Longitude: {longitude}")

    #Exercicio 2:
    cores = ("vermelho", "azul", "branco")
    cores[0] = "amarelo"
    # As tuplas são imutáveis, sendo assim, não podem ser alteradas.

    #Exercicio 3:
    nomes = ["Pedro", "Catarina", "Isabel"]
    tupla_nomes = tuple(nomes)
    print(tupla_nomes)

    #Exercicio 4:
    pessoa = ("João", 30, "São Paulo")
    nome, idade, cidade = pessoa
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

    #Exercicio 5:
    localizacao = {
        (23.55, -46.63): "São Paulo",
        (34.05, -118.24): "Los Angeles",
        (48.86, 2.35): "Paris"
    }
    print(localizacao[(23.55, -46.63)])
    #Criacao de uma chave valor utilizando tupla


"""
FUNÇÕES

São blocos de códigos reutilizáveis que fazem tarefas específicas, tornam o código mais organizado, eficiente, 

executando também a função apenas quando necessária, deixando o código e a aplicação mais limpa.

"""

#EXERCICIO 5: NUMEROS PRIMOS

def eh_primo(numero):

  if numero < 2:
    return False

  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False

  #Retorna true se nenhum é divisível, então é primo.
  return True


#EXERCICIO 7
def media(numeros):
  """Calcula a média de uma lista de números."""
  if len(numeros) == 0:
    return 0
  soma = sum(numeros)
  media = soma / len(numeros)
  return media

#EXERCICIO 8

def descricao_pessoa(nome, idade, cidade):
  return f"{nome} tem {idade} anos e mora em {cidade}."

#EXERCICIO 9
def soma_multiplos(*args):
  soma = 0
  for arg in args:
    soma += arg
  return soma


#EXERCICIO 10: CONVERTER TEMPERATURA

def converter_temperatura(temperatura, unidade):
  if unidade == "Celsius":
    return (temperatura * 9/5) + 32
  elif unidade == "Fahrenheit":
    return (temperatura - 32) * 5/9
  else:
    return "Unidade inválida."
