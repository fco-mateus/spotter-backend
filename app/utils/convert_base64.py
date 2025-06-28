import base64

def converter_imagem_para_base64_formatado(file_content, mime_type):
    imagem_base64 = base64.b64encode(file_content).decode('utf-8')
    # Monta a string no formato esperado
    return f"data:{mime_type};base64,{imagem_base64}"