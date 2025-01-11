import os
from pytubefix import YouTube  # Mudança principal: usando pytubefix ao invés de pytube

def validar_url(url):
    """Valida se a URL fornecida é do YouTube."""
    return url.startswith(('https://www.youtube.com/', 'https://youtu.be/'))

def baixar_audio(url, caminho_saida, formato='mp3'):
    """Baixa a stream de áudio com maior qualidade."""
    try:
        yt = YouTube(url)
        print(f"\nPrepando download de: {yt.title}")
        
        # Obtém todas as streams de áudio disponíveis
        streams_audio = yt.streams.filter(
            only_audio=True
        ).order_by('abr').desc()

        if not streams_audio:
            print("Nenhuma stream de áudio disponível.")
            return False

        # Mostra as qualidades disponíveis
        print("\nQualidades disponíveis:")
        for i, stream in enumerate(streams_audio, 1):
            print(f"{i}. {stream.abr} ({stream.mime_type})")

        # Permite o usuário escolher a qualidade
        while True:
            try:
                escolha = input(f"\nEscolha a qualidade (1-{len(streams_audio)}) [1 para maior qualidade]: ").strip()
                if not escolha:  # Se pressionar Enter, escolhe a maior qualidade
                    escolha = "1"
                indice = int(escolha) - 1
                if 0 <= indice < len(streams_audio):
                    audio = streams_audio[indice]
                    break
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Por favor, digite um número válido.")

        print(f"\nBaixando áudio em {audio.abr} ({audio.mime_type})")
        nome_arquivo = f"{yt.title}.{formato}"
        caminho_arquivo = audio.download(
            output_path=caminho_saida, 
            filename=nome_arquivo
        )
        print(f"✓ Download concluído: {caminho_arquivo}")
        return True
            
    except Exception as e:
        print(f"Erro no download: {str(e)}")
        return False

def baixar_mp4(url, caminho_saida):
    """Baixa a stream de vídeo MP4 com melhor qualidade."""
    try:
        yt = YouTube(url)
        print(f"\nPrepando download de: {yt.title}")

        streams_mp4 = yt.streams.filter(
            progressive=True,
            file_extension='mp4'
        ).order_by('resolution').desc()

        if streams_mp4:
            mp4 = streams_mp4.first()
            print(f"Qualidade do vídeo: {mp4.resolution}")
            nome_arquivo = f"{yt.title}.mp4"
            caminho_arquivo = mp4.download(
                output_path=caminho_saida,
                filename=nome_arquivo
            )
            print(f"✓ Download concluído: {caminho_arquivo}")
            return True
        else:
            print("Nenhuma stream MP4 disponível.")
            return False
            
    except Exception as e:
        print(f"Erro no download: {str(e)}")
        return False

def obter_caminho_saida():
    """Obtém o caminho de saída dos arquivos."""
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