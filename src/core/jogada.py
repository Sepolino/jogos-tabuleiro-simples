class Jogada:
    """Representa uma jogada: movimento de uma peça."""
    
    def __init__(self, linha_inicio, coluna_inicio, linha_fim, coluna_fim):
        self._linha_inicio = linha_inicio
        self._coluna_inicio = coluna_inicio
        self._linha_fim = linha_fim
        self._coluna_fim = coluna_fim
        self._captura_peca = None
    
    @property
    def inicio(self):
        return (self._linha_inicio, self._coluna_inicio)
    
    @property
    def fim(self):
        return (self._linha_fim, self._coluna_fim)
    
    @property
    def captura_peca(self):
        return self._captura_peca
    
    def marcar_captura(self, peca):
        """Marca uma peça capturada nesta jogada."""
        self._captura_peca = peca
    
    def __str__(self):
        return f"({self._linha_inicio},{self._coluna_inicio}) -> ({self._linha_fim},{self._coluna_fim})"
    
    def __repr__(self):
        return f"Jogada{self}"
