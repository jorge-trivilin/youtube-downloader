from pytube import YouTube

def baixar_audio(url, caminho_saida):
    """Baixa a stream de áudio com maior qualidade de um vídeo do YouTube.

    Args:
        url (str): A URL do vídeo do YouTube.
        caminho_saida (str): O caminho para salvar o arquivo de áudio.
    """

    try:
        yt = YouTube(url)
        
        # Filtrar streams de áudio e ordenar por bitrate
        streams_audio = yt.streams.filter(
                only_audio=True).order_by('abr').desc()

        # Baixar a stream de áudio com maior qualidade
        if streams_audio:
            audio = streams_audio.first()
            nome_arquivo = f"{yt.title}.mp3"
            caminho_arquivo = audio.download(
                    output_path=caminho_saida, filename=nome_arquivo)
            print(f"Stream de áudio baixada em: {caminho_arquivo}")
        else:
            print("Nenhuma stream de áudio disponível para download.")
    except Exception as e:
        print(f"Erro ao baixar o áudio: {e}")


def baixar_mp4(url, caminho_saida):
    """Baixa a stream de mp4 com audio.

    Args:
        url(str): A URL do vídeo do Youtube
        caminho_saida (str): O caminho para salvar o arquivo de áudio.
    """

    try:
        yt = YouTube(url)

        # filtrar streams usando progressive e buscando mp4
        streams_mp4 = yt.streams.filter(
                progressive=True,
                file_extension='mp4')  # filtrando streams
        # baixar a stream MP4 com a melhor resolução possível (progressive)
        if streams_mp4:
            streams_mp4 = streams_mp4.order_by('resolution').desc() # ordena streams pela res
            mp4 = streams_mp4.first()  # baixa a primeira stream de maior qualidade
            nome_arquivo = f"{yt.title}.mp4"
            caminho_arquivo = mp4.download(
                    output_path=caminho_saida, filename=nome_arquivo)
            print(f"Stream MP4 baixada em: {caminho_arquivo}")
        else:
            print("Nenhuma stream MP4 disponível para download.")
    except Exception as e:
        print(f"Erro ao baixar o MP4: {e}")








