# Sistema de Menu e Entrada de Dados

## Visão Geral

O sistema foi refatorado para incluir:

1. **Menu Principal** - Escolha do jogo (extensível)
2. **Entrada de Nomes** - Pedir nomes dos 2 jogadores
3. **Validação Robusta** - Tratamento de erros sem cancelar o jogo
4. **Interface Melhorada** - Mensagens claras e amigáveis

---

## Como Executar

```bash
python -m src.main
```

---

## Fluxo do Jogo

### 1. Menu Principal

```
========================================
JOGOS DE TABULEIRO
========================================
1. Damas
9. Sair
========================================
Escolha uma opção: _
```

**Opções:**
- `1` → Inicia um jogo de Damas
- `9` → Sai do programa
- Outro valor → "Opção inválida. Digite 1 ou 9."

---

### 2. Configuração do Jogo

```
========================================
CONFIGURAÇÃO DO JOGO
========================================
Nome do Jogador 1 (Peças de cima): Alice
Nome do Jogador 2 (Peças de baixo): Bob
```

**Validação:**
- Máximo 20 caracteres
- Não pode estar vazio
- Se inválido, pede novamente

---

### 3. Durante o Jogo

```
==============================
Damas - Turno 1
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

## Validação de Entrada

### Formatos Aceitos

✓ **Válido:** `5 0 4 1` (move de [5,0] para [4,1])

### Tratamento de Erros

❌ **Sem números:** `5 0 a 1`
```
❌ Todos os valores devem ser números inteiros.
```

❌ **Poucos argumentos:** `5 0 4`
```
❌ Formato inválido. Use: l1 c1 l2 c2 (exemplo: 5 0 4 1)
```

❌ **Fora do intervalo:** `5 0 8 1`
```
❌ Posições devem estar entre 0 e 7.
```

❌ **Movimento inválido:** `5 0 5 1` (movimento horizontal, não diagonal)
```
❌ Essa jogada é inválida! Verifique:
   - A peça pertence a você?
   - O movimento é diagonal?
   - A posição de destino está livre?
   - Peças normais só avançam (não voltam)
```

---

## Sair do Jogo

During any move, player can type `sair`:

```
Alice - Digite a jogada (l1 c1 l2 c2) ou 'sair': sair

Tem certeza que deseja sair? (s/n): s
Jogo cancelado pelo jogador.
```

Se digitar `n`, volta ao jogo normalmente.

---

## Fim do Jogo

```
❌ Essa jogada é inválida!

==============================
🎉 JOGO TERMINADO!
VENCEDOR: Alice
==============================
```

Após terminar, volta ao menu principal.

---

## Recursos Implementados

✅ **Menu extensível** - Fácil adicionar mais jogos (opção 2, 3, etc)  
✅ **Entrada de nomes** - Personalização do jogo  
✅ **Validação de entrada** - Múltiplas camadas de verificação  
✅ **Tratamento de erros** - Mensagens claras, não cancela o jogo  
✅ **Opção de saída** - Em qualquer momento com confirmação  
✅ **Interface amigável** - Símbolos (✓, ❌, 🎉) e formatação clara  

---

## Exemplo de Sessão Completa

```
========================================
JOGOS DE TABULEIRO
========================================
1. Damas
9. Sair
========================================
Escolha uma opção: 1

========================================
CONFIGURAÇÃO DO JOGO
========================================
Nome do Jogador 1 (Peças de cima): Alice
Nome do Jogador 2 (Peças de baixo): Bob

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

Bob - Digite a jogada (l1 c1 l2 c2) ou 'sair': 2 1 3 0

[... jogo continua ...]
```

---

## Como Estender para Novos Jogos

1. Implementar o novo jogo em `src/jogos/novo_jogo.py`
2. Adicionar caso no menu:

```python
def menu_principal():
    print("\n" + "="*40)
    print("JOGOS DE TABULEIRO")
    print("="*40)
    print("1. Damas")
    print("2. Xadrez")  # ← Novo jogo
    print("9. Sair")
    print("="*40)
    
    while True:
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            return "damas"
        elif escolha == "2":  # ← Novo jogo
            return "xadrez"
        elif escolha == "9":
            return "sair"
        else:
            print("Opção inválida.")
```

3. Adicionar função de execução:

```python
elif jogo_escolhido == "xadrez":
    nome1, nome2 = obter_nomes_jogadores()
    executar_xadrez(nome1, nome2)
```

---

## Testes

Todos os testes passam:

```bash
# Testes unitários
python -m unittest tests.test_damas -v

# Testes manuais
python -m tests.test_manual
```

Resultado: **✅ 11 + 5 testes passando**
