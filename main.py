import os
import yt_dlp

def check_ffmpeg_path(ffmpeg_path):
    #Download ffmpeg jika tidak tersedia
    #Letakkan ffmpeg di folder yang sama dengan script
    """Memeriksa apakah ffmpeg tersedia di jalur yang diberikan."""
    if not os.path.exists(ffmpeg_path):
        print(f"FFmpeg tidak ditemukan di {ffmpeg_path}. Pastikan jalur sudah benar.")
        return False
    return True

def download_youtube_video(youtube_url, format_choice, quality_choice, quality_audio):
    
    # Path ffmpeg
    ffmpeg_path = os.path.abspath(r'ffmpeg\bin\ffmpeg.exe')

    # Memeriksa apakah ffmpeg tersedia
    if not check_ffmpeg_path(ffmpeg_path):
        return

    # Opsi dasar untuk yt-dlp
    ydl_opts = {
        'outtmpl': os.path.join('Downloads', '%(title)s.%(ext)s'),
        'noplaylist': True,
        'ffmpeg_location': ffmpeg_path
    }

    # Konfigurasi untuk format dan kualitas
    if format_choice == 'video':
        if quality_choice == 'high':
            ydl_opts.update({'format': 'bestvideo+bestaudio/best', 'merge_output_format': 'mp4'})
        elif quality_choice == 'medium':
            ydl_opts.update({'format': '137+bestaudio/best', 'merge_output_format': 'mp4'})
        elif quality_choice == 'low':
            ydl_opts.update({'format': '18', 'merge_output_format': 'mp4'})
    elif format_choice == 'audio':
        if quality_audio == 'super':
            ydl_opts.update({'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'flac'}]})
        elif quality_audio == 'high':
            ydl_opts.update({'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'}]})
        elif quality_audio == 'medium':
            ydl_opts.update({'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]})
        elif quality_audio == 'low':
            ydl_opts.update({'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '64'}]})    

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print("\nDownload selesai!")
    except Exception as e:
        print(f"Terjadi kesalahan saat mendownload: {e}")

def main():
    print("=== YouTube Downloader ===")
    youtube_url = input("Masukkan URL video YouTube: ").strip()

    if not youtube_url:
        print("URL tidak boleh kosong!")
        return

    print("\nPilih format download:")
    print("1. Video")
    print("2. Audio")
    format_choice = input("Pilihan (1/2): ").strip()

    if format_choice == '1':
        format_choice = 'video'
    elif format_choice == '2':
        format_choice = 'audio'
    else:
        print("Pilihan tidak valid!")
        return

    quality_choice = None
    if format_choice == 'video':
        print("\nPilih kualitas video:")
        print("1. High (1080p atau lebih tinggi)")
        print("2. Medium (720p)")
        print("3. Low (360p)")
        quality_choice = input("Pilihan (1/2/3): ").strip()

        if quality_choice == '1':
            quality_choice = 'high'
        elif quality_choice == '2':
            quality_choice = 'medium'
        elif quality_choice == '3':
            quality_choice = 'low'
        else:
            print("Pilihan tidak valid!")
            return

    quality_audio = None
    if format_choice == 'audio':
        print("\nPilih kualitas audio:")
        print("1. Super High (Flac 1000 kbps atau lebih tinggi)")
        print("2. High (Mp3 320 kbps atau lebih tinggi)")
        print("3. Medium (Mp3 192 kbps)")
        print("4. Low (Mp3 64 kbps)")
        quality_audio = input("Pilihan (1/2/3/4): ").strip()

        if quality_audio == '1':
            quality_audio = 'super'
        elif quality_audio == '2':
            quality_audio = 'high'
        elif quality_audio == '3':
            quality_audio = 'medium'
        elif quality_audio == '4':
            quality_audio = 'low'
        else:
            print("Pilihan tidak valid!")
            return

    download_youtube_video(youtube_url, format_choice, quality_choice, quality_audio)

if __name__ == "__main__":
    main()
