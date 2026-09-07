from app import process_text

def test_process_text_with_name():
    result = process_text("홍길동")
    assert "안녕하세요, 홍길동님!" in result

def test_process_text_empty():
    result = process_text("   ")
    assert result == "이름을 입력해주세요."