import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_IMG = os.path.join(BASE_DIR, "criativo_feed_1080x1350.png")

# Dimensões do Feed 4:5
W, H = 1080, 1350
img = Image.new("RGB", (W, H), "#0F172A")
draw = ImageDraw.Draw(img)

# Tenta carregar fontes do Windows
def get_font(size, bold=False):
    font_names = ["segoeuib.ttf" if bold else "segoeui.ttf", "arialbd.ttf" if bold else "arial.ttf", "calibrib.ttf" if bold else "calibri.ttf"]
    for fn in font_names:
        try:
            return ImageFont.truetype(f"C:/Windows/Fonts/{fn}", size)
        except:
            continue
    return ImageFont.load_default()

f_tag = get_font(26, bold=True)
f_title = get_font(52, bold=True)
f_sub = get_font(32, bold=False)
f_box_title = get_font(30, bold=True)
f_box_text = get_font(25, bold=False)
f_price_old = get_font(28, bold=False)
f_price_big = get_font(60, bold=True)
f_btn = get_font(36, bold=True)
f_footer = get_font(22, bold=False)

# 1. Background com gradiente suave ou barra superior
draw.rectangle([0, 0, W, 80], fill="#1E293B")
draw.text((W//2, 40), "⚡ ATUALIZADO 2026/2027 • MANUAL DO ESOCIAL", fill="#F59E0B", font=f_tag, anchor="mm")

# 2. Tag da Categoria
tag_text = "MAPA FÁCIL DO DEPARTAMENTO PESSOAL"
bbox = draw.textbbox((W//2, 125), tag_text, font=f_tag, anchor="mm")
pad = 14
draw.rounded_rectangle([bbox[0]-pad, bbox[1]-pad+4, bbox[2]+pad, bbox[3]+pad-4], radius=20, fill="#2563EB")
draw.text((W//2, 125), tag_text, fill="#FFFFFF", font=f_tag, anchor="mm")

# 3. Título Principal
draw.text((W//2, 200), "DOMINE O ESOCIAL", fill="#FFFFFF", font=f_title, anchor="mm")
draw.text((W//2, 260), "SEM MEDO DE MULTAS", fill="#38BDF8", font=f_title, anchor="mm")

# Subheadline
sub_text = "Todos os eventos S-xxxx e rotinas de DP em fluxogramas visuais."
draw.text((W//2, 320), sub_text, fill="#94A3B8", font=f_sub, anchor="mm")

# 4. Box Central de Conteúdo (Simulação de Mockup e Tabela)
box_y1 = 370
box_y2 = 820
draw.rounded_rectangle([60, box_y1, W-60, box_y2], radius=24, fill="#1E293B", outline="#334155", width=2)

# Cabeçalho da Caixa
draw.rounded_rectangle([60, box_y1, W-60, box_y1+75], radius=24, fill="#2563EB")
draw.rectangle([60, box_y1+40, W-60, box_y1+75], fill="#2563EB") # achata a parte de baixo
draw.text((W//2, box_y1+38), "14 FLUXOGRAMAS PRONTOS PARA CONSULTA", fill="#FFFFFF", font=f_box_title, anchor="mm")

# Itens da Caixa
items = [
    "✓  Prazos de Admissão: Preliminar (S-2190) x Definitiva (S-2200)",
    "✓  Eventos de SST Descomplicados: S-2210, S-2220 e S-2240",
    "✓  Folha de Pagamento: Remuneração (S-1200) e Pagamentos (S-1210)",
    "✓  Regras e Prazos Limite de Rescisão e Desligamento (S-2299)",
    "✓  Calendário Visual com Datas Críticas de Fechamento",
    "✓  Tabela Comparativa de Multas e Prazos da Fiscalização"
]

y_offset = box_y1 + 105
for item in items:
    draw.text((100, y_offset), item, fill="#E2E8F0", font=f_box_text)
    y_offset += 58

# 5. Box dos Bônus Grátis
b_box_y1 = 845
b_box_y2 = 985
draw.rounded_rectangle([60, b_box_y1, W-60, b_box_y2], radius=18, fill="#042F2E", outline="#059669", width=2)
draw.text((W//2, b_box_y1+35), "🎁 INCLUI 5 BÔNUS EXCLUSIVOS DE DP E SST", fill="#34D399", font=f_box_title, anchor="mm")
draw.text((W//2, b_box_y1+75), "Checklist de Folha • Guia Antes x Depois • 50 Respostas para Erros", fill="#E2E8F0", font=f_box_text, anchor="mm")
draw.text((W//2, b_box_y1+110), "Avaliado em R$ 135,00 — GRÁTIS HOJE", fill="#FCD34D", font=f_tag, anchor="mm")

# 6. Oferta e Botão de Ação (CTA)
draw.text((W//2, 1025), "De R$ 97,00 por apenas:", fill="#94A3B8", font=f_price_old, anchor="mm")
draw.text((W//2, 1085), "R$ 27,90", fill="#FFFFFF", font=f_price_big, anchor="mm")
draw.text((W//2, 1130), "Pagamento único • Sem mensalidades", fill="#64748B", font=f_footer, anchor="mm")

# Botão Verde
btn_y1 = 1160
btn_y2 = 1245
draw.rounded_rectangle([80, btn_y1, W-80, btn_y2], radius=20, fill="#059669")
draw.text((W//2, (btn_y1+btn_y2)//2), "QUERO MEU ACESSO AGORA ➔", fill="#FFFFFF", font=f_btn, anchor="mm")

# 7. Rodapé de Confiança
draw.text((W//2, 1290), "🔒 Compra 100% Segura • Acesso Imediato no WhatsApp e E-mail • Garantia de 30 Dias", fill="#94A3B8", font=f_footer, anchor="mm")

img.save(OUTPUT_IMG, quality=95)
print(f"Criativo em imagem 1080x1350 gerado com sucesso em: {OUTPUT_IMG}")
