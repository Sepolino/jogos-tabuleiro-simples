from abc import ABC, abstractmethod

class Tabuleiro(ABC):
    """Classe abstrata que representa um tabuleiro genérico."""
    
    def __init__(self, dimensoes):
        self._dimensoes = dimensoes
        self._celulas = self._criar_tabuleiro()
    
    @abstractmethod
    def _criar_tabuleiro(self):
        """Cria a estrutura do tabuleiro."""
        pass
    
    @property
    def dimensoes(self):
        return self._dimensoes
    
    def obter_peca(self, linha, coluna):
        """Retorna a peça em uma posição do tabuleiro."""
        if not self._posicao_valida(linha, coluna):
            return None
        return self._celulas[linha][coluna]
    
    def colocar_peca(self, linha, coluna, peca):
        """Coloca uma peça no tabuleiro."""
        if self._posicao_valida(linha, coluna):
            self._celulas[linha][coluna] = peca
    
    def remover_peca(self, linha, coluna):
        """Remove uma peça do tabuleiro."""
        if self._posicao_valida(linha, coluna):
            peca = self._celulas[linha][coluna]
            self._celulas[linha][coluna] = None
            return peca
        return None
    
    def _posicao_valida(self, linha, coluna):
        """Verifica se a posição está dentro dos limites."""
        return 0 <= linha < self._dimensoes and 0 <= coluna < self._dimensoes
    
    @abstractmethod
    def exibir(self):
        """Exibe o tabuleiro."""
        pass
