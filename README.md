# semana-06-py
Explicação Detalhada do Código

A estrutura do projeto foi desenvolvida para demonstrar os principais pilares da **Programação Orientada a Objetos (POO)** em Python: Abstração, Encapsulamento, Herança e Polimorfismo.

1. Classe Abstrata `Conta` (Base do Sistema)
A classe `Conta` herda de `ABC` (Abstract Base Class) e serve como o modelo base para todos os tipos de conta bancária. Ela não pode ser instanciada diretamente.

- Encapsulamento com `@property`:
  - Os atributos `_saldo` e `_titular` são protegidos com `_`.
  - O uso de getters e setters via `@property` garante a integridade dos dados, impedindo saldos iniciais negativos ou nomes de titulares em branco.
 Métodos da Classe:
  `depositar(valor)` e `sacar(valor)`: Realizam as operações básicas validando os valores de entrada.
 `@abstractmethod def calcular_tarifa_mensal()`: Método abstrato que força todas as classes filhas a implementarem sua própria regra de cobrança de tarifa.
- Métodos Especiais (Dunder Methods):
   `__str__`: Retorna uma representação amigável do objeto em formato de texto.
   `__repr__`: Retorna uma representação explícita do objeto para depuração.
   `__eq__`: Permite comparar se duas contas possuem o mesmo saldo (`conta1 == conta2`).
   `__lt__`: Permite ordenar listas de contas com base no saldo (`conta1 < conta2`).



2. Classes Filhas (Herança e Especialização)

Cada subclasse estende a classe base `Conta` e adiciona comportamentos específicos usando `super().__init__()` para reaproveitar a inicialização do pai:

`ContaCorrente`
 Atributo próprio: `limite` (cheque especial), protegido por `@property` para evitar valores negativos.
 Sobrescrita do `sacar()`: Permite realizar saques utilizando o saldo disponível somado ao limite do cheque especial.
 Polimorfismo em `calcular_tarifa_mensal()`: Retorna uma tarifa fixa de R$ 20,00.

 `ContaPoupanca`
Atributo próprio: `taxa_rendimento`.
 Método específico `rendimento_mensal()`: Calcula e aplica os juros de rendimento ao saldo da conta.
Polimorfismo em `calcular_tarifa_mensal()`: Retorna R$ 0,00 (conta isenta de tarifas).

 `ContaInvestimento`
 Atributo próprio: `taxa_admin` (taxa de administração).
 Polimorfismo em `calcular_tarifa_mensal()`: Calcula a tarifa de forma dinâmica, cobrando uma porcentagem sobre o saldo atual da conta.


 3. Testes, Polimorfismo e Tratamento de Exceções

No bloco principal (`if __name__ == "__main__":`), o código executa cenários reais para demonstrar as funcionalidades:

1. Instanciação de 10 Objetos: Criação de diversas contas (`ContaCorrente`, `ContaPoupanca` e `ContaInvestimento`).
2. Demonstração de Polimorfismo: Iteração sobre a lista unificada de contas executando `conta.calcular_tarifa_mensal()`. Cada classe responde à chamada do método com sua própria regra de negócio.
3. Uso de Métodos Dunder**: Comparação e ordenação da lista de contas utilizando a função nativa `sorted()` do Python (graças ao método `__lt__`).
4. **Tratamento de Erros (`try/except`)**: Tentativas intencionais de criar contas com dados inválidos (ex: saldo ou limite negativo, nome vazio) para demonstrar a captura de exceções `ValueError` lançadas pelos setters.
