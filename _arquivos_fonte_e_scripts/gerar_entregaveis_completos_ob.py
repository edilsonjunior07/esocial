import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = r"C:\Users\Seu Computador\.gemini\antigravity\scratch\saidas\reforma-tributaria\mapa-facil-esocial"
OB1_DIR = os.path.join(BASE_DIR, "order-bumps", "order-bump-01")
OB2_DIR = os.path.join(BASE_DIR, "order-bumps", "order-bump-02")

os.makedirs(OB1_DIR, exist_ok=True)
os.makedirs(OB2_DIR, exist_ok=True)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(40, 805, "KIT DE 25 MODELOS DE DOCUMENTOS TRABALHISTAS • USO PROFISSIONAL")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(40, 798, 555, 798)
        self.line(40, 45, 555, 45)
        self.drawString(40, 32, "Material Oficial de DP • Pronto para Edição e Uso Imediato")
        self.drawRightString(555, 32, f"Página {self._pageNumber} de {page_count}")
        self.restoreState()

# =========================================================================
# 1. GERAÇÃO COMPLETA DO ORDER BUMP 01 (TODOS OS 25 MODELOS TRABALHISTAS)
# =========================================================================
def generate_full_ob1_pdf():
    pdf_path = os.path.join(OB1_DIR, "kit_25_modelos_documentos_trabalhistas.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=40, rightMargin=40, topMargin=55, bottomMargin=55)
    styles = getSampleStyleSheet()

    title_st = ParagraphStyle('CoverT', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor("#0F172A"), alignment=1, spaceAfter=8)
    sub_st = ParagraphStyle('CoverS', parent=styles['Normal'], fontName='Helvetica', fontSize=11, leading=15, textColor=colors.HexColor("#2563EB"), alignment=1, spaceAfter=20)
    h1_st = ParagraphStyle('H1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=colors.HexColor("#0F172A"), spaceBefore=10, spaceAfter=4)
    h2_st = ParagraphStyle('H2', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=colors.HexColor("#2563EB"), spaceBefore=2, spaceAfter=4)
    body_st = ParagraphStyle('B', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13.5, textColor=colors.HexColor("#1E293B"), spaceAfter=5)
    box_st = ParagraphStyle('Bx', parent=styles['Normal'], fontName='Courier', fontSize=8, leading=11.5, textColor=colors.HexColor("#0F172A"))

    story = [
        Spacer(1, 30),
        Paragraph("<font size='10' color='#D97706'><b>ORDER BUMP EXCLUSIVO • FERRAMENTAS PRÁTICAS DE DP</b></font>", sub_st),
        Paragraph("KIT COMPLETO DE 25 MODELOS<br/>DE DOCUMENTOS TRABALHISTAS", title_st),
        Paragraph("Modelos editáveis em Word/PDF de advertências, suspensões, acordos, termos e rescisão com base legal na CLT e no eSocial.", sub_st),
        HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2563EB"), spaceAfter=14),
        Paragraph("<b>INSTRUÇÕES OPERACIONAIS DE USO:</b><br/>1. Selecione o modelo desejado no sumário abaixo e copie o texto para o seu editor (Word ou Docs).<br/>2. Substitua os campos em colchetes <b>[ASSIM]</b> com os dados do empregado e da empresa.<br/>3. Imprima em duas vias de igual teor: uma via para o empregado e outra para ser arquivada na pasta funcional.<br/>4. Em caso de recusa na assinatura pelo trabalhador, colete a assinatura de 2 testemunhas presenciais no rodapé reservado.", body_st),
        Spacer(1, 15)
    ]

    # Lista dos 25 Modelos Completos
    all_25_models = [
        ("01", "ADVERTÊNCIA ESCRITA POR FALTA INJUSTIFICADA", "Art. 482, alínea 'e' da CLT (Desídia)",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], CTPS nº: [NÚMERO], Cargo: [CARGO].\n\n"
         "Vimos por meio desta adverti-lo(a) formalmente pelo não comparecimento ao trabalho no dia [DATA DA FALTA], sem apresentar justificativa legal ou atestado médico no prazo regulamentar da empresa.\n\n"
         "Ressaltamos que a reiteração em faltas injustificadas configura desídia no cumprimento de suas obrigações contratuais, sujeitando-o(a) a penalidades mais severas, inclusive demissão por justa causa (Art. 482 da CLT).\n\n"
         "[CIDADE - UF], [DATA DA APLICAÇÃO].\n\n"
         "__________________________          __________________________\n"
         "Assinatura do Empregador             Assinatura do Empregado\n\n"
         "TESTEMUNHAS (em caso de recusa do empregado):\n"
         "1) Nome: _______________________ CPF: ________________ Ass: _______________\n"
         "2) Nome: _______________________ CPF: ________________ Ass: _______________"),

        ("02", "ADVERTÊNCIA POR ATRASOS REITERADOS", "Art. 482, alínea 'e' da CLT",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], Cargo: [CARGO].\n\n"
         "Serve a presente para aplicar-lhe formalmente ADVERTÊNCIA ESCRITA em razão de sucessivos atrasos injustificados no início de sua jornada de trabalho nos dias [CITAR DIAS E HORÁRIOS], descumprindo o horário contratual pactuado.\n\n"
         "Solicitamos a regularização imediata de sua pontualidade, sob pena de suspensão disciplinar com desconto em folha e repouso remunerado.\n\n"
         "[CIDADE - UF], [DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("03", "ADVERTÊNCIA POR NÃO UTILIZAÇÃO DE EPI", "Art. 158, parágrafo único da CLT e NR-06",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], Função: [FUNÇÃO].\n\n"
         "Fica V. Sa. advertido(a) por ter sido constatado o não uso do seguinte Equipamento de Proteção Individual (EPI): [ESPECIFICAR O EPI, EX: BOTINA COM BIQUEIRA / ÓCULOS], fornecido gratuitamente pela empresa e de uso obrigatório no setor.\n\n"
         "O Art. 158 da CLT estabelece expressamente que constitui ato faltoso a recusa injustificada do empregado ao uso dos equipamentos de proteção fornecidos pelo empregador.\n\n"
         "[CIDADE - UF], [DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("04", "ADVERTÊNCIA POR USO INDEVIDO DE CELULAR EM HORÁRIO DE TRABALHO", "Regulamento Interno e Art. 482, alínea 'h' da CLT",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], Cargo: [CARGO].\n\n"
         "Constatamos o uso reiterado de aparelho celular pessoal e navegação em redes sociais durante o horário efetivo de labor, contrariando o Regulamento Interno da empresa e comprometendo a segurança e o rendimento de suas tarefas.\n\n"
         "Fica V. Sa. advertido(a) a abster-se de tal prática durante o expediente, ressalvados intervalos e emergências.\n\n"
         "[CIDADE - UF], [DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("05", "ADVERTÊNCIA POR INSUBORDINAÇÃO E INDISCIPLINA", "Art. 482, alínea 'h' da CLT",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], Cargo: [CARGO].\n\n"
         "Vimos por meio desta adverti-lo(a) formalmente pelo ato de insubordinação ocorrido no dia [DATA], consubstanciado na recusa injustificada em cumprir a ordem direta de seu superior hierárquico consistente em: [DESCREVER A ORDEM DE SERVIÇO RECUSADA].\n\n"
         "A reincidência configurará falta grave para rescisão imediata por justa causa.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("06", "SUSPENSÃO DISCIPLINAR GRADATIVA (02 DIAS)", "Art. 474 da CLT",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], Cargo: [CARGO].\n\n"
         "Em virtude da reincidência na conduta faltosa de [DESCREVER O MOTIVO], devidamente registrada em advertências anteriores nos dias [DATAS], comunicamos que fica V. Sa. SUSPENSO(A) de suas atividades profissionais por 02 (dois) dias, a contar de [DATA INÍCIO] até [DATA TÉRMINO].\n\n"
         "Durante este período fica vedado seu acesso às dependências da empresa, havendo o desconto salarial e do DSR correspondente.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("07", "SUSPENSÃO DISCIPLINAR GRAVE (05 DIAS)", "Art. 474 da CLT",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], Cargo: [CARGO].\n\n"
         "Diante da gravidade da falta cometida no dia [DATA], consistente em [DESCREVER A INFRAÇÃO GRAVE], aplicamos a penalidade de SUSPENSÃO DISCIPLINAR pelo período de 05 (cinco) dias, de [DATA 1] a [DATA 2].\n\n"
         "Fica advertido(a) de que este é o último grau sancionatório antes da rescisão por justa causa.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("08", "ACORDO INDIVIDUAL DE BANCO DE HORAS", "Art. 59, § 5º da CLT",
         "Empregador: [RAZÃO SOCIAL], CNPJ: [CNPJ].\n"
         "Empregado: [NOME DO EMPREGADO], CPF: [CPF], Cargo: [CARGO].\n\n"
         "Fica pactuado o sistema de compensação de jornada via BANCO DE HORAS INDIVIDUAL:\n"
         "1. O excesso de horas trabalhadas em um dia será compensado pela diminuição em outro, no prazo máximo de 6 (seis) meses;\n"
         "2. O limite diário de trabalho não poderá ultrapassar 10 (dez) horas diárias;\n"
         "3. Na rescisão do contrato sem que tenha havido a compensação integral, o saldo de horas extras será quitado com acréscimo de 50%.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("09", "ACORDO DE PRORROGAÇÃO DE JORNADA", "Art. 59, caput da CLT",
         "Por este instrumento, EMPREGADOR e EMPREGADO ajustam que a jornada normal de trabalho poderá ser prorrogada em até 02 (duas) horas suplementares diárias, conforme necessidade do serviço.\n"
         "As horas extras serão remuneradas com o adicional legal de 50% (ou percentual superior fixado em Convenção Coletiva).\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("10", "TERMO ADITIVO DE TELETRABALHO (HOME OFFICE)", "Art. 75-C da CLT",
         "Fica alterado o regime presencial do(a) empregado(a) para o REGIME DE TELETRABALHO (Home Office):\n"
         "1. As atividades serão prestadas preponderantemente fora das dependências do empregador;\n"
         "2. O empregador fornece em comodato os seguintes equipamentos: [LISTAR COMPUTADOR / MOUSE];\n"
         "3. O empregado declara estar ciente das instruções de ergonomia e saúde e segurança do trabalho.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("11", "TERMO DE OPÇÃO DO VALE-TRANSPORTE", "Lei Federal nº 7.418/85 e Decreto 95.247/87",
         "Eu, [NOME], CPF [CPF], declaro residir no endereço [ENDEREÇO COMPLETO] e solicito o benefício do Vale-Transporte para o deslocamento residência-trabalho e vice-versa:\n"
         "Linhas utilizadas: [LINHA 1 - R$ VALOR] | [LINHA 2 - R$ VALOR].\n"
         "Autorizo expressamente o desconto de até 6% (seis por cento) sobre meu salário básico mensal.\n\n"
         "[LOCAL E DATA] — Assinatura: ___________________________"),

        ("12", "TERMO DE RENÚNCIA AO VALE-TRANSPORTE", "Decreto 95.247/87",
         "Eu, [NOME], CPF [CPF], declaro sob as penas da lei que NÃO utilizo transporte público coletivo para deslocamento residência-trabalho, utilizando [VEÍCULO PRÓPRIO / TRANSPORTE A PÉ], renunciando expressamente ao benefício do Vale-Transporte e desautorizando qualquer desconto salarial a este título.\n\n"
         "[LOCAL E DATA] — Assinatura: ___________________________"),

        ("13", "TERMO DE ENTREGA E RESPONSABILIDADE POR EPI", "NR-06 da Portaria 3.214/78",
         "Recebi da empresa [EMPRESA] os seguintes EPIs novos e em perfeitas condições:\n"
         "Item: [PROTETOR AURICULAR / CA: 12345] | Data Entrega: [DATA]\n"
         "Comprometo-me a usá-los apenas para os fins a que se destinam, responsabilizando-me pela guarda e conservação e comunicando qualquer dano ou perda imediata.\n\n"
         "[LOCAL E DATA] — Assinatura do Trabalhador: ___________________________"),

        ("14", "TERMO DE ENTREGA DE EQUIPAMENTOS CORPORATIVOS", "Art. 462 da CLT",
         "Recebo em comodato o equipamento: [NOTEBOOK MARCA/MODELO, SERIAL: XXXX, CELULAR IMEI: YYYY].\n"
         "O equipamento é de propriedade exclusiva da empresa e destinado estritamente ao serviço.\n"
         "Autorizo o desconto salarial em caso de dolo ou culpa comprovada por negligência ou extravio (Art. 462, § 1º da CLT).\n\n"
         "[LOCAL E DATA] — Assinatura: ___________________________"),

        ("15", "TERMO DE CONFIDENCIALIDADE E LGPD", "Lei nº 13.709/2018 (LGPD)",
         "O(A) empregado(a) compromete-se a manter absoluto sigilo sobre dados pessoais, segredos comerciais, listagens de clientes e informações restritas a que tiver acesso em razão do contrato de trabalho, mesmo após a rescisão contratual, sob pena de responsabilização civil, criminal e demissão por justa causa.\n\n"
         "[LOCAL E DATA] — Assinatura: ___________________________"),

        ("16", "COMUNICAÇÃO DE FÉRIAS INDIVIDUAIS (AVISO PRÉVIO)", "Art. 135 da CLT",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO].\n\n"
         "Comunicamos que, nos termos do Art. 135 da CLT, ser-lhe-ão concedidas férias relativas ao período aquisitivo de [DATA INÍCIO] a [DATA FIM], a serem gozadas no período de [DATA INÍCIO GOZO] a [DATA FIM GOZO] (30 dias).\n\n"
         "Apresente sua Carteira de Trabalho Digital e cartão de ponto para as devidas anotações no eSocial (S-2230).\n\n"
         "[LOCAL E DATA DA COMUNICAÇÃO - COM 30 DIAS DE ANTECEDÊNCIA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Ciente do Empregado"),

        ("17", "REQUERIMENTO DE ABONO PECUNIÁRIO DE FÉRIAS", "Art. 143 da CLT",
         "À Empresa: [RAZÃO SOCIAL].\n\n"
         "Venho requerer a conversão de 1/3 (um terço) do meu período de férias regulamentares em abono pecuniário (10 dias em dinheiro), requerimento este formulado com 15 dias de antecedência do término do período aquisitivo, conforme facultado pelo Art. 143, § 1º da CLT.\n\n"
         "[LOCAL E DATA] — Assinatura do Empregado: ___________________________"),

        ("18", "NOTIFICAÇÃO DE FÉRIAS COLETIVAS", "Art. 139 da CLT",
         "Aos Colaboradores do Setor: [SETOR OU EMPRESA INTEGRAL].\n\n"
         "Comunicamos a concessão de FÉRIAS COLETIVAS de [NÚMERO] dias, com início em [DATA] e retorno em [DATA], tendo sido feita a prévia comunicação ao Ministério do Trabalho e Emprego e ao sindicato representativo da categoria profissional.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________\n"
         "Diretoria / Departamento Pessoal"),

        ("19", "AVISO PRÉVIO DO EMPREGADOR: TRABALHADO", "Art. 487, II e 488 da CLT",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO].\n\n"
         "Vimos pela presente notificar-lhe que a contar do primeiro dia útil seguinte à entrega desta, não mais utilizaremos os seus serviços e solicitamos o cumprimento do AVISO PRÉVIO de [NÚMERO DE DIAS] dias, na forma da Lei 12.506/2011.\n\n"
         "Opção do Empregado (Art. 488 da CLT):\n"
         "(  ) Redução de 2 horas diárias da jornada normal.\n"
         "(  ) Ausência ao trabalho por 7 dias corridos ao final do período.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("20", "AVISO PRÉVIO DO EMPREGADOR: INDENIZADO", "Art. 487, § 1º da CLT e Lei 12.506/11",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO].\n\n"
         "Comunicamos que a partir desta data fica rescindido o seu contrato de trabalho com nossa empresa. O aviso prévio legal no total de [Nº DE DIAS] dias será integralmente INDENIZADO, ficando V. Sa. dispensado(a) do cumprimento da jornada.\n\n"
         "As verbas rescisórias e a documentação do eSocial (S-2299) serão quitadas no prazo improrrogável de até 10 (dez) dias corridos (Art. 477 da CLT).\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("21", "PEDIDO DE DEMISSÃO PELO EMPREGADO", "Art. 487 da CLT",
         "À Empresa: [RAZÃO SOCIAL].\n\n"
         "Por motivos estritamente particulares, venho por meio desta apresentar meu PEDIDO DE DEMISSÃO do cargo de [CARGO] que ocupo nesta empresa.\n\n"
         "(  ) Cumprirei o aviso prévio de 30 dias a partir desta data.\n"
         "(  ) Solicito a dispensa do cumprimento do aviso prévio, autorizando o desconto em rescisão.\n\n"
         "[LOCAL E DATA] — Assinatura do Empregado: ___________________________"),

        ("22", "TÉRMINO NORMAL DE CONTRATO DE EXPERIÊNCIA", "Art. 473 e 474 da CLT",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO].\n\n"
         "Comunicamos que no dia [DATA FINAL] encerra-se o prazo pactuado do seu CONTRATO DE TRABALHO DE EXPERIÊNCIA. Não havendo interesse na continuidade da relação de emprego para contrato por prazo indeterminado, as verbas rescisórias serão quitadas no primeiro dia útil subsequente.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("23", "RESCISÃO ANTECIPADA DE CONTRATO DE EXPERIÊNCIA", "Art. 479 da CLT",
         "Comunicamos a rescisão antecipada do Contrato de Trabalho de Experiência em [DATA], restando [DIAS] dias para o termo final pactuado. A empresa indenizará a metade da remuneração a que teria direito até o término do contrato, na forma do Art. 479 da CLT.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado"),

        ("24", "NOTIFICAÇÃO DE RETORNO (ABANDONO DE EMPREGO)", "Art. 482, 'i' da CLT e Súmula 32 do TST",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], Endereço: [ENDEREÇO RESIDENCIAL].\n\n"
         "Constatamos sua ausência injustificada ao trabalho desde o dia [DATA], totalizando mais de 30 dias consecutivos sem qualquer contato ou justificativa legal.\n\n"
         "Solicitamos seu comparecimento no prazo improrrogável de 48 (quarenta e oito) horas a contar do recebimento desta para reassumir suas funções ou apresentar justificativa plausível, sob pena de caracterização de ABANDONO DE EMPREGO e consequente rescisão por justa causa (Art. 482, 'i' da CLT).\n\n"
         "[LOCAL E DATA DA NOTIFICAÇÃO VIA AR/CARTÓRIO].\n\n"
         "__________________________\n"
         "Diretoria / DP"),

        ("25", "NOTIFICAÇÃO DE DEMISSÃO POR JUSTA CAUSA", "Art. 482 da CLT",
         "À(Ao) Sr.(a): [NOME DO EMPREGADO], CTPS nº: [NÚMERO], Cargo: [CARGO].\n\n"
         "Comunicamos que a partir do recebimento desta seu contrato de trabalho fica rescindido por MOTIVO DE JUSTA CAUSA, com base no Art. 482, alínea [INDICAR A ALÍNEA, EX: 'A' IMPROBIDADE / 'B' INCONTINÊNCIA / 'H' INDISCIPLINA] da Consolidação das Leis do Trabalho (CLT), em razão da falta grave cometida no dia [DATA], consubstanciada em: [RESUMO CIRCUNSTANCIADO DO FATO GRAVE APURADO].\n\n"
         "Solicitamos seu comparecimento no dia [DATA] para quitação das verbas rescisórias devidas por lei e baixa na Carteira de Trabalho.\n\n"
         "[LOCAL E DATA].\n\n"
         "__________________________          __________________________\n"
         "Empregador                          Empregado\n\n"
         "Testemunha 1: ____________________  Testemunha 2: ____________________")
    ]

    for num, tit, base, txt in all_25_models:
        story.append(Paragraph(f"<b>MODELO {num}: {tit}</b>", h1_st))
        story.append(Paragraph(f"<font color='#2563EB'><b>Base Legal:</b> {base}</font>", h2_st))
        t_mod = Table([[Paragraph(txt.replace('\n', '<br/>'), box_st)]], colWidths=[515])
        t_mod.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
            ('PADDING', (0,0), (-1,-1), 7),
        ]))
        story.append(t_mod)
        story.append(Spacer(1, 12))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Sucesso: PDF completo com todos os 25 modelos gerado em: {pdf_path}")

# =========================================================================
# 2. GERAÇÃO COMPLETA DO ORDER BUMP 02 (PLANILHA EXCEL MULTI-ABA COM FÓRMULAS)
# =========================================================================
def generate_full_ob2_excel():
    xlsx_path = os.path.join(OB2_DIR, "planilha_calculo_prazos_esocial.xlsx")
    wb = openpyxl.Workbook()

    # Estilos
    fill_navy = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    fill_blue = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
    fill_green = PatternFill(start_color="059669", end_color="059669", fill_type="solid")
    fill_alert = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
    fill_danger = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
    fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

    font_w_bold = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    font_title = Font(name="Calibri", size=13, bold=True, color="0F172A")
    font_sub = Font(name="Calibri", size=10, italic=True, color="64748B")
    font_b = Font(name="Calibri", size=10, bold=True)
    font_n = Font(name="Calibri", size=10)
    font_danger = Font(name="Calibri", size=10, bold=True, color="991B1B")
    font_ok = Font(name="Calibri", size=10, bold=True, color="065F46")
    border_t = Border(left=Side(style='thin', color='CBD5E1'), right=Side(style='thin', color='CBD5E1'), top=Side(style='thin', color='CBD5E1'), bottom=Side(style='thin', color='CBD5E1'))

    # -------------------------------------------------------------
    # ABA 1: CALCULADORA DE RESCISÃO & AVISO PRÉVIO PROPORCIONAL
    # -------------------------------------------------------------
    ws1 = wb.active
    ws1.title = "Calculo Aviso Previo & Prazos"

    ws1.merge_cells("A1:H1")
    ws1["A1"] = "CALCULADORA DE RESCISÃO & AVISO PRÉVIO PROPORCIONAL (LEI 12.506/2011)"
    ws1["A1"].font = font_title
    ws1["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[1].height = 28

    ws1.merge_cells("A2:H2")
    ws1["A2"] = "Preencha as colunas destacadas (B, C, D, E e F). O Excel calcula automaticamente os dias, prazos e vencimentos."
    ws1["A2"].font = font_sub
    ws1["A2"].alignment = Alignment(horizontal="center", vertical="center")

    h_calc = ["Nº", "Nome do Empregado", "Data Admissão", "Data Demissão", "Salário Base (R$)", "Tipo de Aviso", "Anos Completos", "Dias Lei 12.506", "Total Dias Aviso", "Prazo Pagamento S-2299 (10 dias)", "Valor Estimado Aviso (R$)"]
    
    for col_idx, h_txt in enumerate(h_calc, 1):
        c = ws1.cell(row=4, column=col_idx, value=h_txt)
        c.fill = fill_blue
        c.font = font_w_bold
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = border_t
    ws1.row_dimensions[4].height = 28

    # Linhas de exemplo com fórmulas reais de Excel
    exemplos = [
        (1, "João Silva", "2021-02-10", "2026-03-15", 3500.00, "Indenizado"),
        (2, "Mariana Souza", "2023-08-01", "2026-04-20", 2800.00, "Trabalhado"),
        (3, "Carlos Oliveira", "2019-05-14", "2026-02-28", 5200.00, "Indenizado"),
        (4, "Fernanda Lima", "2025-01-15", "2026-05-10", 2200.00, "Trabalhado"),
        (5, "Roberto Mendes", "2018-11-20", "2026-06-01", 6400.00, "Indenizado")
    ]

    for r_idx, (num, nome, adm, dem, sal, tipo) in enumerate(exemplos, 5):
        ws1.cell(row=r_idx, column=1, value=num).alignment = Alignment(horizontal="center")
        ws1.cell(row=r_idx, column=2, value=nome)
        
        c_adm = ws1.cell(row=r_idx, column=3, value=adm)
        c_adm.alignment = Alignment(horizontal="center")
        c_dem = ws1.cell(row=r_idx, column=4, value=dem)
        c_dem.alignment = Alignment(horizontal="center")
        
        c_sal = ws1.cell(row=r_idx, column=5, value=sal)
        c_sal.number_format = 'R$ #,##0.00'
        
        c_tip = ws1.cell(row=r_idx, column=6, value=tipo)
        c_tip.alignment = Alignment(horizontal="center")

        # Fórmulas Excel:
        # Col 7: Anos Completos = INT((D - C)/365.25)
        ws1.cell(row=r_idx, column=7, value=f"=INT((D{r_idx}-C{r_idx})/365.25)").alignment = Alignment(horizontal="center")
        # Col 8: Dias Adicionais = MIN(60, Anos * 3)
        ws1.cell(row=r_idx, column=8, value=f"=MIN(60, G{r_idx}*3)").alignment = Alignment(horizontal="center")
        # Col 9: Total Dias = 30 + Dias Adicionais
        ws1.cell(row=r_idx, column=9, value=f"=30+H{r_idx}").alignment = Alignment(horizontal="center")
        # Col 10: Prazo S-2299 e Pagamento = Data Demissão + 10 dias corridos
        c_prz = ws1.cell(row=r_idx, column=10, value=f"=D{r_idx}+10")
        c_prz.alignment = Alignment(horizontal="center")
        c_prz.number_format = 'YYYY-MM-DD'
        # Col 11: Valor Estimado Aviso = IF(Tipo="Indenizado", (Salário/30)*TotalDias, 0)
        c_val = ws1.cell(row=r_idx, column=11, value=f'=IF(F{r_idx}="Indenizado", ROUND((E{r_idx}/30)*I{r_idx}, 2), 0)')
        c_val.number_format = 'R$ #,##0.00'

        for c_col in range(1, 12):
            cell_elem = ws1.cell(row=r_idx, column=c_col)
            cell_elem.border = border_t
            cell_elem.font = font_n
            if r_idx % 2 == 0:
                cell_elem.fill = fill_zebra

    # -------------------------------------------------------------
    # ABA 2: SIMULADOR E MONITOR DE PRAZOS DO eSOCIAL
    # -------------------------------------------------------------
    ws2 = wb.create_sheet(title="Monitor Prazos eSocial")

    ws2.merge_cells("A1:G1")
    ws2["A1"] = "MONITOR ELETRÔNICO DE PRAZOS E STATUS DO eSOCIAL"
    ws2["A1"].font = font_title
    ws2["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws2.row_dimensions[1].height = 28

    h_mon = ["Código", "Evento do eSocial", "Fato Gerador / Objeto", "Data Ocorrência", "Regra de Prazo", "Prazo Limite Envio", "Status Operacional"]
    for col_idx, h_txt in enumerate(h_mon, 1):
        c = ws2.cell(row=3, column=col_idx, value=h_txt)
        c.fill = fill_navy
        c.font = font_w_bold
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = border_t
    ws2.row_dimensions[3].height = 24

    eventos_monitor = [
        ("S-2190", "Admissão Preliminar", "Novo funcionário s/ docs finais", "2026-11-03", "Até o final do dia anterior (D-1)", "2026-11-02", "NO PRAZO"),
        ("S-2200", "Admissão Definitiva", "Registro integral com CTPS digital", "2026-11-03", "Até dia 15 do mês seguinte", "2026-12-15", "NO PRAZO"),
        ("S-2210", "CAT - Acidente de Trabalho", "Acidente de trajeto sem óbito", "2026-11-01", "1º dia útil seguinte", "2026-11-03", "ALERTA (HOJE)"),
        ("S-2220", "ASO Periódico / Admissional", "Exame médico ocupacional clínico", "2026-10-25", "Dia 15 do mês subsequente", "2026-11-15", "NO PRAZO"),
        ("S-2230", "Afastamento Temporário", "Atestado médico de 18 dias", "2026-10-18", "Dia 15 do mês subsequente", "2026-11-15", "NO PRAZO"),
        ("S-2240", "Condições Ambientais (LTCAT)", "Exposição a ruído 88 dB", "2026-10-15", "Dia 15 do mês subsequente", "2026-11-15", "NO PRAZO"),
        ("S-2299", "Rescisão / Desligamento", "Término de contrato sem aviso", "2026-10-22", "10 dias corridos da rescisão", "2026-11-01", "ATRASADO"),
        ("S-1200", "Remuneração (Folha Mensal)", "Apuração da competência Outubro/26", "2026-10-31", "Dia 15 do mês subsequente", "2026-11-15", "NO PRAZO"),
        ("S-1210", "Pagamento de Rendimentos", "Crédito em conta 5º dia útil", "2026-11-06", "Dia 15 do mês subsequente", "2026-12-15", "NO PRAZO"),
        ("S-1299", "Fechamento de Periódicos", "Encerramento e envio DCTFWeb", "2026-10-31", "Dia 15 do mês subsequente", "2026-11-15", "NO PRAZO")
    ]

    for r_idx, (cod, ev, fat, dt, rgr, prz, st) in enumerate(eventos_monitor, 4):
        ws2.cell(row=r_idx, column=1, value=cod).alignment = Alignment(horizontal="center")
        ws2.cell(row=r_idx, column=2, value=ev)
        ws2.cell(row=r_idx, column=3, value=fat)
        ws2.cell(row=r_idx, column=4, value=dt).alignment = Alignment(horizontal="center")
        ws2.cell(row=r_idx, column=5, value=rgr)
        ws2.cell(row=r_idx, column=6, value=prz).alignment = Alignment(horizontal="center")
        
        c_st = ws2.cell(row=r_idx, column=7, value=st)
        c_st.alignment = Alignment(horizontal="center")
        if st == "ATRASADO":
            c_st.fill = fill_danger
            c_st.font = font_danger
        elif "ALERTA" in st:
            c_st.fill = fill_alert
            c_st.font = font_b
        else:
            c_st.font = font_ok

        for c_col in range(1, 8):
            ws2.cell(row=r_idx, column=c_col).border = border_t

    # -------------------------------------------------------------
    # ABA 3: TABELA OFICIAL DE MULTAS DA CLT E MTE
    # -------------------------------------------------------------
    ws3 = wb.create_sheet(title="Multas CLT e eSocial")

    ws3.merge_cells("A1:E1")
    ws3["A1"] = "TABELA OFICIAL DE PENALIDADES E MULTAS POR ATRASO NO eSOCIAL"
    ws3["A1"].font = font_title
    ws3["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws3.row_dimensions[1].height = 28

    h_mul = ["Infração Trabalhista / Fiscal", "Evento Relacionado", "Base Legal", "Valor da Multa Legal", "Procedimento de Prevenção"]
    for col_idx, h_txt in enumerate(h_mul, 1):
        c = ws3.cell(row=3, column=col_idx, value=h_txt)
        c.fill = PatternFill(start_color="991B1B", end_color="991B1B", fill_type="solid")
        c.font = font_w_bold
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = border_t
    ws3.row_dimensions[3].height = 24

    multas_dados = [
        ("Não registro de empregado no prazo (admissão retroativa)", "S-2190 / S-2200", "Art. 47 da CLT", "R$ 3.000 por empregado (R$ 800 para ME/EPP)", "Transmitir S-2190 até 23h59 do dia anterior"),
        ("Atraso na quitação das verbas rescisórias", "S-2299", "Art. 477, § 8º da CLT", "Multa equivalente a 1 salário integral do trabalhador", "Pagar e transmitir até o 10º dia corrido"),
        ("Não comunicação de Acidente de Trabalho (CAT)", "S-2210", "Art. 22 da Lei 8.213/91", "De R$ 1.302,00 a R$ 7.507,49 (dobrada na reincidência)", "Transmitir até o 1º dia útil seguinte"),
        ("Omissão de Exames Médicos (ASO)", "S-2220", "NR-28 e Art. 168 CLT", "De R$ 402,53 a R$ 4.025,33 por trabalhador irregular", "Receber laudo da clínica e enviar até dia 15"),
        ("Omissão de Informações Ambientais (LTCAT / Riscos)", "S-2240", "Art. 283 do Decreto 3.048/99", "De R$ 2.926,52 a R$ 292.650,52", "Exigir LTCAT assinado e cadastrar agentes nocivos"),
        ("Falta de envio da folha e fechamento de periódicos", "S-1200 / S-1299", "Lei 8.212/91 e RFB", "Impedimento de CND + Multa de mora e juros Selic", "Enviar folha até o dia 15 e DCTFWeb dia 20")
    ]

    for r_idx, row_d in enumerate(multas_dados, 4):
        for c_idx, val in enumerate(row_d, 1):
            cell = ws3.cell(row=r_idx, column=c_idx, value=val)
            cell.border = border_t
            cell.font = font_n
            if c_idx in [2, 3]:
                cell.alignment = Alignment(horizontal="center")
            if c_idx == 4:
                cell.font = font_danger

    # Ajuste geral de colunas
    for ws_each in [ws1, ws2, ws3]:
        for col in ws_each.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = openpyxl.utils.get_column_letter(col[0].column)
            ws_each.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 40)

    wb.save(xlsx_path)
    print(f"Sucesso: Planilha Excel automatizada gerada em: {xlsx_path}")

if __name__ == "__main__":
    generate_full_ob1_pdf()
    generate_full_ob2_excel()
