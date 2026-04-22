from abc import ABC, abstractmethod

class JogoTabuleiro(ABC):
    """Classe abstrata que representa um jogo de tabuleiro genérico."""
    
    def __init__(self, nome, jogador1, jogador2):
        self._nome = nome
        self._jogadores = [jogador1, jogador2]
        self._turno_atual = 0
        self._jogo_ativo = False
        self._tabuleiro = None
        self._historico_jogadas = []
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def jogadores(self):
        return self._jogadores
    
    @property
    def turno_atual(self):
        return self._turno_atual
    
    @property
    def jogador_atual(self):
        return self._jogadores[self._turno_atual % 2]
    
    @property
    def jogo_ativo(self):
        return self._jogo_ativo
    
    @abstractmethod
    def inicializar(self):
        """Inicializa o jogo."""
        pass
    
    @abstractmethod
    def validar_jogada(self, jogada):
        """Valida se uma jogada é legal."""
        pass
    
    @abstractmethod
    def aplicar_jogada(self, jogada):
        """Aplica uma jogada ao tabuleiro."""
        pass
    
    @abstractmethod
    def verificar_fim_de_jogo(self):
        """Verifica se o jogo terminou e retorna (terminou, vencedor)."""
        pass
    
    def executar_turno(self, jogada):
        """Executa um turno completo."""
        if not self._jogo_ativo:
            raise RuntimeError("Jogo não foi inicializado")
        
        if not self.validar_jogada(jogada):
            raise ValueError("Jogada inválida")
        
        self.aplicar_jogada(jogada)
        self._historico_jogadas.append(jogada)
        
        terminou, vencedor = self.verificar_fim_de_jogo()
        if terminou:
            self._jogo_ativo = False
            return terminou, vencedor
        
        self._trocar_turno()
        return False, None
    
    def _trocar_turno(self):
        """Muda o turno para o próximo jogador."""
        self._turno_atual += 1
    
    @abstractmethod
    def exibir_estado(self):
        """Exibe o estado atual do jogo."""
        pass
