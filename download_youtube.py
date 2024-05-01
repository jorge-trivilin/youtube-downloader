# importing the libraries after pip install pytube



#on_progress_callback=progress_func =  # permite passar função que será chamada sempre que um ppedaço (chunk) dos dados for baixado do vídeo. A função será chamada com três argumentos: stream (fluxo) dos dados, o pedaço de dados que foi baixado e a quantidade de bytes restantes do vídeo. Isso é útil para exibir por exemplo uma barra de progresso.

 #on_complete_callback=complete_func =  permite passar uma função que será chamada depois que o vídeo for baixado. a função será chamada com dois argumentos: o stream (fluxo) de dados e o caminho do arquivo onde o vídeo foi salvo. isso pode ser útil por exemplo para executar algum processo após o download, como cortar o vídeo. 

 #proxies=my_proxies =  esse argumento permite passar um dicionário de proxies que serão usados para fazer a requisição HTTP para o YouTube. Pode ser útil em caso de usar um firewall ou ocultar o endereço IP.                

# use_oauth e allow_oauth_cache são sinalizadores (flags) que controlam se o Pytube deve ou nãor usar o OAuth para autenticar com a sua conta do Youtube. Se use_oauth for definido como True, o Pytube será autorizado a interagir com o Youtube no seu nome, permitindo por exemplo acessar vídeos privados ou listas de reprodução restritas. Se allow oauth cache for definido como True, será solicitado a autenticar uma avoz, depois o pytube armazena em cache os tokens necessários para agir em meu nome. se for False, será solicitado a autenticar novamente a cada ação que exigir autenticação.

"""API youtube e credenciais"""


from pytube import YouTube  # Para download de vídeos do YouTube






# yt = YouTube(
#        'https://www.youtube.com/watch?v=qVEs5Y_UAvo',
#        on_progress_callback=progress_func,  
#        on_complete_callback=complete_func,         
#        proxies=my_proxies,         
#        use_oauth=False,  
#        allow_oauth_cache=True 
#        ) 




from pytube import YouTube


yt = YouTube(
        'https://www.youtube.com/watch?v=3ttO_giGpgs') 





# using the pytube API to get the name of the video

yt.title

print(yt.title)

# using the API to get the thumbnail url

yt.thumbnail_url  

print(yt.thumbnail_url)


"""
    O Youtube utiliza duas técnicas de streaming: DASH e Progressiva. 
    DASH divide os trilhos de áudio e vídeo, proporcionando melhor qualidade
    Progressive é um único arquivo para áudio e vídeo mas oferece menos qualidade. O PYTUBE suporta a   mbas as técnicas.

Filtragem de streams
    - O Pytube permite filtrar streams com o método `.filter()`
    - é possível filtrar por tipo de stream (progressive ou adptive), por exemplo
    - Streams adaptativos são divididos em áudio e vídeo, enquanto streams progressivos são um único arquivo. 

    - usar `filter(progressive=True)` para obter streams progressivos
    - usar `.filter(adaptive=True)`para filtrar stream adaptativos. 

Filtragem somente de audio:
    - usar `.filter(only_audio=True)` para obter somente audio
Download de streams:
    - Após selecionar a stream desejada, usar o método `download()`para baixar o arquivo.
"""

yt.streams

# print(yt.streams)

"""
Filtrando DASH  streams e imprimindo elas,
usando o método .all() para obter uma lista de
todas as streams filtradas 
"""

yt_dash = yt.streams.filter(
        adaptive=True).all()
print("Dash Streams:")
for stream in yt_dash:
    print(stream)

"""
Filtrando streams progressivas e imprimindo elas
"""

yt_progressive = yt.streams.filter(progressive=True)  


yt_audio = yt.streams.filter(
        only_audio=True).order_by('abr').desc()  # filtrando somente o audio
print("Audio Only Streams:")
for stream in yt_audio:
    print(stream)

# DOWNLOAD AUDIO

"""Downloading stream de audio"""
if yt_audio:
    audio = yt_audio[0] # seleciona a primeira stream
    file_path_audio = audio.download(
            output_path='/home/jorgetrivilin/Videos/pytube_videos', filename=yt.title +".mp3"
            )
    print("Stream de audio baixada em:{}".format(file_path_audio))
else:
    print("Nenhuma stream de audio disponível para download.")

# DOWNLOAD MP4

yt_mp4 = yt.streams.filter(
        progressive=True,
        file_extension='mp4')  # filtrando streams no formato mp4
if yt_mp4:
    yt_mp4 = yt_mp4.order_by('resolution').desc() # ordenando streams pela resolução desc
    # baixando a primeira stream de maior qualidade
    mp4 = yt_mp4.first()
    file_path_mp4 = mp4.download(
            output_path='/home/jorgetrivilin/Videos/pytube_videos', filename=yt.title + ".mp4"
            )
    print("MP4 baixado em:{}".format(file_path_mp4))
else:
    print("Nenhuma Stream MP4 disponível para download")


