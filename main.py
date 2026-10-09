from abc import ABC, abstractmethod


# 1. CLASSE ABSTRATA (MODELAGEM DE CLASSES & ENCAPSULAMENTO)
class Conta(ABC):
    """Classe base abstrata para contas bancárias."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self._saldo = 0.0
        self.saldo = saldo_inicial  # Utiliza o setter para validação inicial

    #Property para Titular 
    @property
    def titular(self) -> str:
        return self._titular

    @titular.setter
    def titular(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O nome do titular não pode ser vazio.")
        self._titular = valor.strip()

    #Property para Saldo (Encapsulamento com Validação)
    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if valor < 0:
            raise ValueError(
                f"Erro ({self.titular}): Saldo inicial/novo não pode ser negativo (R$ {valor:.2f})."
            )
        self._saldo = valor

    #Operações Bancárias 
    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError(
                f"Saldo insuficiente na conta de {self.titular}. Saldo disponível: R$ {self._saldo:.2f}"
            )
        self._saldo -= valor

    #Polimorfismo: Método Abstrato 
    @abstractmethod
    def calcular_tarifa_mensal(self) -> float:
        """Calcula a tarifa de manutenção mensal da conta."""
        pass

    # Métodos Especiais 
    def __str__(self) -> str:
        return f"Titular: {self.titular} | Saldo: R$ {self._saldo:.2f}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(titular='{self.titular}', saldo={self._saldo})"

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Conta):
            return NotImplemented
        return self._saldo == outro._saldo

    def __lt__(self, outro: object) -> bool:
        if not isinstance(outro, Conta):
            return NotImplemented
        return self._saldo < outro._saldo

# 2. CLASSES FILHAS (HERANÇA E SUPER())

class ContaCorrente(Conta):
    """Classe filha representando Conta Corrente com limite de cheque especial."""

    def __init__(
        self, titular: str, saldo_inicial: float = 0.0, limite: float = 500.0
    ):
        super().__init__(
            titular, saldo_inicial
        )  # Chamada ao construtor pai
        self.limite = limite

    @property
    def limite(self) -> float:
        return self._limite

    @limite.setter
    def limite(self, valor: float):
        if valor < 0:
            raise ValueError("O limite do cheque especial não pode ser negativo.")
        self._limite = valor

    # Sobrescrevendo o método sacar para considerar o limite
    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > (self._saldo + self._limite):
            raise ValueError(
                f"Saque excede o saldo e limite disponível de R$ {self._saldo + self._limite:.2f}."
            )
        self._saldo -= valor

    #Polimorfismo: Sobrescrita do método abstrato 
    def calcular_tarifa_mensal(self) -> float:
        return 20.0  # Tarifa fixa mensal de Conta Corrente

    def __str__(self) -> str:
        return f"[Conta Corrente] {super().__str__()} | Limite: R$ {self.limite:.2f}"


class ContaPoupanca(Conta):
    """Classe filha representando Conta Poupança com taxa de rendimento."""

    def __init__(
        self,
        titular: str,
        saldo_inicial: float = 0.0,
        taxa_rendimento: float = 0.005,
    ):
        super().__init__(
            titular, saldo_inicial
        )  # Chamada ao construtor pai
        self.taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self) -> float:
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor: float):
        if valor < 0:
            raise ValueError("A taxa de rendimento não pode ser negativa.")
        self._taxa_rendimento = valor

    def rendimento_mensal(self) -> float:
        """Aplica o rendimento na conta."""
        ganho = self._saldo * self._taxa_rendimento
        self._saldo += ganho
        return ganho

    #Polimorfismo: Sobrescrita do método abstrato 
    def calcular_tarifa_mensal(self) -> float:
        return 0.0  # Isenta de tarifa mensal

    def __str__(self) -> str:
        return f"[Conta Poupança] {super().__str__()} | Taxa: {self.taxa_rendimento * 100:.1f}%"


class ContaInvestimento(Conta):
    """Classe filha representando Conta de Investimento com taxa de administração."""

    def __init__(
        self,
        titular: str,
        saldo_inicial: float = 0.0,
        taxa_admin: float = 0.01,
    ):
        super().__init__(titular, saldo_inicial)
        self.taxa_admin = taxa_admin

    @property
    def taxa_admin(self) -> float:
        return self._taxa_admin

    @taxa_admin.setter
    def taxa_admin(self, valor: float):
        if valor < 0:
            raise ValueError("A taxa de administração não pode ser negativa.")
        self._taxa_admin = valor

    #Polimorfismo: Sobrescrita do método abstrato
    def calcular_tarifa_mensal(self) -> float:
        return self._saldo * self._taxa_admin  # Tarifa proporcional ao saldo

    def __str__(self) -> str:
        return f"[Conta Investimento] {super().__str__()} | Taxa Admin: {self.taxa_admin * 100:.1f}%"

# 3. TESTES E DEMONSTRAÇÃO

if __name__ == "__main__":
    print("=== CRIAÇÃO E INSTANCIAÇÃO DE OBJETOS (Mínimo 10 Instâncias) ===\n")

    contas = []

    # 1. Instanciação válida de 10 objetos
    try:
        contas = [
            ContaCorrente("Alice Silva", 1500.0, 1000.0),
            ContaCorrente("Bruno Lima", 500.0, 300.0),
            ContaCorrente("Carla Souza", 2500.0, 1500.0),
            ContaCorrente("Diego Rocha", 100.0, 200.0),
            ContaPoupanca("Eduarda Costa", 3000.0, 0.006),
            ContaPoupanca("Fernando Dias", 8000.0, 0.005),
            ContaPoupanca("Gabriela Alves", 12000.0, 0.007),
            ContaInvestimento("Heitor Martins", 50000.0, 0.015),
            ContaInvestimento("Isabela Santos", 20000.0, 0.01),
            ContaInvestimento("João Pedro", 35000.0, 0.012),
        ]
        print(f"✔️ {len(contas)} contas criadas com sucesso!\n")
    except ValueError as e:
        print(f"Erro na criação de conta: {e}")

    # 2. Demonstração de Polimorfismo (Iterando sobre a lista)
    print("=== DEMONSTRAÇÃO DE POLIMORFISMO ===")
    print("Calculando tarifa mensal para diferentes tipos de contas:\n")
    for conta in contas:
        tarifa = conta.calcular_tarifa_mensal()
        print(f"{conta} -> Tarifa Mensal: R$ {tarifa:.2f}")

    # 3. Métodos Dunder (__repr__, __eq__, __lt__)
    print("\n=== DEMONSTRAÇÃO DE MÉTODOS ESPECIAIS (DUNDER) ===")
    print(f"__repr__: {repr(contas[0])}")
    print(f"__eq__ ({contas[0].titular} == {contas[1].titular}): {contas[0] == contas[1]}")

    # Ordenação por saldo utilizando __lt__
    contas_ordenadas = sorted(contas)
    print(f"\nConta com menor saldo: {contas_ordenadas[0]}")
    print(f"Conta com maior saldo: {contas_ordenadas[-1]}")

    # 4. Tratamento de Exceções (try/except) para entradas inválidas com @property
    print("\n=== DEMONSTRAÇÃO DE TRATAMENTO DE EXCEÇÕES (VALIDAÇÕES) ===")

    testes_invalidos = [
        lambda: ContaCorrente("Lucas", -500.0),  # Saldo negativo
        lambda: ContaCorrente("", 1000.0),  # Nome vazio
        lambda: ContaCorrente("Marcos", 500.0, limite=-200.0),  # Limite negativo
        lambda: contas[0].sacar(5000.0),  # Saque maior que saldo + limite
    ]

    for i, teste in enumerate(testes_invalidos, 1):
        try:
            teste()
        except ValueError as e:
            print(f"Captura de Exceção {i}: {e}")