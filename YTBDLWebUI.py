# YTBDLWebUI.py
# --coding:utf-8--
# Time:2024-09-17 08:14:40
# Author:Luckykefu
# Email:3124568493@qq.com
# Description:

import os
import gradio as gr
import argparse
from src.download_from_youtube import download_from_youtube
from src.log import get_logger

logger = get_logger(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
template_path = os.path.join(dir_path, "temp")


def main():

    # Define the interface
    with gr.Blocks() as demo:
        with gr.TabItem("YTBDL"):
            gr.Markdown("## YTBDL")
            ytb_url = gr.Textbox(
                label="Youtube URL",
                lines=1,
                value="https://www.youtube.com/watch?v=qASkoV5TsAg",
            )
            proxy_arg = gr.Textbox(
                label="Proxy", lines=1, value="socks5://192.168.43.1:1088"
            )
            ytb_output_dir = gr.Textbox(label="Output Dir", value=template_path)
            download_btn = gr.Button("Download")
            download_btn.click(
                fn=download_from_youtube,
                inputs=[ytb_url, proxy_arg, ytb_output_dir],
                outputs=[],
            )

    # Launch the interface
    parser = argparse.ArgumentParser(description="Demo")
    parser.add_argument(
        "--server_name", type=str, default="localhost", help="server name"
    )
    parser.add_argument("--server_port", type=int, default=8080, help="server port")
    parser.add_argument("--root_path", type=str, default=None, help="root path")
    args = parser.parse_args()

    demo.launch(
        server_name=args.server_name,
        server_port=args.server_port,
        root_path=args.root_path,
        show_api=False,
    )


if __name__ == "__main__":
    main()
