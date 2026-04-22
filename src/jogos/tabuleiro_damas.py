from src.core import Tabuleiro, Peca

class TabuleiroDamas(Tabuleiro):
    """Tabuleiro 8x8 com cores alternadas para o jogo de damas."""
    
    DIMENSAO = 8
    
    def __init__(self):
        super().__init__(self.DIMENSAO)
    
    def _criar_tabuleiro(self):
        """Cria tabuleiro 8x8 vazio."""
        return [[None for _ in range(self.DIMENSAO)] for _ in range(self.DIMENSAO)]
    
    def _eh_posicao_jogavel(self, linha, coluna):
        """Apenas quadrados escuros são jogáveis em damas."""
        return (linha + coluna) % 2 == 1
    
    def exibir(self):
        """Exibe o tabuleiro formatado."""
        print("\n  0 1 2 3 4 5 6 7")
        for linha in range(self.DIMENSAO):
            print(f"{linha} ", end="")
            for coluna in range(self.DIMENSAO):
                peca = self._celulas[linha][coluna]
                if peca is None:
                    print(". " if self._eh_posicao_jogavel(linha, coluna) else "# ", end="")
                elif peca.tipo == "especial":
                    print("R " if peca.jogador_id == 0 else "r ", end="")
                else:
                    print("O " if peca.jogador_id == 0 else "o ", end="")
            print()
        print()
