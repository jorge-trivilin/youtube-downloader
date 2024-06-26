# YouTube Audio & MP4 Downloader

*This Python project allows you to download both the highest quality audio stream and MP4 video from public YouTube videos. It provides a convenient way to extract audio and video content for offline enjoyment or further processing.*

![Version](https://img.shields.io/badge/version-1.0.0-blue)

*This project was created by Jorge Trivilin.* 

*Connect with Jorge here:*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Jorge_Trivilin-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/jorgetrivilin/)

**Features:**
- Downloads the highest quality audio stream available in MP3 format.
- Downloads the highest quality MP4 video with audio.
- Offers flexibility by providing separate functions for audio and video downloads.

**Files:**

- `downloader.py`: Contains the core functions for downloading audio and MP4 videos from YouTube.
- `main.py:` Provides an example of how to use the downloader functions to download audio and video from a specific YouTube ideo URL.
-  `__pycache__`: This directory stores compiled Python bytecode files and can be ignored.

**Installation:**

- Make sure you have Python 3 installed.
- Install the Pytube library:


```
pip install pytube
```

**How to Use:**

1. Clone the repository:

```
git clone https://github.com/your-username/your-repository.git
```

2. Import the functions:
In your Python script, import the necessary functions from `downloader.py`:

```
from downloader import baixar_audio, baixar_mp4
```

3.  Download audio:  
```
url = "https://www.youtube.com/watch?v=VIDEO_ID"
caminho_saida = "/path/to/save/audio.mp3"  # Specify desired path and filename

baixar_audio(url, caminho_saida)
```

4. Download MP4 video:
```
url = "https://www.youtube.com/watch?v=VIDEO_ID"
caminho_saida = "/path/to/save/video.mp4"  # Specify desired path and filename

baixar_mp4(url, caminho_saida)
```

**Images:**

![image](https://github.com/jorge-trivilin/youtube-downloader/assets/84451671/b73f69b7-1a72-41d9-99b8-5de9b749c9b2)

![image](https://github.com/jorge-trivilin/youtube-downloader/assets/84451671/08394051-56e1-415b-b2f9-3559fb960ef6)


