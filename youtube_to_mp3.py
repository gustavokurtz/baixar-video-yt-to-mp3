# youtube_to_mp3_with_ytdlp.py

import os
import yt_dlp as youtube_dl
from pydub import AudioSegment
from pydub.utils import which

# Configurar o ffmpeg para pydub
AudioSegment.converter = which("ffmpeg")

def download_youtube_video_as_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloaded_audio.%(ext)s',
        'quiet': True
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Renomeia o arquivo baixado para o nome de saída desejado
        os.rename('downloaded_audio.mp3', output_path)
        print(f"Download e conversão concluídos. Arquivo salvo como {output_path}")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    output_path = input("Digite o nome do arquivo de saída (com extensão .mp3): ")
    download_youtube_video_as_audio(url, output_path)
