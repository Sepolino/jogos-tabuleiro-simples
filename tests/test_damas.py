import unittest
from src.core import Jogador, Peca, Jogada
from src.jogos import Damas

class TestDamas(unittest.TestCase):
    
    def setUp(self):
        self.jogador1 = Jogador(0, "Teste1")
        self.jogador2 = Jogador(1, "Teste2")
        self.jogo = Damas(self.jogador1, self.jogador2)
        self.jogo.inicializar()
    
    def test_inicializar_jogo(self):
        """Testa se o jogo inicia com o estado correto."""
        self.assertTrue(self.jogo.jogo_ativo)
        self.assertEqual(self.jogo.turno_atual, 0)
        self.assertEqual(self.jogo.jogador_atual.id, 0)
    
    def test_validar_jogada_invalida_peca_nao_existe(self):
        """Testa rejeição de jogada onde não há peça."""
        jogada = Jogada(4, 4, 5, 5)
        self.assertFalse(self.jogo.validar_jogada(jogada))
    
    def test_validar_movimento_simples(self):
        """Testa rejeição de movimento inválido."""
        jogada = Jogada(5, 0, 4, 1)
        self.assertTrue(self.jogo.validar_jogada(jogada))
    
    def test_validar_movimento_peca_jogador0(self):
        """Testa movimento válido de peça do jogador 0."""
        jogada = Jogada(5, 0, 4, 1)
        self.assertTrue(self.jogo.validar_jogada(jogada))
    
    def test_rejeita_movimento_peca_adversario(self):
        """Testa se rejeita movimento da peça do adversário."""
        jogada = Jogada(2, 1, 3, 2)
        self.assertFalse(self.jogo.validar_jogada(jogada))
    
    def test_rejeita_movimento_para_posicao_ocupada(self):
        """Testa se rejeita movimento para posição ocupada."""
        jogada = Jogada(5, 0, 4, 1)
        self.assertTrue(self.jogo.validar_jogada(jogada))
        self.jogo.aplicar_jogada(jogada)
        
        jogada2 = Jogada(2, 1, 3, 0)
        self.jogo._turno_atual += 1
        self.assertTrue(self.jogo.validar_jogada(jogada2))
        self.jogo.aplicar_jogada(jogada2)
        
        jogada3 = Jogada(4, 1, 3, 0)
        self.jogo._turno_atual += 1
        self.assertFalse(self.jogo.validar_jogada(jogada3))
    
    def test_aplicar_jogada_simples(self):
        """Testa aplicação de uma jogada simples."""
        jogada = Jogada(5, 0, 4, 1)
        self.jogo.aplicar_jogada(jogada)
        
        peca_nova = self.jogo._tabuleiro.obter_peca(4, 1)
        self.assertIsNotNone(peca_nova)
        self.assertEqual(peca_nova.jogador_id, 0)
        self.assertIsNone(self.jogo._tabuleiro.obter_peca(5, 0))
    
    def test_captura_de_peca(self):
        """Testa captura de uma peça adversária."""
        peca_player0 = Peca(0)
        peca_player1 = Peca(1)
        
        self.jogo._tabuleiro.remover_peca(5, 0)
        self.jogo._tabuleiro.remover_peca(2, 1)
        self.jogo._tabuleiro.remover_peca(2, 3)
        
        self.jogo._tabuleiro.colocar_peca(4, 1, peca_player0)
        self.jogo._tabuleiro.colocar_peca(3, 2, peca_player1)
        
        jogada_captura = Jogada(4, 1, 2, 3)
        self.assertTrue(self.jogo.validar_jogada(jogada_captura))
        self.jogo.aplicar_jogada(jogada_captura)
        
        self.assertEqual(len(self.jogo._pecas_capturadas[0]), 1)
        self.assertIsNone(self.jogo._tabuleiro.obter_peca(3, 2))
    
    def test_peca_normal_nao_anda_para_trás(self):
        """Testa se peça normal não consegue voltar."""
        peca = self.jogo._tabuleiro.obter_peca(5, 0)
        self.assertEqual(peca.tipo, "normal")
        
        jogada = Jogada(5, 0, 6, 1)
        self.assertFalse(self.jogo.validar_jogada(jogada))
    
    def test_promocao_peca(self):
        """Testa promoção de peça ao chegar no final."""
        peca = Peca(0)
        self.jogo._tabuleiro.colocar_peca(6, 1, peca)
        
        jogada = Jogada(6, 1, 7, 0)
        self.jogo._turno_atual = 0
        self.jogo.aplicar_jogada(jogada)
        
        peca_promovida = self.jogo._tabuleiro.obter_peca(7, 0)
        self.assertEqual(peca_promovida.tipo, "especial")
    
    def test_turno_alterna(self):
        """Testa alternância de turnos."""
        self.assertEqual(self.jogo.jogador_atual.id, 0)
        
        jogada = Jogada(5, 0, 4, 1)
        self.jogo.executar_turno(jogada)
        
        self.assertEqual(self.jogo.jogador_atual.id, 1)

if __name__ == '__main__':
    unittest.main()
