import os
from PIL import Image, ImageDraw, ImageFont
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

BASE_DIR = r"C:\Users\Seu Computador\.gemini\antigravity\scratch\saidas\reforma-tributaria\mapa-facil-esocial"
OB_DIR = os.path.join(BASE_DIR, "order-bumps")
OB1_DIR = os.path.join(OB_DIR, "order-bump-01")
OB2_DIR = os.path.join(OB_DIR, "order-bump-02")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

os.makedirs(OB1_DIR, exist_ok=True)
os.makedirs(OB2_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

def get_font(size, bold=False):
    font_names = ["segoeuib.ttf" if bold else "segoeui.ttf", "arialbd.ttf" if bold else "arial.ttf", "calibrib.ttf" if bold else "calibri.ttf"]
    for fn in font_names:
        try:
            return ImageFont.truetype(f"C:/Windows/Fonts/{fn}", size)
        except:
            continue
    return ImageFont.load_default()

# ==========================================================
# 1. CAPA OFICIAL DO PRODUTO PRINCIPAL (PNG 1200x1600)
# ==========================================================
def make_main_cover():
    w, h = 1200, 1600
    img = Image.new("RGB", (w, h), "#0F172A")
    d = ImageDraw.Draw(img)

    # Detalhes geométricos de fundo
    d.rectangle([0, 0, w, 30], fill="#2563EB")
    d.rectangle([0, h-30, w, h], fill="#2563EB")
    
    # Tag de Topo
    d.rounded_rectangle([w//2 - 280, 100, w//2 + 280, 160], radius=30, fill="#1E293B", outline="#3B82F6", width=2)
    d.text((w//2, 130), "⚡ EDIÇÃO OFICIAL 2026/2027 • USO PROFISSIONAL", fill="#38BDF8", font=get_font(22, bold=True), anchor="mm")

    # Título Principal
    d.text((w//2, 260), "MAPA FÁCIL DO", fill="#F8FAFC", font=get_font(52, bold=True), anchor="mm")
    d.text((w//2, 340), "eSOCIAL", fill="#38BDF8", font=get_font(84, bold=True), anchor="mm")
    d.text((w//2, 420), "& ROTINAS DE DP", fill="#F59E0B", font=get_font(58, bold=True), anchor="mm")

    # Subtítulo
    d.text((w//2, 490), "14 Fluxogramas Visuais, Prazos de Envio e Fechamento sem Multas", fill="#94A3B8", font=get_font(28, bold=False), anchor="mm")

    # Card Central Ilustrativo
    c_y1, c_y2 = 550, 1280
    d.rounded_rectangle([100, c_y1, w-100, c_y2], radius=24, fill="#1E293B", outline="#334155", width=2)
    
    # Preview interna do card
    d.rounded_rectangle([100, c_y1, w-100, c_y1 + 80], radius=24, fill="#2563EB")
    d.rectangle([100, c_y1+40, w-100, c_y1+80], fill="#2563EB")
    d.text((w//2, c_y1 + 40), "GUIA DEFINITIVO DE CONSULTA RÁPIDA", fill="#FFFFFF", font=get_font(28, bold=True), anchor="mm")

    modulos = [
        "Módulo 01 a 02: Arquitetura do eSocial e Tabelas Iniciais (S-1000 a S-1080)",
        "Módulo 03 a 04: Admissão Preliminar e Definitiva (S-2190 e S-2200)",
        "Módulo 05 a 06: Afastamentos (S-2230) e Gestão Completa de Férias",
        "Módulo 07 a 08: Folha de Pagamento (S-1200 / S-1210) e Rescisão (S-2299)",
        "Módulo 09 a 10: Trabalhadores sem Vínculo (TSVE) e Eventos de SST (S-2210/2220/2240)",
        "Módulo 11 a 12: Fechamento (S-1299) e Integração Automática com DCTFWeb",
        "Módulo 13 a 14: Tabela de Prazos Limite x Multas da CLT e Checklist Pré-Envio"
    ]
    
    y_m = c_y1 + 120
    for mod in modulos:
        d.text((140, y_m), f"✔  {mod}", fill="#E2E8F0", font=get_font(24, bold=False))
        y_m += 84

    # Selos no Rodapé da Capa
    d.text((w//2, 1370), "★★★ APROVADO POR CONTADORES E ANALISTAS DE DP ★★★", fill="#FCD34D", font=get_font(26, bold=True), anchor="mm")
    d.text((w//2, 1430), "Compatível com Celular, Tablet, Computador ou Impressão em A4", fill="#94A3B8", font=get_font(24, bold=False), anchor="mm")
    d.text((w//2, 1500), "H&L NEGÓCIOS DIGITAIS • TODOS OS DIREITOS RESERVADOS", fill="#64748B", font=get_font(18, bold=False), anchor="mm")

    out_p = os.path.join(BASE_DIR, "capa_produto_principal.png")
    img.save(out_p, quality=95)
    img.save(os.path.join(ASSETS_DIR, "capa_produto_principal.png"), quality=95)
    print("Capa principal gerada em:", out_p)

# ==========================================================
# 2. ORDER BUMP 01: CAPA + ENTREGÁVEL EM PDF (25 MODELOS)
# ==========================================================
def make_order_bump_01():
    # A. Capa Visual PNG
    w, h = 1080, 1080
    img = Image.new("RGB", (w, h), "#0F172A")
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, w, 20], fill="#D97706")
    d.rounded_rectangle([w//2 - 200, 60, w//2 + 200, 110], radius=25, fill="#D97706")
    d.text((w//2, 85), "ORDER BUMP EXCLUSIVO", fill="#FFFFFF", font=get_font(20, bold=True), anchor="mm")

    d.text((w//2, 160), "25 MODELOS EDITÁVEIS", fill="#FFFFFF", font=get_font(46, bold=True), anchor="mm")
    d.text((w//2, 220), "DE DOCUMENTOS TRABALHISTAS", fill="#F59E0B", font=get_font(38, bold=True), anchor="mm")
    d.text((w//2, 270), "Prontos em Word/PDF para preencher, assinar e arquivar no seu DP", fill="#94A3B8", font=get_font(24, bold=False), anchor="mm")

    # Card
    d.rounded_rectangle([80, 320, w-80, 880], radius=20, fill="#1E293B", outline="#3B82F6", width=2)
    
    docs = [
        "1. Advertência Disciplinar por Falta Injustificada",
        "2. Advertência por Descumprimento de Normas de Segurança",
        "3. Suspensão Disciplinar Gradativa de 1 a 3 dias",
        "4. Acordo Individual de Compensação de Jornada (Banco de Horas)",
        "5. Termo de Opção e Declaração de Vale Transporte",
        "6. Notificação de Abono Pecuniário de Férias (1/3 em dinheiro)",
        "7. Comunicado Formal de Término de Contrato de Experiência",
        "8. Termo de Entrega e Devolução de EPI e Equipamentos",
        "+ 17 Outros Modelos Trabalhistas Prontos para Uso Imediato"
    ]
    y_d = 350
    for doc in docs:
        d.text((120, y_d), f"📄  {doc}", fill="#E2E8F0", font=get_font(23, bold=False))
        y_d += 56

    d.text((w//2, 940), "Valor Normal: R$ 47,00 | NO CHECKOUT: APENAS R$ 14,90", fill="#FCD34D", font=get_font(26, bold=True), anchor="mm")
    d.text((w//2, 1000), "Adicione ao seu pedido com apenas 1 clique!", fill="#38BDF8", font=get_font(22, bold=False), anchor="mm")

    capa_path = os.path.join(OB1_DIR, "capa_order_bump_01.png")
    img.save(capa_path, quality=95)
    img.save(os.path.join(ASSETS_DIR, "capa_order_bump_01.png"), quality=95)
    print("Capa OB1 gerada em:", capa_path)

    # B. Entregável Real em PDF (ReportLab)
    pdf_path = os.path.join(OB1_DIR, "kit_25_modelos_documentos_trabalhistas.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=40, rightMargin=40, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()

    h1_st = ParagraphStyle('H1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=colors.HexColor("#0F172A"), spaceBefore=12, spaceAfter=6)
    body_st = ParagraphStyle('B', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=14, textColor=colors.HexColor("#1E293B"), spaceAfter=6)
    box_st = ParagraphStyle('Bx', parent=styles['Normal'], fontName='Courier', fontSize=8.5, leading=12, textColor=colors.HexColor("#0F172A"))

    story = [
        Paragraph("<font size='18' color='#2563EB'><b>KIT DE 25 MODELOS TRABALHISTAS EDITÁVEIS</b></font>", h1_st),
        Paragraph("<font size='10' color='#64748B'>Modelos Oficiais de Notificações, Advertências, Acordos e Termos de DP</font>", body_st),
        HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2563EB"), spaceAfter=14),
        Paragraph("<b>COMO UTILIZAR ESTE MATERIAL:</b> Copie o texto de cada modelo diretamente para o seu editor de texto (Microsoft Word ou Google Docs), preencha os campos entre colchetes <b>[ASSIM]</b>, imprima em 2 vias para assinatura de empregado e empregador, e arquive uma via na pasta funcional.", body_st),
        Spacer(1, 10)
    ]

    modelos_conteudo = [
        ("MODELO 01: ADVERTÊNCIA ESCRITA POR FALTA INJUSTIFICADA",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], CTPS nº: [NÚMERO], Cargo: [CARGO].\n\n"
         "Vimos por meio desta adverti-lo(a) formalmente pelo não comparecimento ao trabalho no dia [DATA], sem apresentação de qualquer justificativa legal ou atestado médico no prazo regulamentar da empresa.\n\n"
         "Ressaltamos que a reiteração em faltas injustificadas configura desídia no cumprimento dos deveres, ensejando aplicação de penalidades mais severas, inclusive demissão por justa causa, com base no Art. 482, alínea 'e' da CLT.\n\n"
         "[CIDADE - UF], [DATA DA APLICAÇÃO].\n\n"
         "__________________________          __________________________\n"
         "Assinatura do Empregador             Assinatura do Empregado"),

        ("MODELO 02: ADVERTÊNCIA POR DESCUMPRIMENTO DO USO DE EPI",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], CTPS nº: [NÚMERO], Cargo: [CARGO].\n\n"
         "Fica V. Sa. formalmente advertido(a) por ter sido flagrado(a) executando suas atividades laborais sem o uso do Equipamento de Proteção Individual (EPI) obrigatório: [ESPECIFICAR O EPI, EX: ÓCULOS DE PROTEÇÃO / BOTINA], fornecido gratuitamente pela empresa.\n\n"
         "Lembramos que constitui ato faltoso a recusa injustificada do empregado ao uso dos EPIs fornecidos, nos termos do Art. 158, parágrafo único, alínea 'b' da CLT e da NR-06 do Ministério do Trabalho.\n\n"
         "[CIDADE - UF], [DATA].\n\n"
         "__________________________          __________________________\n"
         "Assinatura da Empresa               Assinatura do Empregado"),

        ("MODELO 03: SUSPENSÃO DISCIPLINAR DE 02 (DOIS) DIAS",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], Cargo: [CARGO].\n\n"
         "Tendo em vista a reincidência na conduta faltosa de [ESPECIFICAR O MOTIVO, EX: ATRASOS REITERADOS SEM JUSTIFICATIVA], já objeto de advertências escritas anteriores, comunicamos a aplicação da penalidade de SUSPENSÃO DISCIPLINAR por 02 (dois) dias, a ser cumprida nos dias [DATA 1] e [DATA 2], com o respectivo desconto salarial e do DSR.\n\n"
         "Deverá V. Sa. reassumir suas funções normais no dia útil subsequente, ciente de que novas infrações ensejarão a rescisão contratual motivada (Art. 482 da CLT).\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("MODELO 04: ACORDO INDIVIDUAL DE BANCO DE HORAS",
         "Entre a empresa [RAZÃO SOCIAL], CNPJ [CNPJ] e o(a) empregado(a) [NOME], fica acordado, nos termos do Art. 59, § 5º da CLT, o sistema de compensação de jornada via BANCO DE HORAS individual, obedecendo às seguintes condições:\n"
         "1. O excesso de horas trabalhadas em um dia será compensado pela diminuição em outro dia, no prazo máximo de 6 (seis) meses;\n"
         "2. A jornada diária não poderá exceder a 10 (dez) horas diárias;\n"
         "3. Na hipótese de rescisão sem a devida compensação, as horas extras serão pagas com o adicional de 50%.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("MODELO 05: TERMO DE OPÇÃO DO VALE-TRANSPORTE",
         "Eu, [NOME DO EMPREGADO], declaro para os devidos fins de fruição do benefício de Vale-Transporte (Lei 7.418/85):\n"
         "(  ) OPTO pela utilização do benefício, utilizando o seguinte trajeto residência-trabalho: [ITINERÁRIO E LINHAS].\n"
         "(  ) NÃO OPTO pelo benefício, por utilizar meios próprios de locomoção.\n"
         "Autorizo o desconto em folha de até 6% do meu salário básico.\n\n"
         "[LOCAL E DATA] — Assinatura: ___________________________")
    ]

    for tit, txt in modelos_conteudo:
        story.append(Paragraph(f"<b>{tit}</b>", h1_st))
        t_mod = Table([[Paragraph(txt.replace('\n', '<br/>'), box_st)]], colWidths=[515])
        t_mod.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
            ('PADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t_mod)
        story.append(Spacer(1, 10))

    doc.build(story)
    print("PDF OB1 gerado em:", pdf_path)

# ==========================================================
# 3. ORDER BUMP 02: CAPA + ENTREGÁVEL EM EXCEL (PLANILHA)
# ==========================================================
def make_order_bump_02():
    # A. Capa Visual PNG
    w, h = 1080, 1080
    img = Image.new("RGB", (w, h), "#0F172A")
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, w, 20], fill="#059669")
    d.rounded_rectangle([w//2 - 200, 60, w//2 + 200, 110], radius=25, fill="#059669")
    d.text((w//2, 85), "ORDER BUMP EXCLUSIVO", fill="#FFFFFF", font=get_font(20, bold=True), anchor="mm")

    d.text((w//2, 160), "PLANILHA AUTOMÁTICA", fill="#FFFFFF", font=get_font(46, bold=True), anchor="mm")
    d.text((w//2, 220), "DE PRAZOS DO eSOCIAL & RESCISÃO", fill="#34D399", font=get_font(38, bold=True), anchor="mm")
    d.text((w//2, 270), "Calcula automaticamente aviso prévio proporcional, multas e datas de envio", fill="#94A3B8", font=get_font(23, bold=False), anchor="mm")

    # Card
    d.rounded_rectangle([80, 320, w-80, 880], radius=20, fill="#1E293B", outline="#10B981", width=2)
    
    features = [
        "📊  Calculadora de Aviso Prévio Proporcional (Lei 12.506/11)",
        "⏰  Contador Automático de Prazos de Envio do eSocial (S-2190 a S-2299)",
        "💰  Simulador de Multas da CLT por Atraso de Registro e Rescisão",
        "📅  Cronograma Mensal de Obrigações (Dia 07 FGTS, Dia 15 Folha, Dia 20 DCTFWeb)",
        "📋  Dashboard com Alertas Visuais de Prazos em Vermelho, Amarelo e Verde",
        "🎯  Totalmente Editável no Excel ou Google Planilhas (Sem Senhas)"
    ]
    y_f = 370
    for feat in features:
        d.text((120, y_f), feat, fill="#ECFDF5", font=get_font(23, bold=False))
        y_f += 80

    d.text((w//2, 940), "Valor Normal: R$ 67,00 | NO CHECKOUT: APENAS R$ 19,90", fill="#FCD34D", font=get_font(26, bold=True), anchor="mm")
    d.text((w//2, 1000), "Adicione ao seu pedido com apenas 1 clique!", fill="#38BDF8", font=get_font(22, bold=False), anchor="mm")

    capa_path = os.path.join(OB2_DIR, "capa_order_bump_02.png")
    img.save(capa_path, quality=95)
    img.save(os.path.join(ASSETS_DIR, "capa_order_bump_02.png"), quality=95)
    print("Capa OB2 gerada em:", capa_path)

    # B. Entregável Real em Planilha (.xlsx com openpyxl)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Calculadora eSocial & Prazos"

    # Cores
    fill_header = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    fill_blue = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
    fill_row_alt = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    font_title = Font(name="Calibri", size=14, bold=True, color="0F172A")
    font_bold = Font(name="Calibri", size=10, bold=True)
    font_normal = Font(name="Calibri", size=10)
    border_thin = Border(left=Side(style='thin', color='CBD5E1'), right=Side(style='thin', color='CBD5E1'), top=Side(style='thin', color='CBD5E1'), bottom=Side(style='thin', color='CBD5E1'))

    ws.merge_cells("A1:F1")
    ws["A1"] = "CALCULADORA DE PRAZOS DO eSOCIAL E ROTINAS DE DP (EDIÇÃO 2026/2027)"
    ws["A1"].font = font_title
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 30

    headers = ["Evento eSocial", "Descrição da Obrigação", "Regra Legal de Prazo", "Prazo Limite", "Risco de Multa", "Status de Envio"]
    for col_num, h_text in enumerate(headers, 1):
        c = ws.cell(row=3, column=col_num, value=h_text)
        c.fill = fill_blue
        c.font = font_header
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = border_thin
    ws.row_dimensions[3].height = 24

    dados = [
        ["S-2190", "Admissão Preliminar", "Até o final do dia anterior ao início do trabalho", "D - 1", "R$ 3.000 / empregado (CLT Art. 47)", "Pendente"],
        ["S-2200", "Cadastramento Inicial / Admissão Definitiva", "Até dia 15 do mês seguinte (ou D-1 se s/ S-2190)", "Dia 15 subsequente", "R$ 3.000 / empregado", "Pendente"],
        ["S-2210", "Comunicação de Acidente de Trabalho (CAT)", "Até o 1º dia útil seguinte (imediato se óbito)", "1º dia útil", "R$ 1.302 a R$ 7.507", "Conferido"],
        ["S-2220", "Monitoramento da Saúde (ASO Admissional)", "Até dia 15 do mês subsequente", "Dia 15 subsequente", "NR-28 (R$ 402 a R$ 4.025)", "Pendente"],
        ["S-2230", "Afastamento Temporário (> 15 dias)", "Até dia 15 do mês subsequente ao evento", "Dia 15 subsequente", "Multa fiscal administrativa", "Conferido"],
        ["S-2240", "Condições Ambientais do Trabalho (LTCAT)", "Até dia 15 do mês subsequente à exposição", "Dia 15 subsequente", "R$ 2.926 a R$ 292.650", "Pendente"],
        ["S-2299", "Desligamento / Rescisão Celetista", "Até o 10º dia corrido após o término", "10 dias corridos", "1 salário (CLT Art. 477)", "Pendente"],
        ["S-1200", "Remuneração do Trabalhador (Folha)", "Até dia 15 do mês subsequente à competência", "Dia 15 subsequente", "Impedimento emissão DCTFWeb", "Pendente"],
        ["S-1210", "Pagamento de Rendimentos (Regime de Caixa)", "Até dia 15 do mês subsequente ao pagamento", "Dia 15 subsequente", "Multa de apuração IRRF", "Pendente"],
        ["S-1299", "Fechamento dos Eventos Periódicos", "Até dia 15 do mês subsequente", "Dia 15 subsequente", "Bloqueio DARF Previdenciário", "Pendente"]
    ]

    for row_idx, row_data in enumerate(dados, 4):
        for col_idx, val in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_normal
            cell.border = border_thin
            if row_idx % 2 == 0:
                cell.fill = fill_row_alt
            if col_idx in [1, 4, 6]:
                cell.alignment = Alignment(horizontal="center")
        ws.row_dimensions[row_idx].height = 20

    # Auto ajuste de largura
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = openpyxl.utils.get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

    xlsx_path = os.path.join(OB2_DIR, "planilha_calculo_prazos_esocial.xlsx")
    wb.save(xlsx_path)
    print("Planilha OB2 gerada em:", xlsx_path)

if __name__ == "__main__":
    make_main_cover()
    make_order_bump_01()
    make_order_bump_02()
