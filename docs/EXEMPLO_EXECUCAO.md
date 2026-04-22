# Exemplo de Uso - Sistema de Menu e Entrada

## Execução Completa do Jogo

Este documento mostra um exemplo completo de como o programa funciona com entrada do usuário.

---

## 1. Iniciando o Programa

```bash
$ python -m src.main
```

---

## 2. Menu Principal

```
========================================
JOGOS DE TABULEIRO
========================================
1. Damas
9. Sair
========================================
Escolha uma opção: 1
```

---

## 3. Entrada de Nomes

```
========================================
CONFIGURAÇÃO DO JOGO
========================================
Nome do Jogador 1 (Peças de cima): Alice
Nome do Jogador 2 (Peças de baixo): Bob
```

---

## 4. Início do Jogo

```
========================================
JOGO DE DAMAS
========================================

==============================
Damas - Turno 0
Jogador atual: Alice
==============================

  0 1 2 3 4 5 6 7
0 # o # o # o # o 
1 o # o # o # o # 
2 # o # o # o # o 
3 . # . # . # . # 
4 # . # . # . # . 
5 O # O # O # O # 
6 # O # O # O # O 
7 O # O # O # O # 

Alice - Digite a jogada (l1 c1 l2 c2) ou 'sair': _
```

---

## 5. Primeiro Movimento - Válido

```
Alice - Digite a jogada (l1 c1 l2 c2) ou 'sair': 5 0 4 1

==============================
Damas - Turno 1
Jogador atual: Bob
==============================

  0 1 2 3 4 5 6 7
0 # o # o # o # o 
1 o # o # o # o # 
2 # o # o # o # o 
3 . # . # . # . # 
4 # O # . # . # . 
5 . # O # O # O # 
6 # O # O # O # O 
7 O # O # O # O # 

Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': _
```

---

## 6. Tentativa de Erro - Formato Inválido

### Exemplo 1: Poucos argumentos

```
Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 5 0

❌ Formato inválido. Use: l1 c1 l2 c2 (exemplo: 5 0 4 1)

Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 2 1 3 0
```

**Resultado:** Jogo NÃO foi cancelado. Bob pode tentar novamente.

---

### Exemplo 2: Valores não são números

```
Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 5 a 4 1

❌ Todos os valores devem ser números inteiros.

Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 2 1 3 0
```

**Resultado:** Jogo NÃO foi cancelado.

---

### Exemplo 3: Posições fora do intervalo

```
Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 2 1 3 8

❌ Posições devem estar entre 0 e 7.

Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 2 1 3 0
```

**Resultado:** Jogo NÃO foi cancelado.

---

### Exemplo 4: Movimento válido em formato, mas inválido em regras

```
Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 2 1 2 2

❌ Essa jogada é inválida! Verifique:
   - A peça pertence a você?
   - O movimento é diagonal?
   - A posição de destino está livre?
   - Peças normais só avançam (não voltam)

Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 2 1 3 0
```

**Resultado:** Jogo NÃO foi cancelado. Bob pode tentar outra jogada.

---

## 7. Segundo Movimento - Válido

```
Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 2 1 3 0

==============================
Damas - Turno 2
Jogador atual: Alice
==============================

  0 1 2 3 4 5 6 7
0 # o # o # o # o 
1 o # . # o # o # 
2 # . # o # o # o 
3 o # . # . # . # 
4 # O # . # . # . 
5 . # O # O # O # 
6 # O # O # O # O 
7 O # O # O # O # 

Alice - Digite a jogada (l1 c1 l2 c2) ou 'sair': _
```

---

## 8. Saída do Jogo - Com Confirmação

```
Alice - Digite a jogada (l1 c1 l2 c2) ou 'sair': sair

Tem certeza que deseja sair? (s/n): s
Jogo cancelado pelo jogador.

========================================
JOGOS DE TABULEIRO
========================================
1. Damas
9. Sair
========================================
Escolha uma opção: _
```

---

## 9. Saída do Jogo - Confirmação Negada

```
Alice - Digite a jogada (l1 c1 l2 c2) ou 'sair': sair

Tem certeza que deseja sair? (s/n): n

Alice - Digite a jogada (l1 c1 l2 c2) ou 'sair': 4 1 3 0
```

**Resultado:** Jogo continua normalmente.

---

## 10. Fim de Jogo - Vitória

```
[... após muitos movimentos ...]

==============================
Damas - Turno 47
Jogador atual: Alice
==============================

  0 1 2 3 4 5 6 7
0 # . # . # . # . 
1 . # . # . # . # 
2 # . # . # . # . 
3 . # . # . # . # 
4 # . # . # O # . 
5 . # . # . # . # 
6 # . # . # . # . 
7 . # . # . # . # 

Alice - Digite a jogada (l1 c1 l2 c2) ou 'sair': 4 4 3 5

==============================
🎉 JOGO TERMINADO!
VENCEDOR: Alice
==============================

========================================
JOGOS DE TABULEIRO
========================================
1. Damas
9. Sair
========================================
Escolha uma opção: _
```

---

## 11. Sair do Programa

```
Escolha uma opção: 9

Obrigado por jogar! Até logo!

$
```

---

## Resumo das Funcionalidades

| Funcionalidade | Status | Exemplo |
|---|---|---|
| Menu Principal | ✅ | Opções 1 (Damas), 9 (Sair) |
| Entrada de Nomes | ✅ | Máx 20 caracteres, validação |
| Formato de Jogada | ✅ | `5 0 4 1` |
| Validação de Números | ✅ | Rejeita `5 a 4 1` |
| Validação de Intervalo | ✅ | Rejeita `2 1 3 8` |
| Validação de Movimento | ✅ | Rejeita movimentos ilegais |
| Sem Cancelamento | ✅ | Erro = tenta novamente |
| Sair com Confirmação | ✅ | Pergunta antes de sair |
| Retorno ao Menu | ✅ | Após fim de jogo |
| Mensagens Claras | ✅ | Emojis (❌, ✅, 🎉) |

---

## Padrão de Validação

```
┌─────────────────────────────────────────────┐
│ Input do Usuário                            │
└────────────────────┬────────────────────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │ É "sair"?            │
          └──┬─────────────────┬──┘
             │ Sim    │ Não     
             │        └─────────────────┐
             │                          ▼
             │                 ┌─────────────────────┐
             │                 │ Tem 4 valores?      │
             │                 └──┬──────────────┬───┘
             │                    │ Não  │ Sim
             │                    │      └──────────────┐
             │                    │                     ▼
             │                    │            ┌─────────────────────┐
             │                    │            │ São inteiros?       │
             │                    │            └──┬──────────────┬───┘
             │                    │               │ Não  │ Sim
             │                    │               │      └──────────────┐
             │                    │               │                     ▼
             │                    │               │            ┌─────────────────────┐
             │                    │               │            │ Estão em [0,7]?     │
             │                    │               │            └──┬──────────────┬───┘
             │                    │               │               │ Não  │ Sim
             │                    │               │               │      └─────┐
             │                    │               │               │            ▼
             │                    │               │               │   ┌─────────────────────┐
             │                    │               │               │   │ Jogada válida?      │
             │                    │               │               │   └──┬──────────────┬───┘
             │                    │               │               │      │ Não  │ Sim
        ┌────▼────┐    ┌─────────▼──┐  ┌─────────▼──┐  ┌──────┘──▼──┐  └──────┬──────┘
        │Confirmar │    │Peso Inválido│  │Formato Inv│  │Posi Inv│  │Mov Válido
        │Saída?    │    │Tenta novamente│  │Tenta novamente│Tenta novamente│Executa
        └──┬───┬───┘    └───────────────┘  └────────────┘  └───────────────┘  └──────┬──┘
           │ │ │                                                                      │
           │ │ Não                                                                    │
        Sim│ └────────────────────────────────────────────────────────────────┐       │
           │                                                                   │       │
           ▼                                                              ┌────▼───────▼──┐
        Encerra                                                         │ Próximo Turno  │
                                                                        └─────────────────┘
```

---

## Conclusão

O sistema implementa validação robusta em todas as camadas, garantindo que:
- ✅ Erros não cancelam o jogo
- ✅ Mensagens são claras e específicas
- ✅ Usuário pode tentar novamente
- ✅ Saída é confirmada
- ✅ Menu permite múltiplas partidas
