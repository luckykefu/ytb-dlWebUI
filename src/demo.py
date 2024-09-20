import os
import gradio as gr
from .download_from_youtube import download_from_youtube

output_dir = os.path.join(os.getcwd(), "output")
os.makedirs(output_dir, exist_ok=True)

def demo_download_from_youtube():
    with gr.Blocks() as demo:
        gr.Markdown("## YTBDL")
        ytb_url = gr.Textbox(
            label="Youtube URL",
            lines=1,
            value="https://www.youtube.com/watch?v=qASkoV5TsAg",
        )
        proxy_arg = gr.Textbox(
            label="Proxy", lines=1, value="socks5://192.168.43.1:1088"
        )
        ytb_output_dir = gr.Textbox(label="Output Dir", value=output_dir)
        download_btn = gr.Button("Download")
        download_btn.click(
            fn=download_from_youtube,
            inputs=[ytb_url, proxy_arg, ytb_output_dir],
            outputs=[],
        )
    return demo
