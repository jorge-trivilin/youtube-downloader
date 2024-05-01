# YouTube Audio & MP4 Downloader

**Description:**
*This Python project allows you to download both the highest quality audio stream and MP4 video from public YouTube videos. It provides a convenient way to extract audio and video content for offline enjoyment or further processing.*

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

**License:**

This project is licensed under the MIT License.
