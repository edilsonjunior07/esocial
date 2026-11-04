import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

img_mockup_path = os.path.join(ASSETS_DIR, "mockup-kit-esocial.jpg")
img_shield_path = os.path.join(ASSETS_DIR, "anuncio-blindagem-fiscal.jpg")

W, H = 1080, 1350

def get_font(size, bold=False):
    font_names = ["segoeuib.ttf" if bold else "segoeui.ttf", "arialbd.ttf" if bold else "arial.ttf", "calibrib.ttf" if bold else "calibri.ttf"]
    for fn in font_names:
        try:
            return ImageFont.truetype(f"C:/Windows/Fonts/{fn}", size)
        except:
            continue
    return ImageFont.load_default()

f_tag = get_font(24, bold=True)
f_title = get_font(44, bold=True)
f_sub = get_font(28, bold=False)
f_box = get_font(22, bold=True)
f_price_big = get_font(52, bold=True)
f_price_sub = get_font(22, bold=False)
f_btn = get_font(32, bold=True)
f_footer = get_font(20, bold=False)

# ==============================================================
# CRIATIVO 01: MOCKUP REAL 3D DO PRODUTO (FOCO EM PRATICIDADE)
# ==============================================================
def make_creative_01():
    out_path = os.path.join(BASE_DIR, "criativo_01_mockup_completo.png")
    c = Image.new("RGB", (W, H), "#0B1120")
    d = ImageDraw.Draw(c)

    # Topo
    d.rectangle([0, 0, W, 70], fill="#030712")
    d.text((W//2, 35), "⚡ ATUALIZADO 2026/2027 • MANUAL DO ESOCIAL", fill="#F59E0B", font=f_tag, anchor="mm")

    # Tag Badge
    d.rounded_rectangle([W//2 - 250, 95, W//2 + 250, 145], radius=25, fill="#1D4ED8")
    d.text((W//2, 120), "GUIA VISUAL DE DEPARTAMENTO PESSOAL", fill="#FFFFFF", font=get_font(22, bold=True), anchor="mm")

    # Headline
    d.text((W//2, 190), "DOMINE O ESOCIAL NA PRÁTICA", fill="#FFFFFF", font=f_title, anchor="mm")
    d.text((W//2, 245), "SEM DECORAR 400 PÁGINAS DE MANUAL", fill="#38BDF8", font=get_font(36, bold=True), anchor="mm")

    # Imagem Real do Mockup Central
    if os.path.exists(img_mockup_path):
        raw_mockup = Image.open(img_mockup_path).convert("RGB")
        # Resize mantendo proporção para caber em 960 x 580
        mw, mh = 960, 580
        raw_mockup.thumbnail((mw, mh), Image.Resampling.LANCZOS)
        
        # Cria card com borda sutil
        card_w, card_h = raw_mockup.width + 16, raw_mockup.height + 16
        card_x = (W - card_w) // 2
        card_y = 295
        d.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=20, fill="#1E293B", outline="#3B82F6", width=2)
        c.paste(raw_mockup, (card_x + 8, card_y + 8))

    # Features Pill Box
    f_y = 920
    d.rounded_rectangle([60, f_y, W-60, f_y + 115], radius=16, fill="#0F172A", outline="#1E293B", width=2)
    d.text((100, f_y + 26), "✓  14 Fluxogramas: Admissão, Folha, Férias, Rescisão e SST", fill="#E2E8F0", font=f_box)
    d.text((100, f_y + 66), "✓  Tabela de Prazos Críticos x Multas da Legislação em PDF", fill="#E2E8F0", font=f_box)

    # Preço e Oferta
    d.text((W//2, 1075), "De R$ 97,00 por apenas:", fill="#94A3B8", font=get_font(24, bold=False), anchor="mm")
    d.text((W//2, 1125), "R$ 27,90", fill="#FFFFFF", font=f_price_big, anchor="mm")
    d.text((W//2, 1162), "Pagamento único • Acesso Imediato", fill="#64748B", font=f_price_sub, anchor="mm")

    # Botão CTA
    btn_y1 = 1195
    btn_y2 = 1275
    d.rounded_rectangle([80, btn_y1, W-80, btn_y2], radius=18, fill="#059669")
    d.text((W//2, (btn_y1+btn_y2)//2), "QUERO MEU ACESSO AGORA ➔", fill="#FFFFFF", font=f_btn, anchor="mm")

    # Footer
    d.text((W//2, 1315), "🔒 Compra Segura • Envio no WhatsApp e E-mail • Garantia de 30 Dias", fill="#64748B", font=f_footer, anchor="mm")

    c.save(out_path, quality=95)
    print(f"Criativo 01 gerado em: {out_path}")

# ==============================================================
# CRIATIVO 02: BLINDAGEM FISCAL CONTRA MULTAS (FOCO EM MEDO/DOR)
# ==============================================================
def make_creative_02():
    out_path = os.path.join(BASE_DIR, "criativo_02_blindagem_fiscal.png")
    c = Image.new("RGB", (W, H), "#090D16")
    d = ImageDraw.Draw(c)

    # Topo Alerta
    d.rectangle([0, 0, W, 70], fill="#450A0A")
    d.text((W//2, 35), "⚠️ ATENÇÃO: MULTAS AUTOMÁTICAS DA FISCALIZAÇÃO", fill="#FCA5A5", font=f_tag, anchor="mm")

    # Tag Badge
    d.rounded_rectangle([W//2 - 240, 95, W//2 + 240, 145], radius=25, fill="#991B1B")
    d.text((W//2, 120), "BLINDAGEM DE DEPARTAMENTO PESSOAL", fill="#FFFFFF", font=get_font(20, bold=True), anchor="mm")

    # Headline
    d.text((W//2, 190), "A FISCALIZAÇÃO ELETRÔNICA", fill="#FFFFFF", font=f_title, anchor="mm")
    d.text((W//2, 245), "NÃO AVISA ANTES DE MULTAR", fill="#EF4444", font=get_font(38, bold=True), anchor="mm")

    # Imagem Central: Escudo e Calendário Holográfico 3D
    if os.path.exists(img_shield_path):
        raw_shield = Image.open(img_shield_path).convert("RGB")
        mw, mh = 960, 580
        raw_shield.thumbnail((mw, mh), Image.Resampling.LANCZOS)
        
        card_w, card_h = raw_shield.width + 16, raw_shield.height + 16
        card_x = (W - card_w) // 2
        card_y = 295
        d.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=20, fill="#1E293B", outline="#DC2626", width=2)
        c.paste(raw_shield, (card_x + 8, card_y + 8))

    # Alerta de Multas
    f_y = 920
    d.rounded_rectangle([60, f_y, W-60, f_y + 115], radius=16, fill="#18181B", outline="#27272A", width=2)
    d.text((100, f_y + 26), "🚨 Admissão enviada atrasada: Multa de R$ 3.000 por empregado", fill="#FCA5A5", font=f_box)
    d.text((100, f_y + 66), "🛡️ Tenha a Tabela de Prazos e Evite Qualquer Autuação no DP", fill="#86EFAC", font=f_box)

    # Preço e Oferta
    d.text((W//2, 1075), "Acesso completo por apenas:", fill="#94A3B8", font=get_font(24, bold=False), anchor="mm")
    d.text((W//2, 1125), "R$ 27,90", fill="#FFFFFF", font=f_price_big, anchor="mm")
    d.text((W//2, 1162), "Inclui 5 Bônus Exclusivos • Garantia de 30 Dias", fill="#64748B", font=f_price_sub, anchor="mm")

    # Botão CTA
    btn_y1 = 1195
    btn_y2 = 1275
    d.rounded_rectangle([80, btn_y1, W-80, btn_y2], radius=18, fill="#DC2626")
    d.text((W//2, (btn_y1+btn_y2)//2), "BLINDAR MEU DP AGORA ➔", fill="#FFFFFF", font=f_btn, anchor="mm")

    # Footer
    d.text((W//2, 1315), "Envio Imediato via WhatsApp e E-mail • Pagamento Único", fill="#64748B", font=f_footer, anchor="mm")

    c.save(out_path, quality=95)
    print(f"Criativo 02 gerado em: {out_path}")

# ==============================================================
# CRIATIVO 03: COMPARATIVO ANTES x DEPOIS (CONTRASTE DIRETO)
# ==============================================================
def make_creative_03():
    out_path = os.path.join(BASE_DIR, "criativo_03_contraste_visual.png")
    c = Image.new("RGB", (W, H), "#0F172A")
    d = ImageDraw.Draw(c)

    # Topo
    d.rectangle([0, 0, W, 70], fill="#1E293B")
    d.text((W//2, 35), "COMO VOCÊ PREFERE TRABALHAR NO DP?", fill="#38BDF8", font=f_tag, anchor="mm")

    # Headline
    d.text((W//2, 130), "CHEGA DE FOLHEAR 400 PÁGINAS", fill="#FFFFFF", font=get_font(38, bold=True), anchor="mm")
    d.text((W//2, 180), "TODA VEZ QUE TIVER UMA DÚVIDA", fill="#94A3B8", font=get_font(30, bold=False), anchor="mm")

    # Comparativo: 2 Colunas lado a lado
    # Coluna 1: O Jeito Antigo (Vermelho/Cinza)
    box1_x1, box1_x2 = 60, 520
    box_y1, box_y2 = 230, 830
    d.rounded_rectangle([box1_x1, box_y1, box1_x2, box_y2], radius=18, fill="#1E1B2E", outline="#EF4444", width=2)
    d.rounded_rectangle([box1_x1, box_y1, box1_x2, box_y1 + 55], radius=18, fill="#7F1D1D")
    d.rectangle([box1_x1, box_y1 + 30, box1_x2, box_y1 + 55], fill="#7F1D1D")
    d.text(((box1_x1+box1_x2)//2, box_y1 + 28), "❌ JEITO TRADICIONAL", fill="#FFFFFF", font=get_font(20, bold=True), anchor="mm")

    items_bad = [
        "• Manual do MOS com 420 páginas",
        "• Dúvidas caçadas em fóruns",
        "• Insegurança com prazos de admissão",
        "• Pânico em eventos de SST",
        "• Risco diário de multas da RFB",
        "• Retrabalho no fechamento de folha"
    ]
    y_i = box_y1 + 80
    for it in items_bad:
        d.text((box1_x1 + 20, y_i), it, fill="#CBD5E1", font=get_font(19, bold=False))
        y_i += 54

    # Coluna 2: O Jeito com o Mapa Fácil (Verde/Azul)
    box2_x1, box2_x2 = 560, 1020
    d.rounded_rectangle([box2_x1, box_y1, box2_x2, box_y2], radius=18, fill="#064E3B", outline="#10B981", width=2)
    d.rounded_rectangle([box2_x1, box_y1, box2_x2, box_y1 + 55], radius=18, fill="#047857")
    d.rectangle([box2_x1, box_y1 + 30, box2_x2, box_y1 + 55], fill="#047857")
    d.text(((box2_x1+box2_x2)//2, box_y1 + 28), "✅ COM O MAPA FÁCIL", fill="#FFFFFF", font=get_font(20, bold=True), anchor="mm")

    items_good = [
        "✓ 14 Fluxogramas visuais diretos",
        "✓ Consulta em 10 segundos na mesa",
        "✓ Prazos exatos de S-2190 e S-2200",
        "✓ Fluxo claro de CAT e ASOs",
        "✓ Zero multas da fiscalização",
        "✓ Fechamento seguro da folha"
    ]
    y_i = box_y1 + 80
    for it in items_good:
        d.text((box2_x1 + 20, y_i), it, fill="#ECFDF5", font=get_font(19, bold=True))
        y_i += 54

    # Box com preview miniatura do kit
    if os.path.exists(img_mockup_path):
        raw_thumb = Image.open(img_mockup_path).convert("RGB")
        raw_thumb.thumbnail((400, 200), Image.Resampling.LANCZOS)
        c.paste(raw_thumb, ((W - raw_thumb.width)//2, 600))

    # Banner de Destaque
    d.rounded_rectangle([60, 860, W-60, 970], radius=16, fill="#1E293B", outline="#3B82F6", width=2)
    d.text((W//2, 900), "🎁 LEVE O MAPA FÁCIL + 5 BÔNUS EXCLUSIVOS", fill="#FBBF24", font=get_font(24, bold=True), anchor="mm")
    d.text((W//2, 938), "Checklist de Folha • SST Descomplicado • Calendário de Prazos", fill="#E2E8F0", font=get_font(20, bold=False), anchor="mm")

    # Preço e Oferta
    d.text((W//2, 1020), "Apenas pagamento único:", fill="#94A3B8", font=get_font(22, bold=False), anchor="mm")
    d.text((W//2, 1075), "R$ 27,90", fill="#FFFFFF", font=f_price_big, anchor="mm")
    d.text((W//2, 1115), "Sem mensalidades • Acesso Vitalício", fill="#64748B", font=f_price_sub, anchor="mm")

    # Botão CTA
    btn_y1 = 1150
    btn_y2 = 1235
    d.rounded_rectangle([80, btn_y1, W-80, btn_y2], radius=18, fill="#059669")
    d.text((W//2, (btn_y1+btn_y2)//2), "QUERO FACILITAR MINHA ROTINA ➔", fill="#FFFFFF", font=f_btn, anchor="mm")

    # Footer
    d.text((W//2, 1290), "Garantia Total de 30 Dias • Receba agora no seu WhatsApp", fill="#64748B", font=f_footer, anchor="mm")

    c.save(out_path, quality=95)
    print(f"Criativo 03 gerado em: {out_path}")

if __name__ == "__main__":
    make_creative_01()
    make_creative_02()
    make_creative_03()
