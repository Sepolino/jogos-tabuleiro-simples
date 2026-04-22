"""Script de teste para validar o novo sistema de menu e entrada de dados."""

from src.core import Jogador, Jogada
from src.jogos import Damas

def testar_validacao_jogada():
    """Testa validação de movimentos no jogo de damas."""
    print("\n" + "="*50)
    print("TESTE 1: Validação de Movimentos")
    print("="*50)
    
    j1 = Jogador(0, "Teste1")
    j2 = Jogador(1, "Teste2")
    jogo = Damas(j1, j2)
    jogo.inicializar()
    
    # Teste 1: Movimento válido
    jogada = Jogada(5, 0, 4, 1)
    assert jogo.validar_jogada(jogada), "Movimento válido foi rejeitado"
    print("✓ Movimento válido (5,0) -> (4,1) aceito")
    
    # Teste 2: Movimento inválido (pegando peça do adversário)
    jogada_invalida = Jogada(2, 1, 3, 0)
    assert not jogo.validar_jogada(jogada_invalida), "Movimento do adversário foi aceito"
    print("✓ Movimento do adversário corretamente rejeitado")
    
    # Teste 3: Peça normal não pode voltar
    jogada_retrocesso = Jogada(5, 0, 6, 1)
    assert not jogo.validar_jogada(jogada_retrocesso), "Retrocesso foi aceito"
    print("✓ Retrocesso de peça normal corretamente rejeitado")
    
    print("\n✅ Todos os testes de validação passaram!")

def testar_fluxo_jogo():
    """Testa o fluxo básico de um jogo."""
    print("\n" + "="*50)
    print("TESTE 2: Fluxo de Jogo")
    print("="*50)
    
    j1 = Jogador(0, "Alice")
    j2 = Jogador(1, "Bob")
    jogo = Damas(j1, j2)
    jogo.inicializar()
    
    # Executar 3 movimentos
    movimentos = [
        (5, 0, 4, 1),
        (2, 1, 3, 0),
        (6, 1, 5, 0),
    ]
    
    for i, (l1, c1, l2, c2) in enumerate(movimentos):
        jogada = Jogada(l1, c1, l2, c2)
        assert jogo.validar_jogada(jogada), f"Movimento {i+1} foi rejeitado"
        terminou, vencedor = jogo.executar_turno(jogada)
        assert not terminou, f"Jogo terminou prematuramente no movimento {i+1}"
        print(f"✓ Movimento {i+1}: ({l1},{c1}) -> ({l2},{c2}) executado")
    
    assert jogo.turno_atual == 3, "Contagem de turnos incorreta"
    print(f"✓ Turno atual correto: {jogo.turno_atual}")
    
    print("\n✅ Fluxo de jogo validado com sucesso!")

def testar_alternancia_turnos():
    """Testa alternância de turnos entre jogadores."""
    print("\n" + "="*50)
    print("TESTE 3: Alternância de Turnos")
    print("="*50)
    
    j1 = Jogador(0, "Jogador1")
    j2 = Jogador(1, "Jogador2")
    jogo = Damas(j1, j2)
    jogo.inicializar()
    
    # Verificar jogador inicial
    assert jogo.jogador_atual.id == 0, "Jogador inicial incorreto"
    print(f"✓ Turno 1: {jogo.jogador_atual.nome} (id={jogo.jogador_atual.id})")
    
    # Primeiro movimento
    jogo.executar_turno(Jogada(5, 0, 4, 1))
    assert jogo.jogador_atual.id == 1, "Turno não alternado corretamente"
    print(f"✓ Turno 2: {jogo.jogador_atual.nome} (id={jogo.jogador_atual.id})")
    
    # Segundo movimento
    jogo.executar_turno(Jogada(2, 1, 3, 0))
    assert jogo.jogador_atual.id == 0, "Turno não voltou ao jogador 0"
    print(f"✓ Turno 3: {jogo.jogador_atual.nome} (id={jogo.jogador_atual.id})")
    
    print("\n✅ Alternância de turnos funcionando perfeitamente!")

def testar_captura():
    """Testa captura de peças."""
    print("\n" + "="*50)
    print("TESTE 4: Captura de Peças")
    print("="*50)
    
    from src.core import Peca
    
    j1 = Jogador(0, "Capturador")
    j2 = Jogador(1, "Alvo")
    jogo = Damas(j1, j2)
    jogo.inicializar()
    
    # Preparar cenário de captura
    jogo._tabuleiro.remover_peca(5, 0)
    jogo._tabuleiro.remover_peca(2, 1)
    jogo._tabuleiro.remover_peca(2, 3)
    
    jogo._tabuleiro.colocar_peca(4, 1, Peca(0))
    jogo._tabuleiro.colocar_peca(3, 2, Peca(1))
    
    # Validar captura
    jogada_captura = Jogada(4, 1, 2, 3)
    assert jogo.validar_jogada(jogada_captura), "Captura foi rejeitada"
    print("✓ Captura validada corretamente")
    
    # Executar captura
    jogo.aplicar_jogada(jogada_captura)
    assert len(jogo._pecas_capturadas[0]) == 1, "Peça não foi registrada como capturada"
    assert jogo._tabuleiro.obter_peca(3, 2) is None, "Peça capturada ainda existe"
    print("✓ Peça capturada foi removida do tabuleiro")
    print("✓ Captura registrada no histórico")
    
    print("\n✅ Sistema de captura funcionando corretamente!")

def testar_promocao():
    """Testa promoção de peças a reis."""
    print("\n" + "="*50)
    print("TESTE 5: Promoção de Peças")
    print("="*50)
    
    from src.core import Peca
    
    j1 = Jogador(0, "Promocao")
    j2 = Jogador(1, "Teste")
    jogo = Damas(j1, j2)
    jogo.inicializar()
    
    peca = Peca(0)
    jogo._tabuleiro.colocar_peca(6, 1, peca)
    
    assert peca.tipo == "normal", "Peça começou com tipo errado"
    print("✓ Peça criada com tipo 'normal'")
    
    jogada = Jogada(6, 1, 7, 0)
    jogo._turno_atual = 0
    jogo.aplicar_jogada(jogada)
    
    peca_promovida = jogo._tabuleiro.obter_peca(7, 0)
    assert peca_promovida.tipo == "especial", "Peça não foi promovida"
    print("✓ Peça chegou à borda oposta")
    print("✓ Peça promovida a 'rei'")
    
    print("\n✅ Sistema de promoção funcionando corretamente!")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("SUITE DE TESTES - SISTEMA COMPLETO")
    print("="*50)
    
    testar_validacao_jogada()
    testar_fluxo_jogo()
    testar_alternancia_turnos()
    testar_captura()
    testar_promocao()
    
    print("\n" + "="*50)
    print("✅ TODOS OS TESTES PASSARAM COM SUCESSO!")
    print("="*50 + "\n")
