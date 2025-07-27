import yt_dlp
import os

# ইউটিউব প্লেলিস্ট URL
playlist_url = "https://www.youtube.com/playlist?list=PL0LcMeEuj9ffUHXnQcf88NspyU186A1b3"

# ডাউনলোড ফোল্ডার
output_dir = "Desktop\SSSSS"
os.makedirs(output_dir, exist_ok=True)

# yt-dlp অপশনস (MP3 রূপান্তর ছাড়াই)
ydl_opts = {
    'format': 'bestaudio[ext=m4a]/bestaudio/best',
    'outtmpl': f'{output_dir}/%(playlist_index)s_%(id)s.%(ext)s',
    'noplaylist': False,
    'quiet': False,
    'no_warnings': True
}

# ডাউনলোড শুরু
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("✅ Download done! Files are in .m4a or .webm format.")
