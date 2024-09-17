
from yt_dlp import YoutubeDL



def download_from_youtube(url=None, proxy=None, output_dir='output'):
    # 代理服务器的地址和端口
    proxy = 'socks5://192.168.43.1:1088'

    # YouTube 视频的 URL
    URLS = url.split("\n")
    URLS = [url.strip() for url in URLS]
    # 设置下载选项
    ydl_opts = {
        'proxy': proxy,  # 代理服务器
        'paths': {'home': output_dir},  # 输出文件路径和命名规则
    }
    # 创建 YoutubeDL 实例
    with YoutubeDL(ydl_opts) as ydl:

        ydl.download(URLS)
    print("\nDownload completed.")
    return
if __name__ == '__main__':
    url = input("Enter the YouTube URL(s) separated by new line: ")
    proxy = 'socks5://192.168.43.1:1088'

    download_from_youtube(url)