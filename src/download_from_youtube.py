from yt_dlp import YoutubeDL
from src.log import get_logger

logger = get_logger(__name__)

def download_from_youtube(url=None, proxy=None, output_dir="output"):
    # 验证输入URL
    if not url:
        logger.error("No URL provided for downloading.")
        return
    
    URLS = url.split("\n")
    URLS = [url.strip() for url in URLS if url.strip()]  # 去除空白项
    
    # 设置下载选项
    ydl_opts = {
        "proxy": proxy,
        "paths": {"home": output_dir},
    }
    
    try:
        # 创建 YoutubeDL 实例并下载
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)
        logger.info("Download completed.")
    except Exception as e:
        logger.error(f"Failed to download: {e}")
