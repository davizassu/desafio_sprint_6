# 🛒 Sistema de E-Commerce (POO em Python)

Este projeto é uma simulação de um sistema de catálogo de produtos, desenvolvido como desafio final da Sprint 6. O objetivo principal é aplicar, na prática, os pilares da Programação Orientada a Objetos (POO): Abstração, Encapsulamento, Herança e Polimorfismo.

## 🧠 O que eu aprendi neste projeto

1. **Modelagem do Mundo Real:** Entendi que Classes são "moldes" (substantivos) e Métodos são "ações" (verbos). 
2. **Encapsulamento com `@property`:** Aprendi a proteger os dados de um objeto. O objeto não deixa ninguém mexer em suas variáveis diretamente; tudo passa pelo "setter", que funciona como um filtro para evitar dados inválidos.
3. **Herança e Super():** Descobri como reaproveitar código. Em vez de reescrever `nome` e `preco` nas classes de Eletrônicos e Alimentos, utilizei o `super().__init__()` para aproveitar a lógica da classe mãe.
4. **Polimorfismo e Classes Abstratas:** Entendi o poder de tratar objetos diferentes de forma uniforme. Um `Eletronico` e um `Alimento` têm formas diferentes de calcular seu preço final (impostos vs perecibilidade), mas o meu sistema só precisa chamar `.calcular_preco_final()` e o próprio objeto decide como agir.
5. **Dunder Methods (Métodos Mágicos):** Compreendi que o Python nos deixa customizar comportamentos nativos, como ensinar o programa a imprimir um objeto de forma bonita (`__str__`) ou como ensinar o `sort()` a ordenar nossos objetos (`__lt__`).

## 📐 Diagrama de Classes (Mermaid)

Nossa modelagem demonstra tanto a relação de **Herança** (É um) quanto a relação de **Composição** (Tem um).

```mermaid
classDiagram
    class Marca {
        - String _nome
        + nome() String
        + nome(valor)
        + __str__()
    }

    class Produto {
        <<Abstract>>
        - String nome
        - Float _preco
        - Marca marca
        + preco() Float
        + preco(valor)
        + calcular_preco_final()* Float
        + __str__()
        + __eq__()
        + __lt__()
    }

    class Eletronico {
        + Integer garantia_meses
        + calcular_preco_final() Float
        + __str__()
    }

    class Alimento {
        + Boolean perecivel
        + calcular_preco_final() Float
        + __str__()
    }

    Produto o-- Marca : Tem uma (Composição)
    Produto <|-- Eletronico : É um (Herança)
    Produto <|-- Alimento : É um (Herança)
