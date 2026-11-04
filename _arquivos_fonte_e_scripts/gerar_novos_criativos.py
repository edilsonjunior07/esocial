import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

img_mockup_1 = os.path.join(ASSETS_DIR, "mockup-kit-esocial.jpg")
img_mockup_bundle = os.path.join(ASSETS_DIR, "mockup-produto-bundle.jpg")

W, H = 1080, 1350

def get_font(size, bold=False):
    font_names = ["segoeuib.ttf" if bold else "segoeui.ttf", "arialbd.ttf" if bold else "arial.ttf", "calibrib.ttf" if bold else "calibri.ttf"]
    for fn in font_names:
        try:
            return ImageFont.truetype(f"C:/Windows/Fonts/{fn}", size)
        except:
            continue
    return ImageFont.load_default()

f_tag = get_font(23, bold=True)
f_title_big = get_font(42, bold=True)
f_title_sub = get_font(34, bold=True)
f_subhead = get_font(26, bold=False)
f_box_text = get_font(23, bold=False)
f_price_old = get_font(23, bold=False)
f_price_val = get_font(52, bold=True)
f_btn = get_font(31, bold=True)
f_footer = get_font(20, bold=False)

def build_creative(out_filename, tag_text, tag_bg, title_line1, title_line2, title_line2_color, subhead_text, mockup_img_path, check1, check2, btn_text, btn_bg):
    out_path = os.path.join(BASE_DIR, out_filename)
    c = Image.new("RGB", (W, H), "#0B1120")
    d = ImageDraw.Draw(c)

    # 1. Top Bar
    d.rectangle([0, 0, W, 68], fill="#030712")
    d.text((W//2, 34), "⚡ ATUALIZADO 2026/2027 • MANUAL DO ESOCIAL", fill="#F59E0B", font=f_tag, anchor="mm")

    # 2. Tag Badge
    bbox = d.textbbox((W//2, 115), tag_text, font=get_font(21, bold=True), anchor="mm")
    pad_x, pad_y = 20, 8
    d.rounded_rectangle([bbox[0]-pad_x, bbox[1]-pad_y, bbox[2]+pad_x, bbox[3]+pad_y], radius=20, fill=tag_bg)
    d.text((W//2, 115), tag_text, fill="#FFFFFF", font=get_font(21, bold=True), anchor="mm")

    # 3. Headlines
    d.text((W//2, 185), title_line1, fill="#FFFFFF", font=f_title_big, anchor="mm")
    d.text((W//2, 238), title_line2, fill=title_line2_color, font=f_title_sub, anchor="mm")
    d.text((W//2, 288), subhead_text, fill="#94A3B8", font=f_subhead, anchor="mm")

    # 4. Mockup Central Imagem 3D
    if os.path.exists(mockup_img_path):
        raw_mockup = Image.open(mockup_img_path).convert("RGB")
        mw, mh = 960, 560
        raw_mockup.thumbnail((mw, mh), Image.Resampling.LANCZOS)
        
        card_w, card_h = raw_mockup.width + 16, raw_mockup.height + 16
        card_x = (W - card_w) // 2
        card_y = 330
        
        # Borda sutil e fundo
        d.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=22, fill="#1E293B", outline="#2563EB", width=2)
        c.paste(raw_mockup, (card_x + 8, card_y + 8))

    # 5. Box de Benefícios / Checks
    f_y = 925
    d.rounded_rectangle([60, f_y, W-60, f_y + 115], radius=16, fill="#0F172A", outline="#1E293B", width=2)
    d.text((100, f_y + 26), f"✓  {check1}", fill="#E2E8F0", font=f_box_text)
    d.text((100, f_y + 66), f"✓  {check2}", fill="#E2E8F0", font=f_box_text)

    # 6. Oferta e Ancoragem
    d.text((W//2, 1075), "De R$ 97,00 por apenas:", fill="#94A3B8", font=f_price_old, anchor="mm")
    d.text((W//2, 1125), "R$ 27,90", fill="#FFFFFF", font=f_price_val, anchor="mm")
    d.text((W//2, 1162), "Pagamento único • Acesso Imediato no WhatsApp e E-mail", fill="#64748B", font=f_footer, anchor="mm")

    # 7. Botão CTA
    btn_y1 = 1195
    btn_y2 = 1275
    d.rounded_rectangle([80, btn_y1, W-80, btn_y2], radius=18, fill=btn_bg)
    d.text((W//2, (btn_y1+btn_y2)//2), btn_text, fill="#FFFFFF", font=f_btn, anchor="mm")

    # 8. Rodapé de Confiança
    d.text((W//2, 1315), "🔒 Compra 100% Segura • Garantia Total de 30 Dias • Suporte Exclusivo", fill="#64748B", font=f_footer, anchor="mm")

    c.save(out_path, quality=95)
    print(f"Gerado com sucesso: {out_path}")

# ==========================================================
# 4 NOVAS VARIAÇÕES BASEADAS NO ESTILO DO CRIATIVO 01
# ==========================================================

# Variação 01A: Rotina de Fechamento sem Pânico
build_creative(
    out_filename="criativo_01A_fechamento_seguro.png",
    tag_text="DEPARTAMENTO PESSOAL & RH • EDIÇÃO 2026/2027",
    tag_bg="#1D4ED8",
    title_line1="FECHAMENTO DE FOLHA",
    title_line2="SEM PÂNICO NO eSOCIAL",
    title_line2_color="#38BDF8",
    subhead_text="Ordem exata de envio (S-1200 a S-1299) e prazos na sua mesa.",
    mockup_img_path=img_mockup_1,
    check1="Admissão, férias, rescisão e SST sem rejeições no sistema",
    check2="Checklist pré-envio + conferência com DCTFWeb e FGTS Digital",
    btn_text="QUERO MEU GUIA DE FECHAMENTO ➔",
    btn_bg="#059669"
)

# Variação 01B: Quebra de Padrão - Você ainda caça prazos?
build_creative(
    out_filename="criativo_01B_guia_de_mesa.png",
    tag_text="CONSULTA RÁPIDA EM 10 SEGUNDOS NA MESA",
    tag_bg="#D97706",
    title_line1="VOCÊ AINDA ABRE O MOS",
    title_line2="TODA VEZ QUE TEM UMA DÚVIDA?",
    title_line2_color="#FCD34D",
    subhead_text="O material que todo analista de DP deveria ter ao lado do teclado.",
    mockup_img_path=img_mockup_bundle,
    check1="Esqueça manuais de 400 páginas: consulte direto em fluxogramas",
    check2="Prazos exatos de S-2190, S-2200, CAT S-2210 e Rescisão S-2299",
    btn_text="QUERO O MATERIAL DE MESA ➔",
    btn_bg="#2563EB"
)

# Variação 01C: Fartura & Síntese - 14 Fluxogramas
build_creative(
    out_filename="criativo_01C_14_fluxogramas.png",
    tag_text="MATERIAL EXCLUSIVO PARA CONTABILIDADE E DP",
    tag_bg="#047857",
    title_line1="O eSOCIAL DESCOMPLICADO",
    title_line2="EM 14 FLUXOGRAMAS VISUAIS",
    title_line2_color="#4ADE80",
    subhead_text="Linha do tempo do trabalhador: da admissão preliminar ao desligamento.",
    mockup_img_path=img_mockup_bundle,
    check1="14 Módulos Visuais em PDF de Alta Resolução para PC ou Impressão",
    check2="Inclui 5 Bônus: Calendário de Prazos, Checklist, SST e Guia Prático",
    btn_text="GARANTIR MEU ACESSO COM 5 BÔNUS ➔",
    btn_bg="#059669"
)

# Variação 01D: Segurança Total & Carreira
build_creative(
    out_filename="criativo_01D_seguranca_total.png",
    tag_text="CONFORMIDADE FISCAL & TRABALHISTA",
    tag_bg="#4338CA",
    title_line1="TRABALHE NO DEPARTAMENTO PESSOAL",
    title_line2="COM SEGURANÇA TOTAL",
    title_line2_color="#818CF8",
    subhead_text="Elimine o medo de errar códigos e tomar multas da fiscalização.",
    mockup_img_path=img_mockup_1,
    check1="Evite autuações automáticas da Receita Federal e Ministério do Trabalho",
    check2="Tabela comparativa de prazos limite x multas da legislação",
    btn_text="BLINDAR MINHA ROTINA AGORA ➔",
    btn_bg="#2563EB"
)
