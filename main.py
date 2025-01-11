import os
from downloader import baixar_audio, baixar_mp4

def validar_url(url):
    """Valida se a URL fornecida é do YouTube."""
    return url.startswith(('https://www.youtube.com/', 'https://youtu.be/'))

def obter_caminho_saida():
    """Obtém o caminho de saída dos arquivos, com fallback para diretório atual."""
    try:
        return os.environ['pytube_videos']
    except KeyError:
        caminho_padrao = os.path.join(os.getcwd(), 'downloads')
        os.makedirs(caminho_padrao, exist_ok=True)
        return caminho_padrao

def main():
    print("\n=== YouTube Downloader ===")
    while True:
        print("\n1. Baixar Áudio (MP3)")
        print("2. Baixar Áudio (WAV)")
        print("3. Baixar Vídeo (MP4)")
        print("4. Sair")

        try:
            opcao = input("\nEscolha uma opção (1-4): ").strip()
            
            if opcao == '4':
                print("\nEncerrando o programa...")
                break
                
            if opcao not in ['1', '2', '3']:
                print("Opção inválida! Escolha 1, 2, 3 ou 4.")
                continue

            url = input("\nInsira o link do YouTube: ").strip()
            
            if not validar_url(url):
                print("URL inválida! Insira um link válido do YouTube.")
                continue

            caminho_saida = obter_caminho_saida()
            
            sucesso = False
            if opcao == '1':
                sucesso = baixar_audio(url, caminho_saida, formato='mp3')
            elif opcao == '2':
                sucesso = baixar_audio(url, caminho_saida, formato='wav')
            else:
                sucesso = baixar_mp4(url, caminho_saida)

            if sucesso:
                continuar = input("\nDeseja baixar outro arquivo? (s/n): ").lower()
                if continuar != 's':
                    print("\nEncerrando o programa...")
                    break
            else:
                print("\nTente novamente ou escolha outra opção.")

        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            print("Tente novamente.")

if __name__ == "__main__":
    main()