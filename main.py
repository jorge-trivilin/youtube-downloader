# baixar audio
import os
from downloader import baixar_audio, baixar_mp4 



url = "https://www.youtube.com/watch?v=scPBmrzdD0g"
caminho_saida =os.environ['pytube_videos']
baixar_audio(url, caminho_saida)

# baixar mp4
url = "https://www.youtube.com/watch?v=scPBmrzdD0g"
caminho_saida =os.environ['pytube_videos']
baixar_mp4(url, caminho_saida)
