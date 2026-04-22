from src.core import JogoTabuleiro, Peca, Jogada
from .tabuleiro_damas import TabuleiroDamas

class Damas(JogoTabuleiro):
    """Implementação do jogo de damas clássico."""
    
    def __init__(self, jogador1, jogador2):
        super().__init__("Damas", jogador1, jogador2)
        self._tabuleiro = TabuleiroDamas()
        self._pecas_capturadas = [[], []]
    
    def inicializar(self):
        """Setup inicial: coloca peças no tabuleiro."""
        self._posicionar_pecas()
        self._jogo_ativo = True
    
    def _posicionar_pecas(self):
        """Posiciona as 12 peças de cada jogador."""
        for linha in range(3):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    self._tabuleiro.colocar_peca(linha, coluna, Peca(1))
        
        for linha in range(5, 8):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    self._tabuleiro.colocar_peca(linha, coluna, Peca(0))
    
    def validar_jogada(self, jogada):
        """Valida se a jogada é legal."""
        linha_init, col_init = jogada.inicio
        linha_fim, col_fim = jogada.fim
        
        peca = self._tabuleiro.obter_peca(linha_init, col_init)
        
        if peca is None or peca.jogador_id != self.jogador_atual.id:
            return False
        
        if self._tabuleiro.obter_peca(linha_fim, col_fim) is not None:
            return False
        
        direcao_linha = linha_fim - linha_init
        direcao_coluna = col_fim - col_init
        
        if abs(direcao_coluna) != abs(direcao_linha):
            return False
        
        passos = abs(direcao_linha)
        
        if passos == 1:
            if peca.tipo == "normal" and self._movimento_invalido_direcao(peca, direcao_linha):
                return False
            return True
        
        elif passos == 2:
            linha_captura = linha_init + direcao_linha // 2
            col_captura = col_init + direcao_coluna // 2
            peca_capturada = self._tabuleiro.obter_peca(linha_captura, col_captura)
            
            if peca_capturada is None or peca_capturada.jogador_id == peca.jogador_id:
                return False
            
            if peca.tipo == "normal" and self._movimento_invalido_direcao(peca, direcao_linha):
                return False
            
            return True
        
        return False
    
    def _movimento_invalido_direcao(self, peca, direcao_linha):
        """Peças normais só podem avançar, não voltar."""
        id_jogador = peca.jogador_id
        if id_jogador == 0 and direcao_linha > 0:
            return True
        if id_jogador == 1 and direcao_linha < 0:
            return True
        return False
    
    def aplicar_jogada(self, jogada):
        """Aplica a jogada ao tabuleiro."""
        linha_init, col_init = jogada.inicio
        linha_fim, col_fim = jogada.fim
        
        peca = self._tabuleiro.remover_peca(linha_init, col_init)
        self._tabuleiro.colocar_peca(linha_fim, col_fim, peca)
        
        direcao_linha = linha_fim - linha_init
        if abs(direcao_linha) == 2:
            linha_captura = linha_init + direcao_linha // 2
            col_captura = col_init + (col_fim - col_init) // 2
            peca_capturada = self._tabuleiro.remover_peca(linha_captura, col_captura)
            jogada.marcar_captura(peca_capturada)
            self._pecas_capturadas[peca.jogador_id].append(peca_capturada)
        
        if (peca.jogador_id == 0 and linha_fim == 7) or (peca.jogador_id == 1 and linha_fim == 0):
            peca.promover()
    
    def verificar_fim_de_jogo(self):
        """Verifica se o jogo terminou."""
        for jogador_idx in range(2):
            if self._contar_pecas(jogador_idx) == 0:
                vencedor = self._jogadores[1 - jogador_idx]
                return True, vencedor
        
        if not self._tem_jogadas_validas(self.jogador_atual):
            vencedor = self._jogadores[1 - self.turno_atual % 2]
            return True, vencedor
        
        return False, None
    
    def _contar_pecas(self, jogador_id):
        """Conta peças de um jogador no tabuleiro."""
        count = 0
        for linha in range(8):
            for coluna in range(8):
                peca = self._tabuleiro.obter_peca(linha, coluna)
                if peca and peca.jogador_id == jogador_id:
                    count += 1
        return count
    
    def _tem_jogadas_validas(self, jogador):
        """Verifica se um jogador tem alguma jogada válida."""
        for linha in range(8):
            for coluna in range(8):
                peca = self._tabuleiro.obter_peca(linha, coluna)
                if peca and peca.jogador_id == jogador.id:
                    if self._peca_tem_jogadas(linha, coluna):
                        return True
        return False
    
    def _peca_tem_jogadas(self, linha, coluna):
        """Verifica se uma peça tem jogadas válidas."""
        for nova_linha in range(8):
            for nova_coluna in range(8):
                jogada = Jogada(linha, coluna, nova_linha, nova_coluna)
                if self.validar_jogada(jogada):
                    return True
        return False
    
    def exibir_estado(self):
        """Exibe o estado atual do jogo."""
        print(f"\n{'='*30}")
        print(f"Damas - Turno {self._turno_atual}")
        print(f"Jogador atual: {self.jogador_atual.nome}")
        print(f"{'='*30}")
        self._tabuleiro.exibir()
