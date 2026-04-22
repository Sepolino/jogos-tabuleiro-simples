class Jogador:
    """Representa um jogador no jogo de tabuleiro."""
    
    def __init__(self, id_jogador, nome):
        self._id = id_jogador
        self._nome = nome
        self._ativo = True
    
    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def ativo(self):
        return self._ativo
    
    def desativar(self):
        """Marca o jogador como inativo (derrotado)."""
        self._ativo = False
    
    def ativar(self):
        """Marca o jogador como ativo."""
        self._ativo = True
    
    def __str__(self):
        return f"Jogador({self._nome})"
    
    def __repr__(self):
        return f"Jogador(id={self._id}, nome={self._nome})"
