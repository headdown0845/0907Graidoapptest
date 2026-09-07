import gradio as gr

def process_text(name: str) -> str:
    if not name.strip():
        return "이름을 입력해주세요."
    return f"안녕하세요, {name}님! CI/CD 파이프라인으로 자동 배포된 모델입니다."

demo = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label="이름 입력", placeholder="홍길동"),
    outputs=gr.Textbox(label="결과"),
    title="Gradio CI/CD 데모",
)

if __name__ == "__main__":
    demo.launch()