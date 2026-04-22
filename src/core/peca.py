class Peca:
    """Representa uma peça no tabuleiro."""
    
    def __init__(self, jogador_id, tipo="normal"):
        self._jogador_id = jogador_id
        self._tipo = tipo
    
    @property
    def jogador_id(self):
        return self._jogador_id
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo
    
    def promover(self):
        """Promove a peça para um tipo especial (ex: rei em damas)."""
        if self._tipo == "normal":
            self._tipo = "especial"
    
    def __str__(self):
        return f"Peca(jogador={self._jogador_id}, tipo={self._tipo})"
    
    def __repr__(self):
        return f"Peca(jogador_id={self._jogador_id}, tipo={self._tipo})"
