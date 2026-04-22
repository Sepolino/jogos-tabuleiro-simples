# Arquitetura do Sistema de Jogos de Tabuleiro

## Visão Geral

A arquitetura foi projetada seguindo princípios SOLID para permitir fácil extensão com novos jogos.

## Classes Base (src/core/)

### 1. `JogoTabuleiro` (Abstrata)
- **Responsabilidade**: Define a interface e lógica genérica de um jogo
- **Métodos principais**:
  - `inicializar()`: setup do jogo
  - `validar_jogada(jogada)`: verifica se jogada é legal
  - `aplicar_jogada(jogada)`: executa a jogada
  - `verificar_fim_de_jogo()`: detecta vitória/derrota
  - `executar_turno(jogada)`: executa turno completo
- **Responsabilidades**: gerenciar turnos, histórico de jogadas, estado do jogo

### 2. `Tabuleiro` (Abstrata)
- **Responsabilidade**: representa o espaço onde o jogo acontece
- **Métodos principais**:
  - `obter_peca(linha, coluna)`: acessa peça
  - `colocar_peca(linha, coluna, peca)`: insere peça
  - `remover_peca(linha, coluna)`: remove peça
  - `exibir()`: renderiza o tabuleiro
- **Encapsulamento**: _celulas privada, acesso via métodos

### 3. `Jogador`
- **Responsabilidade**: representa um participante do jogo
- **Atributos**: id, nome, estado ativo/inativo
- **Associação**: cada Jogo possui 2 Jogadores

### 4. `Peca`
- **Responsabilidade**: representa uma unidade do jogo
- **Atributos**: jogador_id, tipo (normal/especial para promoção)
- **Composição**: Tabuleiro contém múltiplas Peças

### 5. `Jogada`
- **Responsabilidade**: representa um movimento de peça
- **Atributos**: coordenadas iniciais, finais, peça capturada
- **Agregação**: JogoTabuleiro mantém histórico de Jogadas

## Implementação Concreta: Damas

### `Damas` (estende `JogoTabuleiro`)
- Implementa toda a lógica específica do jogo
- Valida movimentos diagonais, capturas de 2 casas
- Promove peças ao atingir a borda

### `TabuleiroDamas` (estende `Tabuleiro`)
- Tabuleiro 8x8
- Apenas quadrados escuros são jogáveis
- Usa padrão de cores para evitar peças em quadrados inválidos

## Relações de Objetos

```
JogoTabuleiro
├── 2x Jogador
├── 1x Tabuleiro
│   └── N x Peca
└── N x Jogada (histórico)
```

## Pontos de Extensibilidade

Para adicionar novo jogo (ex: Xadrez):

1. Criar `TauleiroXadrez` estendendo `Tabuleiro`
2. Criar `Xadrez` estendendo `JogoTabuleiro`
3. Implementar regras específicas (movimentos de cada peça, xeque, etc.)
4. Classes base (`Jogador`, `Peca`, `Jogada`) são reaproveitadas

## Conceitos de POO Aplicados

- **Abstração**: classes base com métodos abstratos
- **Herança**: Damas e TabuleiroDamas herdam comportamentos genéricos
- **Polimorfismo**: cada jogo implementa `validar_jogada()` de forma diferente
- **Encapsulamento**: atributos privados com underscores, acesso via propriedades
- **Composição**: Jogo composto de Tabuleiro, Jogadores, Jogadas
- **Agregação**: Jogo mantém referência a histórico de Jogadas
