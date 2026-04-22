from src.core import Jogador, Jogada
from src.jogos import Damas

def limpar_tela():
    """Limpa a tela do console."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """Exibe o menu principal e retorna a escolha."""
    print("\n" + "="*40)
    print("JOGOS DE TABULEIRO")
    print("="*40)
    print("1. Damas")
    print("9. Sair")
    print("="*40)
    
    while True:
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            return "damas"
        elif escolha == "9":
            return "sair"
        else:
            print("Opção inválida. Digite 1 ou 9.")

def obter_nomes_jogadores():
    """Obtém os nomes dos 2 jogadores."""
    print("\n" + "="*40)
    print("CONFIGURAÇÃO DO JOGO")
    print("="*40)
    
    while True:
        nome1 = input("Nome do Jogador 1 (Peças de baixo): ").strip()
        if nome1 and len(nome1) <= 20:
            break
        print("Nome inválido. Use até 20 caracteres.")
    
    while True:
        nome2 = input("Nome do Jogador 2 (Peças de cima): ").strip()
        if nome2 and len(nome2) <= 20:
            break
        print("Nome inválido. Use até 20 caracteres.")
    
    return nome1, nome2

def obter_entrada_jogada(jogador_atual):
    """Obtém uma jogada do usuário com sua validação."""
    while True:
        entrada = input(f"\n{jogador_atual.nome} - Digite a jogada (l1 c1 l2 c2) ou 'sair': ").strip()
        
        if entrada.lower() == "sair":
            return None
        
        partes = entrada.split()
        
        if len(partes) != 4:
            print("❌ Formato inválido. Use: l1 c1 l2 c2 (exemplo: 5 0 4 1)")
            continue
        
        try:
            linha_init, col_init, linha_fim, col_fim = [int(p) for p in partes]
            
            if not all(0 <= x < 8 for x in [linha_init, col_init, linha_fim, col_fim]):
                print("❌ Posições devem estar entre 0 e 7.")
                continue
            
            return (linha_init, col_init, linha_fim, col_fim)
        
        except ValueError:
            print("❌ Todos os valores devem ser números inteiros.")
            continue

def executar_damas(nome1, nome2):
    """Executa uma partida de damas."""
    print("\n" + "="*40)
    print("JOGO DE DAMAS")
    print("="*40)
    
    jogador1 = Jogador(0, nome1)
    jogador2 = Jogador(1, nome2)
    
    jogo = Damas(jogador1, jogador2)
    jogo.inicializar()
    jogo.exibir_estado()
    
    while jogo.jogo_ativo:
        jogada_dados = obter_entrada_jogada(jogo.jogador_atual)
        
        if jogada_dados is None:
            confirmacao = input("\nTem certeza que deseja sair? (s/n): ").strip().lower()
            if confirmacao == "s":
                print("Jogo cancelado pelo jogador.")
                return
            else:
                continue
        
        linha_init, col_init, linha_fim, col_fim = jogada_dados
        
        try:
            jogada = Jogada(linha_init, col_init, linha_fim, col_fim)
            
            if not jogo.validar_jogada(jogada):
                print("❌ Essa jogada é inválida! Verifique:")
                print("   - A peça pertence a você?")
                print("   - O movimento é diagonal?")
                print("   - A posição de destino está livre?")
                print("   - Peças normais só avançam (não voltam)")
                continue
            
            terminou, vencedor = jogo.executar_turno(jogada)
            jogo.exibir_estado()
            
            if terminou:
                print(f"\n{'='*40}")
                print(f"🎉 JOGO TERMINADO!")
                print(f"VENCEDOR: {vencedor.nome}")
                print(f"{'='*40}\n")
        
        except Exception as e:
            print(f"❌ Erro ao processar jogada: {e}")
            continue

def main():
    """Função principal do programa."""
    while True:
        jogo_escolhido = menu_principal()
        
        if jogo_escolhido == "sair":
            print("\nObrigado por jogar! Até logo!")
            break
        
        elif jogo_escolhido == "damas":
            nome1, nome2 = obter_nomes_jogadores()
            executar_damas(nome1, nome2)

if __name__ == "__main__":
    main()
