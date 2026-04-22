# Jogos de Tabuleiro - Arquitetura OO

## Integrantes

- Marcus Vinícius Milan da Silva

## Descrição Geral

Arquitetura extensível de jogos de tabuleiro em Python, seguindo princípios sólidos de Orientação a Objetos. A solução foi pensada para permitir implementação de diferentes jogos reutilizando a base comum.

## Arquitetura

A solução é dividida em dois níveis:

### Core (`src/core/`)
Classes genéricas e reutilizáveis que definem a estrutura de qualquer jogo de tabuleiro:

- **`JogoTabuleiro`** (abstrata): define interface para qualquer jogo
- **`Tabuleiro`** (abstrata): representa o espaço de jogo
- **`Jogador`**: encapsula dados do participante
- **`Peca`**: unidade que existe no tabuleiro
- **`Jogada`**: representa um movimento

### Jogos (`src/jogos/`)
Implementações concretas de jogos específicos:

- **`Damas`**: lógica completa do jogo de damas
- **`TabuleiroDamas`**: tabuleiro 8x8 específico para damas

## Conceitos de POO

✓ **Abstração**: `JogoTabuleiro` e `Tabuleiro` com métodos abstratos  
✓ **Herança**: `Damas` herda de `JogoTabuleiro`, `TabuleiroDamas` herda de `Tabuleiro`  
✓ **Polimorfismo**: cada jogo implementa `validar_jogada()` de forma específica  
✓ **Encapsulamento**: atributos privados (`_atributo`) com propriedades públicas  
✓ **Composição**: Jogo contém Tabuleiro, Jogadores, histórico de Jogadas  
✓ **Agregação**: Jogo possui referências a múltiplas Jogadas  

## Jogo Implementado

### Damas Clássico
- Tabuleiro 8x8
- 2 jogadores com 12 peças cada
- Movimento diagonal de 1 casa
- Captura pulando 2 casas
- Promoção a rei ao atingir a borda oposta
- Reis podem mover-se em qualquer direção diagonal
- Derrota ao perder todas as peças ou ter sem movimentos válidos

## Como Executar

### Jogar Interativamente

```bash
python -m src.main
```

**Fluxo do Jogo:**

1. **Menu Principal** - Escolha o jogo:
   ```
   1. Damas
   9. Sair
   ```

2. **Entrada de Nomes** - Digite os nomes dos 2 jogadores

3. **Jogo** - Faça suas jogadas:
   - Digite: `linha_ini coluna_ini linha_fim coluna_fim`
   - Exemplo: `5 0 4 1`
   - Ou digite `sair` para desistir

**Formato de Posições:**
- Linhas: 0-7 (de cima para baixo)
- Colunas: 0-7 (da esquerda para direita)

**Validação Robusta:**
- Se formato inválido → mensagem clara e tenta novamente
- Não cancela o jogo por erro de entrada
- Permite `sair` com confirmação

### Executar Testes

**Testes Unitários:**
```bash
python -m unittest tests.test_damas -v
```

**Testes Manuais (Validação Completa):**
```bash
python -m tests.test_manual
```

**Resultado:** ✅ 11 testes unitários + 5 testes manuais passando

## Estrutura do Projeto

```
jogos-de-tabuleiro/
├── README.md
├── docs/
│   ├── ARQUITETURA.md        # Design OO da arquitetura
│   ├── IMPLEMENTACAO.md      # Detalhes de implementação
│   └── MENU_E_ENTRADA.md     # Sistema de menu e validação
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── jogo.py           # Classe base dos jogos
│   │   ├── tabuleiro.py      # Classe base do tabuleiro
│   │   ├── jogador.py        # Classe Jogador
│   │   ├── peca.py           # Classe Peça
│   │   └── jogada.py         # Classe Jogada
│   ├── jogos/
│   │   ├── __init__.py
│   │   ├── damas.py          # Implementação de Damas
│   │   └── tabuleiro_damas.py # Tabuleiro 8x8 para damas
│   ├── main.py               # Menu e entrada de dados
│   └── __init__.py
└── tests/
    ├── __init__.py
    ├── test_damas.py         # Testes unitários (11 testes)
    └── test_manual.py        # Testes manuais (5 testes)
```

## Testes

**Testes Unitários:**
Suite de testes cobrindo:
- Inicialização do jogo
- Validação de jogadas inválidas
- Movimentos válidos
- Capturas de peças
- Promoção de peças
- Alternância de turnos
- Detecção de fim de jogo

```bash
python -m unittest tests.test_damas.TestDamas -v
```

**Testes Manuais:**
Validação do sistema completo:
- Validação de movimentos
- Fluxo de jogo
- Alternância de turnos
- Captura de peças
- Promoção de peças

```bash
python -m tests.test_manual
```

## Validação de Entrada

O sistema implementa validação robusta em múltiplas camadas:

**Entrada de Nomes:**
- Máximo 20 caracteres
- Não pode estar vazio
- Se inválido, reproduz mensagem e tenta novamente

**Entrada de Jogada:**
- Formato: `linha_ini coluna_ini linha_fim coluna_fim`
- Valida número de argumentos
- Valida se são inteiros
- Valida se posições estão no intervalo [0-7]
- Se inválido, mostra erro específico e tenta novamente
- NÃO cancela o jogo

**Exemplos de Erro:**

```
❌ Formato inválido. Use: l1 c1 l2 c2 (exemplo: 5 0 4 1)
❌ Todos os valores devem ser números inteiros.
❌ Posições devem estar entre 0 e 7.
❌ Essa jogada é inválida! Verifique:
   - A peça pertence a você?
   - O movimento é diagonal?
   - A posição de destino está livre?
   - Peças normais só avançam (não voltam)
```

## Como Adicionar um Novo Jogo

**1. Criar a implementação do jogo:**
- Criar `src/jogos/teste_jogo.py`
- Criar `TauleirotesteJogo` estendendo `Tabuleiro`
- Criar `testeJogo` estendendo `JogoTabuleiro`
- Implementar métodos abstratos obrigatórios

**2. Atualizar o menu:**
- Editar `src/main.py`
- Adicionar opção no `menu_principal()`
- Adicionar função `executar_teste_jogo()`
- Adicionar case no `main()`

**3. Adicionar testes:**
- Criar `tests/test_teste_jogo.py`
- Cobrir regras importantes

**Reuso de Classes:**
As classes `Jogador`, `Peca`, `Jogada` são reutilizadas sem modificação.

**Exemplo:**
```python
# src/jogos/teste_jogo.py
from src.core import JogoTabuleiro, Tabuleiro

class TauleirotesteJogo(Tabuleiro):
    def __init__(self):
        super().__init__(8)  # ou outro tamanho
    
    def _criar_tabuleiro(self):
        pass
    
    def exibir(self):
        pass

class testeJogo(JogoTabuleiro):
    def validar_jogada(self, jogada):
        pass
    
    # ... implementar outros métodos abstratos
```

## Decisões de Projeto

- **Métodos abstratos**: força subclasses a implementar lógica específica
- **Propriedades privadas**: protege estado interno
- **Validação antes de aplicar**: garante consistência
- **Histórico de jogadas**: permite replay ou análise

## Limitações e Melhorias Futuras

### Limitações Atuais
- Interface apenas em terminal (sem GUI)
- Jogador deve saber coordenadas (sem seleção visual)
- Sem salvamento de partidas

### Melhorias Possíveis
- Interface gráfica (tkinter ou pygame)
- Mais jogos implementados (Xadrez, Jogo da Velha, etc.)
- IA para jogar contra computador
- Sistema de pontuação e elo
- Validação de movimentos com "deep copy" de estado

## Observações

Esta solução prioriza clareza e extensibilidade sobre complexidade. O código é simples, bem comentado e fácil de estender com novos jogos mantendo a base intocada.
