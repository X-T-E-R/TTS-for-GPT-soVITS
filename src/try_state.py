import gradio as gr

def test_state(text):
    # 这里直接返回需要保存的数据结构
    return {"text": text.split("。")}

def show_state(state):
    # 直接从state参数中提取数据进行操作
    state_list = "|||".join(state["text"])
    return gr.Textbox(state_list, label="分割后的文本")

with gr.Blocks() as block:
    state = gr.State({})  # 初始化state
    with gr.Row():
        text_box_1 = gr.Textbox("你好啊。我是傻逼。", label="输入文本")
        button_1 = gr.Button("测试state", variant="primary", scale=1)
        # 注意这里将state作为输出
        button_1.click(test_state, inputs=[text_box_1], outputs=[state])
        button_2 = gr.Button("展示state", variant="primary", scale=1)
        text_box_2 = gr.Textbox("", label="分割后的文本")
        # 注意这里将state作为输入
        button_2.click(show_state, inputs=[state], outputs=[text_box_2])

block.launch(server_port=9111, show_error=True)
