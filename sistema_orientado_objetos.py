from abc import ABC, abstractmethod

# ==========================================
# 1. CLASSE DE COMPOSIÇÃO ("Tem um")
# ==========================================
class Marca:
    """Representa a marca de um produto (Ex: Samsung, Nestlé)."""
    
    def __init__(self, nome):
        # Chamamos o setter (o método com @nome.setter) para validar logo na criação
        self.nome = nome
        
    @property
    def nome(self):
        # Getter: Como a informação é acessada
        return self._nome
        
    @nome.setter
    def nome(self, valor):
        # Setter: Valida a informação antes de salvar
        if not valor or len(valor.strip()) == 0:
            raise ValueError("O nome da marca não pode estar vazio.")
        self._nome = valor.strip().title()
        
    def __str__(self):
        # Representação amigável para o usuário final
        return self.nome
        
    def __repr__(self):
        # Representação oficial (útil para debug e logs)
        return f"Marca(nome='{self.nome}')"


# ==========================================
# 2. CLASSE ABSTRATA ("Mãe")
# ==========================================
class Produto(ABC):
    
    def __init__(self, nome, preco, marca):
        self.nome = nome
        self.preco = preco # Passa pela validação do @property
        
        # COMPOSIÇÃO: Um Produto "TEM UMA" Marca.
        if not isinstance(marca, Marca):
            raise TypeError("O atributo 'marca' deve ser um objeto da classe Marca.")
        self.marca = marca
        
    @property
    def preco(self):
        return self._preco
        
    @preco.setter
    def preco(self, valor):
        # Proteção (Encapsulamento): Impede que criem um produto com preço negativo
        if valor < 0:
            raise ValueError(f"O preço não pode ser negativo. Valor tentado: R$ {valor}")
        self._preco = valor
        
    @abstractmethod
    def calcular_preco_final(self):
        # Método abstrato: Toda classe filha é OBRIGADA a criar esse método.
        pass

    # --- MÉTODOS MÁGICOS (Dunder Methods) ---
    def __str__(self):
        return f"{self.nome} ({self.marca}) - R$ {self.preco:.2f}"
        
    def __repr__(self):
        return f"{self.__class__.__name__}(nome='{self.nome}', preco={self.preco}, marca={self.marca.nome})"
        
    def __eq__(self, outro_produto):
        # Ensina o Python a comparar se um produto é igual a outro (usando ==) pelo preço
        return self.preco == outro_produto.preco
        
    def __lt__(self, outro_produto):
        # Ensina o Python a saber quem é "menor que". Permite usar a função sort()
        return self.preco < outro_produto.preco


# ==========================================
# 3. CLASSES FILHAS ("É um" - Herança)
# ==========================================
class Eletronico(Produto):
    """Eletrônico 'É UM' Produto."""
    
    def __init__(self, nome, preco, marca, garantia_meses):
        # super() chama o __init__ da classe mãe (Produto)
        super().__init__(nome, preco, marca)
        
        # Atributo exclusivo desta classe
        if garantia_meses < 0:
            raise ValueError("Garantia não pode ser negativa.")
        self.garantia_meses = garantia_meses
        
    # POLIMORFISMO: O eletrônico calcula o preço final com 10% de imposto
    def calcular_preco_final(self):
        imposto = self.preco * 0.10
        return self.preco + imposto
        
    def __str__(self):
        # Aproveita o __str__ da classe mãe e adiciona detalhes
        return f"[Eletronico] {super().__str__()} | Garantia: {self.garantia_meses} meses"


class Alimento(Produto):
    """Alimento 'É UM' Produto."""
    
    def __init__(self, nome, preco, marca, perecivel):
        super().__init__(nome, preco, marca)
        self.perecivel = perecivel
        
    # POLIMORFISMO: O alimento não tem imposto, e se for perecível, tem 5% de desconto
    def calcular_preco_final(self):
        if self.perecivel:
            desconto = self.preco * 0.05
            return self.preco - desconto
        return self.preco
        
    def __str__(self):
        return f"[Alimento] {super().__str__()} | Perecivel: {'Sim' if self.perecivel else 'Nao'}"


# ==========================================
# 4. TESTES E DEMONSTRAÇÃO
# ==========================================
if __name__ == "__main__":
    print("--- INICIANDO TESTES DO SISTEMA ---\n")
    
    # 1. Tratamento de Exceções (Testando o Encapsulamento)
    print(">> TESTANDO VALIDACOES (@property e try/except):")
    try:
        marca_invalida = Marca("")
    except ValueError as erro:
        print(f"[ERRO CAPTURADO] {erro}")
        
    try:
        marca_sony = Marca("Sony")
        tv_invalida = Eletronico("TV OLED", -500.0, marca_sony, 12)
    except ValueError as erro:
        print(f"[ERRO CAPTURADO] {erro}")


    print("\n>> CRIANDO INSTANCIAS VALIDAS:")
    # Criando Marcas (Objetos de composição)
    nestle = Marca("Nestle")
    samsung = Marca("Samsung")
    apple = Marca("Apple")
    pepsico = Marca("PepsiCo")
    
    # Criando 10 instâncias no total (4 Marcas + 6 Produtos)
    produtos_estoque = [
        Eletronico("Smartphone Galaxy S23", 4000.0, samsung, 12),
        Eletronico("MacBook Air M2", 8000.0, apple, 12),
        Eletronico("Smart TV 55", 3500.0, samsung, 24),
        Alimento("Barra de Chocolate", 10.0, nestle, perecivel=True),
        Alimento("Iogurte Natural", 5.0, nestle, perecivel=True),
        Alimento("Salgadinho Doritos", 8.0, pepsico, perecivel=False)
    ]
    
    print(f"[SUCESSO] Foram criados {len(produtos_estoque)} produtos e 4 marcas.\n")

    # Demonstração de Polimorfismo
    print(">> DEMONSTRACAO DE POLIMORFISMO (Calculo de Precos Final):")
    total_carrinho = 0
    for prod in produtos_estoque:
        print(prod) 
        preco_final = prod.calcular_preco_final()
        print(f"   -> Preco final de venda: R$ {preco_final:.2f}\n")
        total_carrinho += preco_final
        
    print(f"[TOTAL] Valor do estoque (com taxas/descontos): R$ {total_carrinho:.2f}")

    # Demonstração dos Métodos Mágicos (__lt__)
    print("\n>> DEMONSTRACAO DE ORDENACAO (Uso do Dunder Method __lt__):")
    produtos_estoque.sort() 
    print("Produtos ordenados do mais barato para o mais caro:")
    for prod in produtos_estoque:
        print(f" - R$ {prod.preco:.2f} : {prod.nome}")