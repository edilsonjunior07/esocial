import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUTO_DIR = os.path.join(BASE_DIR, "produto")
BONUS_DIR = os.path.join(BASE_DIR, "bonus")

os.makedirs(PRODUTO_DIR, exist_ok=True)
os.makedirs(BONUS_DIR, exist_ok=True)

# Cores da Marca
NAVY = colors.HexColor("#0F172A")
NAVY_LIGHT = colors.HexColor("#1E293B")
BLUE = colors.HexColor("#2563EB")
BLUE_SOFT = colors.HexColor("#EFF6FF")
AMBER = colors.HexColor("#D97706")
AMBER_BG = colors.HexColor("#FEF3C7")
EMERALD = colors.HexColor("#059669")
EMERALD_BG = colors.HexColor("#ECFDF5")
GRAY_BG = colors.HexColor("#F8FAFC")
BORDER_COLOR = colors.HexColor("#CBD5E1")
TEXT_MUTED = colors.HexColor("#64748B")

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
            return  # Capa limpa
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(TEXT_MUTED)
        
        # Header
        self.drawString(40, 805, "MAPA FÁCIL DO ESOCIAL E ROTINAS DE DP • GUIA DE CONSULTA RÁPIDA")
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.5)
        self.line(40, 798, 555, 798)
        
        # Footer
        self.line(40, 45, 555, 45)
        self.drawString(40, 32, "Material Exclusivo de Consulta Profissional • Atualizado 2026/2027")
        self.drawRightString(555, 32, f"Página {self._pageNumber} de {page_count}")
        self.restoreState()

def create_main_product():
    pdf_path = os.path.join(PRODUTO_DIR, "mapa_facil_esocial_produto_principal.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=55,
        bottomMargin=55
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=NAVY,
        alignment=1, # Centralizado
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=BLUE,
        alignment=1,
        spaceAfter=25
    )
    
    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=NAVY,
        spaceBefore=14,
        spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'Header2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=BLUE,
        spaceBefore=8,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=NAVY_LIGHT,
        spaceAfter=6
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=NAVY_LIGHT
    )
    
    story = []
    
    # ==================== CAPA ====================
    story.append(Spacer(1, 100))
    story.append(Paragraph("<font size='10' color='#2563EB'><b>GUIA PRÁTICO EM FLUXOGRAMAS</b></font>", subtitle_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("MAPA FÁCIL DO eSOCIAL<br/>E ROTINAS DE DP", title_style))
    story.append(Paragraph("Domine todos os eventos S-xxxx, prazos legais e fechamento de folha de forma simples, visual e sem multas.", subtitle_style))
    story.append(Spacer(1, 30))
    
    # Caixa de Destaque na Capa
    capa_box_data = [
        [Paragraph("<b>CONTEÚDO DESTE MATERIAL:</b><br/>• 14 Módulos Visuais com a linha do tempo do eSocial<br/>• Tabela de Prazos Limite x Multas da Legislação<br/>• Rotinas de Admissão, Folha, Férias, Rescisão e SST<br/>• Checklist Pré-Envio de Conferência", callout_style)]
    ]
    t_capa = Table(capa_box_data, colWidths=[450])
    t_capa.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BLUE_SOFT),
        ('BOX', (0,0), (-1,-1), 1, BLUE),
        ('PADDING', (0,0), (-1,-1), 14),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ]))
    story.append(t_capa)
    story.append(Spacer(1, 150))
    story.append(Paragraph("<font size='9' color='#64748B'>Edição 2026/2027 • Versão S-1.2 do MOS • Uso Profissional</font>", subtitle_style))
    story.append(PageBreak())
    
    # ==================== SUMÁRIO & COMO USAR ====================
    story.append(Paragraph("COMO UTILIZAR ESTE MAPA VISUAL", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=12))
    story.append(Paragraph(
        "Este guia foi desenhado especificamente para consulta rápida na mesa de trabalho do profissional de Departamento Pessoal e Contabilidade. Em vez de ler manuais extensos, utilize as tabelas e fluxogramas sintetizados.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Regra de Ouro do eSocial:</b> A transmissão tempestiva dos eventos preliminares e periódicos evita o cruzamento fiscal eletrônico da Receita Federal e do Ministério do Trabalho. Mantenha os prazos marcados na sua rotina diária.",
        body_style
    ))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("SUMÁRIO DOS 14 MÓDULOS:", h2_style))
    
    modulos_list = [
        ("Módulo 01", "Visão Geral da Arquitetura do eSocial (Tabelas, Não Periódicos e Periódicos)"),
        ("Módulo 02", "Eventos de Tabela e Empregador (S-1000 a S-1080)"),
        ("Módulo 03", "Rotina de Admissão: Preliminar (S-2190) x Definitiva (S-2200)"),
        ("Módulo 04", "Alterações Cadastrais e Contratuais (S-2205 e S-2206)"),
        ("Módulo 05", "Afastamentos Temporários e Atestados Médicos (S-2230)"),
        ("Módulo 06", "Gestão de Férias: Prazos de Aviso, Gozo e Transmissão"),
        ("Módulo 07", "Folha de Pagamento: Remuneração (S-1200) e Pagamentos (S-1210)"),
        ("Módulo 08", "Desligamento e Rescisão Contratual (S-2299 e S-2399)"),
        ("Módulo 09", "Trabalhadores Sem Vínculo de Emprego - TSVE (S-2300 e S-2306)"),
        ("Módulo 10", "Saúde e Segurança do Trabalho - SST (S-2210, S-2220 e S-2240)"),
        ("Módulo 11", "Fechamento e Reabertura da Folha (S-1298 e S-1299)"),
        ("Módulo 12", "Integração eSocial com DCTFWeb e Geração de Guias (DARF)"),
        ("Módulo 13", "Tabela Comparativa de Prazos Críticos x Multas CLT/RFB"),
        ("Módulo 14", "Checklist Operacional Pré-Transmissão de DP")
    ]
    
    sumario_data = [[Paragraph(f"<b>{m[0]}</b>", body_style), Paragraph(m[1], body_style)] for m in modulos_list]
    t_sumario = Table(sumario_data, colWidths=[80, 435])
    t_sumario.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GRAY_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sumario)
    story.append(PageBreak())
    
    # ==================== DETALHAMENTO DOS MÓDULOS ====================
    conteudos_modulos = [
        ("MÓDULO 01: ARQUITETURA E FLUXO DO eSOCIAL", [
            ("Conceito Central", "O eSocial não calcula tributos por si só: ele é um repositório centralizado que recebe eventos em XML assinados digitalmente e alimenta a DCTFWeb e o FGTS Digital."),
            ("Divisão em 3 Grupos", "1. Eventos Iniciais e Tabelas (S-1000 a S-1080) | 2. Eventos Não Periódicos (admissões, alterações, afastamentos, rescisões e SST) | 3. Eventos Periódicos (folha de pagamento S-1200 a S-1299)."),
            ("Ordem Obrigatória", "Nunca envie um evento de remuneração (S-1200) sem que o trabalhador (S-2200) e a lotação tributária (S-1020) já tenham sido validados com recibo de entrega.")
        ]),
        ("MÓDULO 02: EVENTOS DE TABELA (S-1000 A S-1080)", [
            ("S-1000 (Empregador)", "Informações da empresa, enquadramento tributário, classificação fiscal e indicativo de desoneração da folha. Enviado no início ou quando houver alteração cadastral."),
            ("S-1005 (Estabelecimentos)", "Cadastramento de matriz e filiais, alíquota RAT, FAP e CNAE preponderante."),
            ("S-1010 (Rubricas)", "Tabela mestre de vencimentos e descontos. Ponto crítico: a correta incidência de INSS, FGTS e IRRF em cada rubrica evita geração incorreta de guias na DCTFWeb.")
        ]),
        ("MÓDULO 03: ROTINA DE ADMISSÃO (S-2190 vs. S-2200)", [
            ("S-2190 (Admissão Preliminar)", "Usado quando faltam documentos finais do empregado. DEVE ser transmitido até o final do dia imediatamente anterior ao início da prestação de serviços."),
            ("S-2200 (Cadastramento Inicial e Admissão)", "Registro completo com todos os dados contratuais e pessoais. Se usado o S-2190, o S-2200 deve ser transmitido até o dia 15 do mês subsequente (ou antes de qualquer outro evento do trabalhador)."),
            ("Atenção Crítica", "Transmitir admissão com data retroativa gera notificação e multa imediata por infração ao Art. 47 da CLT (R$ 3.000 por empregado não registrado).")
        ]),
        ("MÓDULO 04: ALTERAÇÕES CONTRATUAIS E CADASTRAIS (S-2205 E S-2206)", [
            ("S-2205 (Alteração Cadastral)", "Mudança de endereço, estado civil, escolaridade, etc. Prazo: até o dia 15 do mês subsequente ao da ocorrência."),
            ("S-2206 (Alteração Contratual)", "Aumento salarial, mudança de cargo, horário ou transferência. Prazo: até o dia 15 do mês seguinte ou antes do envio da folha correspondente.")
        ]),
        ("MÓDULO 05: AFASTAMENTOS TEMPORÁRIOS (S-2230)", [
            ("Atestados Médicos", "Afastamentos por doença não ocupacional superiores a 15 dias devem ser informados até o dia 15 do mês seguinte."),
            ("Acidente de Trabalho", "Afastamento decorrente de acidente de trabalho deve ser enviado até o primeiro dia útil seguinte ao da ocorrência (vinculado à CAT S-2210)."),
            ("Licença Maternidade", "Informar o início e o retorno da licença maternidade para correta dedução na apuração previdenciária.")
        ]),
        ("MÓDULO 06: GESTÃO E TRANSMISSÃO DE FÉRIAS", [
            ("Aviso de Férias", "CLT exige comunicação com 30 dias de antecedência ao empregado. No eSocial, o aviso prévio de férias não gera evento próprio isolado, mas o afastamento sim."),
            ("Afastamento por Férias (S-2230)", "Transmitido indicando o motivo 15 (Férias). Deve ser enviado até o dia 15 do mês seguinte ao início das férias (ou antes do desligamento, caso ocorra)."),
            ("Pagamento das Férias (S-1210)", "O adiantamento e o terço constitucional entram no evento S-1210 conforme a data efetiva do pagamento (que deve ocorrer 2 dias antes do início do gozo).")
        ]),
        ("MÓDULO 07: FOLHA DE PAGAMENTO (S-1200 E S-1210)", [
            ("S-1200 (Remuneração do Trabalhador)", "Regime de competência: contém todas as verbas devidas ao trabalhador naquele mês de apuração."),
            ("S-1210 (Pagamento de Rendimentos)", "Regime de caixa: data real em que o dinheiro caiu na conta do empregado. Define o fato gerador do Imposto de Renda Retido na Fonte (IRRF)."),
            ("Prazo de Envio", "Até o dia 15 do mês subsequente ao período de apuração (antecipando-se caso não seja dia útil).")
        ]),
        ("MÓDULO 08: DESLIGAMENTO E RESCISÃO (S-2299 E S-2399)", [
            ("S-2299 (Desligamento de Celetista)", "Prazo: até o 10º (décimo) dia corrido seguinte ao término do contrato, caso não haja aviso trabalhado; ou no primeiro dia útil seguinte se o término for por fim de contrato a termo."),
            ("Impacto no FGTS Digital", "A liberação do saque rescisório e a geração da guia de multa rescisória dependem do envio tempestivo e sem erros do S-2299."),
            ("S-2399 (Término de TSVE)", "Aplicável a estagiários e diretores não empregados.")
        ]),
        ("MÓDULO 09: TRABALHADORES SEM VÍNCULO - TSVE (S-2300)", [
            ("Estagiários e Pró-Labore", "Sócios que retiram pró-labore, estagiários e autônomos entram sob o código S-2300."),
            ("Prazo de Início", "Deve ser transmitido até o dia 15 do mês subsequente ao início das atividades ou antes do envio de sua respectiva remuneração (S-1200).")
        ]),
        ("MÓDULO 10: SST NO eSOCIAL (S-2210, S-2220 E S-2240)", [
            ("S-2210 (CAT)", "Comunicação de Acidente de Trabalho. Prazo: até o 1º dia útil seguinte ao acidente (ou imediatamente em caso de morte)."),
            ("S-2220 (Monitoramento da Saúde / ASO)", "Informações dos exames admissionais, periódicos, de retorno e demissionais. Prazo: dia 15 do mês seguinte."),
            ("S-2240 (Condições Ambientais do Trabalho)", "Registra agentes nocivos que ensejam aposentadoria especial (LTCAT). Prazo: dia 15 do mês seguinte à contratação ou alteração de risco.")
        ]),
        ("MÓDULO 11: FECHAMENTO DE PERIÓDICOS (S-1298 E S-1299)", [
            ("S-1299 (Fechamento)", "Informa o encerramento do envio de remunerações daquele mês. Dispara a apuração e alimenta a DCTFWeb."),
            ("S-1298 (Reabertura)", "Necessário caso surja alguma retificação de holerite após o fechamento. Atenção: reabrir a folha exige novo fechamento e reemissão de guia na DCTFWeb.")
        ]),
        ("MÓDULO 12: INTEGRAÇÃO eSOCIAL + DCTFWeb", [
            ("Transmissão Automática", "Com o fechamento do S-1299, os débitos previdenciários e de IRRF são consolidados na DCTFWeb."),
            ("Conferência de Guias", "Bata o resumo da folha do seu software de DP com o relatório do eSocial antes de transmitir a DCTFWeb para evitar DARF com valor divergente.")
        ]),
        ("MÓDULO 13: TABELA DE PRAZOS CRÍTICOS X MULTAS", [
            ("Admissão Fora do Prazo", "Prazo: 1 dia antes do início. Multa: R$ 3.000 por empregado (R$ 800 para ME/EPP) - Art. 47 da CLT."),
            ("Atraso no S-2299 (Rescisão)", "Prazo: 10 dias corridos. Multa: 1 salário do empregado (Art. 477 da CLT) + penalidades administrativas."),
            ("Omissão de SST (S-2240/2220)", "Prazo: Dia 15 do mês subsequente. Multas da NR-28 e legislação previdenciária de R$ 400 a R$ 40.000.")
        ]),
        ("MÓDULO 14: CHECKLIST PRÉ-TRANSMISSÃO DE DP", [
            ("Fase 1: Cadastro", "Conferir CPF na base da Receita, qualificação cadastral e dados bancários."),
            ("Fase 2: Folha", "Validar rubricas com eSocial, conferir afastamentos lançados e fechar ponto."),
            ("Fase 3: SST", "Garantir recebimento dos ASOs e laudos das clínicas antes do fechamento."),
            ("Fase 4: Finalização", "Enviar S-1200/1210 -> Fechar no S-1299 -> Acessar DCTFWeb -> Emitir DARF numerado.")
        ])
    ]
    
    for titulo, topicos in conteudos_modulos:
        story.append(Paragraph(titulo, h1_style))
        story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=8))
        
        table_rows = []
        for rotulo, texto in topicos:
            table_rows.append([
                Paragraph(f"<b>{rotulo}</b>", body_bold),
                Paragraph(texto, body_style)
            ])
            
        t_mod = Table(table_rows, colWidths=[130, 385])
        t_mod.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), GRAY_BG),
            ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
            ('PADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(t_mod)
        story.append(Spacer(1, 14))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Produto Principal gerado com sucesso em: {pdf_path}")

def create_bonus_pdfs():
    bonus_files = [
        ("bonus_01_mapa_visual_sst.pdf", "BÔNUS #1: MAPA VISUAL DE SST NO eSOCIAL", [
            ("S-2210 - CAT", "Comunicação de Acidente de Trabalho. Deve ser emitido em até 1 dia útil após o acidente. Exige CID-10, dados do atestado e local do acidente."),
            ("S-2220 - ASO", "Monitoramento da Saúde do Trabalhador. Envolve exames Admissional, Periódico, Retorno ao Trabalho, Mudança de Risco e Demissional. Prazo: Dia 15 do mês seguinte."),
            ("S-2240 - Condições Ambientais", "Laudo das condições de trabalho (LTCAT). Informa exposição a ruído, calor, químicos ou biológicos para fins de aposentadoria especial."),
            ("Dispensa de PGR/PCMSO", "MEI, ME e EPP graus de risco 1 e 2 sem riscos físicos/químicos/biológicos declaram DIR (Declaração de Inexistência de Risco).")
        ]),
        ("bonus_02_calendario_prazos_dp.pdf", "BÔNUS #2: CALENDÁRIO VISUAL DE PRAZOS DE DP", [
            ("Dia 1 Anterior ao Início", "Prazo limite para transmissão da admissão preliminar (S-2190) ou definitiva (S-2200)."),
            ("Dia 07 de Cada Mês", "Vencimento tradicional da guia de FGTS Digital (gerada via ambiente unificado)."),
            ("Dia 10 Dias Corridos", "Prazo limite de pagamento da rescisão e envio do evento de desligamento (S-2299)."),
            ("Dia 15 de Cada Mês", "Prazo limite para envio da Folha de Pagamento (S-1200 e S-1210) e eventos de SST."),
            ("Dia 20 de Cada Mês", "Vencimento do DARF Previdenciário / DCTFWeb (antecipa se cair em fim de semana ou feriado).")
        ]),
        ("bonus_03_guia_antes_depois_rotinas.pdf", "BÔNUS #3: ANTES x DEPOIS DAS ROTINAS DE DP", [
            ("Admissão", "Antes: Livro de registro físico ou ficha de papel. Agora: CTPS Digital abastecida pelo evento S-2200 do eSocial."),
            ("Folha e Previdência", "Antes: Envio mensal da GFIP / SEFIP e emissão de GPS. Agora: Transmissão do S-1200/1299 e guia única DARF via DCTFWeb."),
            ("Rescisão e Homologação", "Antes: GRRF na Caixa e homologação presencial em sindicato. Agora: Evento S-2299 com emissão de guia no FGTS Digital."),
            ("Fiscalização Trabalhista", "Antes: Fiscal presencial solicitando livros físicos. Agora: Malhas fiscais digitais com cruzamento automatizado de dados.")
        ]),
        ("bonus_04_50_perguntas_respostas_erros.pdf", "BÔNUS #4: 50 RESPOSTAS SOBRE ERROS NO eSOCIAL", [
            ("Erro 102 - O evento informado não foi reconhecido", "Solução: Verifique se o schema XML do seu software está atualizado com a versão corrente do MOS."),
            ("Erro 162 - O trabalhador já se encontra cadastrado", "Solução: O CPF já possui admissão ativa para esta matrícula. Consulte os eventos já aceitos no portal web."),
            ("Erro 246 - Código de Rubrica não existe", "Solução: Transmita primeiro a tabela de rubricas (S-1010) antes de enviar a folha de pagamento."),
            ("Erro 724 - Não foi localizado evento de admissão para o trabalhador", "Solução: O evento S-2200 foi rejeitado ou não transmitido. Verifique a ordem cronológica.")
        ]),
        ("bonus_05_checklist_fechamento_folha.pdf", "BÔNUS #5: CHECKLIST DE FECHAMENTO DE FOLHA", [
            ("[  ] Passo 1", "Conferir admissões do mês e garantir que todas têm recibo do S-2200."),
            ("[  ] Passo 2", "Lançar e validar afastamentos médicos superiores a 15 dias (S-2230)."),
            ("[  ] Passo 3", "Verificar rescisões calculadas e transmitidas no prazo de 10 dias (S-2299)."),
            ("[  ] Passo 4", "Conferir apontamento de horas extras, adicionais e faltas."),
            ("[  ] Passo 5", "Transmitir eventos de remuneração (S-1200) e pagamentos (S-1210)."),
            ("[  ] Passo 6", "Emitir relatório de fechamento e transmitir encerramento no S-1299."),
            ("[  ] Passo 7", "Acessar ambiente da DCTFWeb, conferir débitos e emitir DARF numerado."),
            ("[  ] Passo 8", "Emitir e conferir guias do FGTS Digital.")
        ])
    ]
    
    styles = getSampleStyleSheet()
    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=NAVY,
        spaceBefore=10,
        spaceAfter=6
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=NAVY_LIGHT
    )
    body_bold = ParagraphStyle('BodyBold', parent=body_style, fontName='Helvetica-Bold')

    for fname, title, content in bonus_files:
        pdf_path = os.path.join(BONUS_DIR, fname)
        doc = SimpleDocTemplate(
            pdf_path,
            pagesize=A4,
            leftMargin=40,
            rightMargin=40,
            topMargin=55,
            bottomMargin=55
        )
        story = []
        story.append(Paragraph(title, h1_style))
        story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=12))
        story.append(Paragraph("<font size='9' color='#64748B'>Material Bônus Exclusivo • Plano Completo Mapa Fácil</font>", body_style))
        story.append(Spacer(1, 10))
        
        t_data = []
        for r, t in content:
            t_data.append([Paragraph(f"<b>{r}</b>", body_bold), Paragraph(t, body_style)])
            
        table = Table(t_data, colWidths=[130, 385])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), GRAY_BG),
            ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
            ('PADDING', (0,0), (-1,-1), 8),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(table)
        doc.build(story, canvasmaker=NumberedCanvas)
        print(f"Bônus gerado com sucesso em: {pdf_path}")

if __name__ == "__main__":
    create_main_product()
    create_bonus_pdfs()
