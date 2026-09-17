from pathlib import Path
from html import escape

from pypdf import PageObject, PdfReader, PdfWriter, Transformation
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, A5, B5, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    PageBreak,
    PageTemplate,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = Path(__file__).resolve().parent / "output" / "pdf"
TMP_DIR = Path("/private/tmp/pralaya_print_pdfs")
FOLD_PANEL_DIR = TMP_DIR / "fold-panels"
SUMMARY_A5 = TMP_DIR / "summary-a5.pdf"
SUMMARY_B5 = TMP_DIR / "summary-b5.pdf"
FAQ_B5 = TMP_DIR / "faq-b5.pdf"
SUMMARY_CUT_OVERLAY = TMP_DIR / "summary-cut-overlay.pdf"
SUMMARY_B7 = TMP_DIR / "summary-b7.pdf"
SUMMARY_B7_CUT_OVERLAY = TMP_DIR / "summary-b7-cut-overlay.pdf"
SUMMARY_OUT = OUT_DIR / "Pralaya_Chinese_Rule_Summary_A5_Booklet_A4_2up_SingleSided.pdf"
SUMMARY_B5_OUT = OUT_DIR / "Pralaya_Chinese_Rule_Summary_B5_Lawson_Straight.pdf"
SUMMARY_B7_OUT = OUT_DIR / "Pralaya_Chinese_Rule_Summary_B7_BoxInsert_A4_4up_SingleSided.pdf"
FAQ_OUT = OUT_DIR / "Pralaya_FAQ_Trilingual_A4_SingleSided.pdf"
FAQ_B5_OUT = OUT_DIR / "Pralaya_FAQ_Trilingual_B5_Lawson_Straight.pdf"
SUMMARY_FOLD_OUT = OUT_DIR / "Pralaya_Chinese_Rule_Summary_A4_6Panel_Duplex_FoldOnly.pdf"
FAQ_FOLD_OUT = OUT_DIR / "Pralaya_FAQ_Trilingual_A4_6Panel_Duplex_FoldOnly.pdf"

B7_PAGE = (90 * mm, 125 * mm)
FOLD_PANEL_PAGE = (99 * mm, 105 * mm)


NAVY = colors.HexColor("#21405e")
OCEAN = colors.HexColor("#347d9f")
SAND = colors.HexColor("#f6f0e5")
INK = colors.HexColor("#263238")
MUTED = colors.HexColor("#66737a")
LINE = colors.HexColor("#c9d5da")
ACCENT = colors.HexColor("#bf7c43")

UNICODE_FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
pdfmetrics.registerFont(TTFont("CJK", UNICODE_FONT))
pdfmetrics.registerFont(TTFont("CJK-Bold", UNICODE_FONT))
pdfmetrics.registerFontFamily("CJK", normal="CJK", bold="CJK-Bold", italic="CJK", boldItalic="CJK-Bold")


def style(name, font, size, leading=None, **kwargs):
    kwargs.setdefault("textColor", INK)
    kwargs.setdefault("spaceAfter", 4)
    return ParagraphStyle(
        name,
        fontName=font,
        fontSize=size,
        leading=leading or size * 1.42,
        **kwargs,
    )


CN_BODY = style("cn-body", "CJK", 9.2, 13.2)
CN_SMALL = style("cn-small", "CJK", 7.2, 9.6, textColor=MUTED)
CN_H1 = style("cn-h1", "CJK", 17, 22, textColor=NAVY, spaceAfter=8)
CN_H2 = style("cn-h2", "CJK", 12.2, 16, textColor=OCEAN, spaceBefore=5, spaceAfter=5)
CN_H3 = style("cn-h3", "CJK", 10.2, 13, textColor=NAVY, spaceBefore=3, spaceAfter=3)
CN_COVER = style("cn-cover", "CJK", 22, 30, textColor=NAVY, alignment=TA_CENTER)
CN_COVER_SUB = style("cn-cover-sub", "CJK", 11, 16, textColor=OCEAN, alignment=TA_CENTER)
CN_TABLE = style("cn-table", "CJK", 7.2, 9.2)
CN_TABLE_HEAD = style("cn-table-head", "CJK", 7.2, 9.2, textColor=colors.white)

B7_BODY = style("b7-body", "CJK", 7.0, 9.2, spaceAfter=2)
B7_SMALL = style("b7-small", "CJK", 5.6, 7.0, textColor=MUTED, spaceAfter=1)
B7_H1 = style("b7-h1", "CJK", 12.4, 15.0, textColor=NAVY, spaceAfter=4)
B7_H2 = style("b7-h2", "CJK", 8.9, 11.0, textColor=OCEAN, spaceBefore=3, spaceAfter=3)
B7_COVER = style("b7-cover", "CJK", 16.5, 21, textColor=NAVY, alignment=TA_CENTER, spaceAfter=3)
B7_COVER_SUB = style("b7-cover-sub", "CJK", 8.6, 11, textColor=OCEAN, alignment=TA_CENTER, spaceAfter=2)
B7_TABLE = style("b7-table", "CJK", 5.65, 7.15, spaceAfter=0)
B7_TABLE_HEAD = style("b7-table-head", "CJK", 5.65, 7.15, textColor=colors.white, spaceAfter=0)

JA_BODY = style("ja-body", "CJK", 9.5, 13.8)
JA_SMALL = style("ja-small", "CJK", 7.4, 9.7, textColor=MUTED)
JA_H1 = style("ja-h1", "CJK", 18, 23, textColor=NAVY, spaceAfter=8)
JA_H2 = style("ja-h2", "CJK", 13.2, 17, textColor=OCEAN, spaceBefore=6, spaceAfter=5)
JA_H3 = style("ja-h3", "CJK", 10.4, 14, textColor=NAVY, spaceBefore=4, spaceAfter=3)

EN_BODY = style("en-body", "Helvetica", 9.5, 13.8)
EN_SMALL = style("en-small", "Helvetica", 7.4, 9.7, textColor=MUTED)
EN_H1 = style("en-h1", "Helvetica", 18, 23, textColor=NAVY, spaceAfter=8)
EN_H2 = style("en-h2", "Helvetica", 13.2, 17, textColor=OCEAN, spaceBefore=6, spaceAfter=5)
EN_H3 = style("en-h3", "Helvetica", 10.4, 14, textColor=NAVY, spaceBefore=4, spaceAfter=3)
B5_EN_BODY = style("b5-en-body", "CJK", 9.5, 13.8)
B5_EN_SMALL = style("b5-en-small", "CJK", 7.4, 9.7, textColor=MUTED)
B5_EN_H1 = style("b5-en-h1", "CJK", 18, 23, textColor=NAVY, spaceAfter=8)
B5_EN_H2 = style("b5-en-h2", "CJK", 13.2, 17, textColor=OCEAN, spaceBefore=6, spaceAfter=5)

FOLD_BODY = style("fold-body", "CJK", 7.15, 9.2, spaceAfter=1.2)
FOLD_SMALL = style("fold-small", "CJK", 5.75, 7.1, textColor=MUTED, spaceAfter=1)
FOLD_H1 = style("fold-h1", "CJK", 12.3, 14.6, textColor=NAVY, spaceAfter=3)
FOLD_H2 = style("fold-h2", "CJK", 8.8, 10.7, textColor=OCEAN, spaceBefore=2, spaceAfter=2)
FOLD_COVER = style("fold-cover", "CJK", 15.5, 19, textColor=NAVY, alignment=TA_CENTER, spaceAfter=2)
FOLD_COVER_SUB = style("fold-cover-sub", "CJK", 8.4, 10.5, textColor=OCEAN, alignment=TA_CENTER, spaceAfter=2)
FOLD_EN_BODY = style("fold-en-body", "Helvetica", 7.1, 9.25, spaceAfter=1.2)
FOLD_EN_SMALL = style("fold-en-small", "Helvetica", 5.8, 7.15, textColor=MUTED, spaceAfter=1)
FOLD_EN_H1 = style("fold-en-h1", "Helvetica", 12.3, 14.6, textColor=NAVY, spaceAfter=3)
FOLD_TABLE = style("fold-table", "CJK", 5.75, 7.1, spaceAfter=0)
FOLD_TABLE_HEAD = style("fold-table-head", "CJK", 5.75, 7.1, textColor=colors.white, spaceAfter=0)
FOLD_EN_TABLE = style("fold-en-table", "Helvetica", 5.75, 7.1, spaceAfter=0)
FOLD_EN_TABLE_HEAD = style("fold-en-table-head", "Helvetica", 5.75, 7.1, textColor=colors.white, spaceAfter=0)


def P(text, st):
    return Paragraph(escape(text).replace("\n", "<br/>").replace("  ", " &nbsp;"), st)


def rich(text, st):
    return Paragraph(text, st)


def bullets(items, st):
    return [rich(f"• {escape(item)}", st) for item in items]


def section_rule():
    return HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=2, spaceAfter=7)


def footer(canvas, doc, label="2018 Revised Edition"):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(doc.leftMargin, 13 * mm, doc.pagesize[0] - doc.rightMargin, 13 * mm)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 8 * mm, label)
    canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 8 * mm, f"Page {canvas.getPageNumber()}")
    canvas.restoreState()


def summary_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(doc.leftMargin, 13 * mm, doc.pagesize[0] - doc.rightMargin, 13 * mm)
    canvas.setFont("CJK", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 8 * mm, "2018 Revised Edition | 简体中文规则摘要")
    canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 8 * mm, f"第 {canvas.getPageNumber()} 页")
    canvas.restoreState()


def b7_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.3)
    canvas.line(doc.leftMargin, 7 * mm, doc.pagesize[0] - doc.rightMargin, 7 * mm)
    canvas.setFont("CJK", 5.2)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 3.5 * mm, "2018 Revised Edition | 箱内保存用")
    canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 3.5 * mm, f"{canvas.getPageNumber()}/8")
    canvas.restoreState()


def table(data, widths, repeat=1, font_style=CN_TABLE, head_style=CN_TABLE_HEAD, padding=3):
    converted = []
    for row_i, row in enumerate(data):
        row_style = head_style if row_i == 0 else font_style
        converted.append([rich(escape(str(cell)), row_style) for cell in row])
    t = Table(converted, colWidths=widths, repeatRows=repeat, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), padding + 1),
                ("RIGHTPADDING", (0, 0), (-1, -1), padding + 1),
                ("TOPPADDING", (0, 0), (-1, -1), padding),
                ("BOTTOMPADDING", (0, 0), (-1, -1), padding),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, SAND]),
            ]
        )
    )
    return t


def _build_summary_source(output_path, page_size, left_margin, right_margin, top_margin, bottom_margin, title, footer_fn):
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=page_size,
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=top_margin,
        bottomMargin=bottom_margin,
        title=title,
        author="Codex",
    )
    story = []

    story += [Spacer(1, 28 * mm), P("《王国沉没》", CN_COVER), P("Pralaya Revised Edition", CN_COVER_SUB), Spacer(1, 8 * mm)]
    story += [rich("<b>简体中文规则摘要</b>", CN_COVER_SUB), Spacer(1, 14 * mm)]
    story += [P("2018年11月修订版 | 简体中文规则摘要", CN_SMALL), Spacer(1, 10 * mm), section_rule()]
    story += [P("术语：遗迹牌、行动点、圣典、救生船。规则基准：Pralaya Revised Edition。", CN_BODY)]
    story += [PageBreak()]

    story += [P("1. 游戏目标与组件", CN_H1), section_rule()]
    story += [P("在岛屿沉入大海之前收集珍贵遗迹并逃离岛屿。带着最多遗迹逃离的玩家获胜；等待太久会与岛屿一起沉没。", CN_BODY)]
    story += [P("组件", CN_H2)]
    story += bullets(["规则书 x 1", "卡牌 x 95（遗迹牌、圣典牌、救生船牌）"], CN_BODY)
    story += [P("遗迹牌的行动点是收集成本；铜币、银币和金币在逃离前同时具有货币价值。圣典和救生船不是遗迹牌，而是通过货币购买。", CN_BODY)]
    story += [P("基本术语", CN_H2)]
    term_data = [
        ["日本語", "English", "简体中文"],
        ["遺物カード", "Relic card", "遗迹牌"],
        ["行動力", "Vitality", "行动点"],
        ["聖典", "Veda", "圣典"],
        ["ドーニー", "Dhoni", "救生船"],
        ["海", "Ocean", "海洋"],
    ]
    story += [table(term_data, [105, 105, 105])]
    story += [PageBreak()]

    story += [P("2. 游戏准备", CN_H1), section_rule()]
    story += bullets(
        [
            "将包括海洋牌在内的所有遗迹牌洗匀，背面朝上组成遗迹牌库。",
            "取出与玩家人数相同数量的圣典牌和救生船牌。救生船按价格X、之后从低到高叠放。",
            "2～3人：从牌库抽15张，摆成3 x 5；4～5人：抽18张，摆成3 x 6。所有牌面朝上组成岛屿。",
            "决定首位玩家，之后依次由左手边玩家进行回合。",
        ],
        CN_BODY,
    )
    story += [P("救生船价格配置", CN_H2)]
    story += [table([["玩家人数", "使用的救生船价格"], ["2人", "X、7"], ["3人", "X、7、4"], ["4人", "X、7、4、2"], ["5人", "X、7、4、2、10"]], [75, 240])]
    story += [Spacer(1, 5), P("可以查看救生船牌背面的玩家人数标记来确认使用哪些牌。没有人数标记的牌始终使用。", CN_BODY), PageBreak()]

    story += [P("3. 回合流程", CN_H1), section_rule()]
    turn_data = [
        ["步骤", "处理"],
        ["1", "回合开始拥有3点行动。第一轮中，首位玩家第一次回合为1点，第二位玩家第一次回合为2点。"],
        ["2", "消耗行动点，从岛上至少收集1张面朝上的遗迹牌。行动点可以剩余，但不能保留到下回合。"],
        ["3", "收集后，可以弃置货币购买圣典或救生船牌叠最上方的一张。支付超过价格不找零；同回合不能同时买两种牌。"],
        ["4", "从遗迹牌库补充因收集而产生的空位。"],
        ["5", "补充完成后回合结束，由左手边玩家继续。"],
    ]
    story += [table(turn_data, [33, 282])]
    story += [Spacer(1, 6), P("重点：每个回合必须至少收集1张遗迹牌。只有完成遗迹收集后，才进行圣典或救生船的购买。", CN_BODY)]
    story += [PageBreak()]

    story += [P("4. 购买、逃离、结束与计分", CN_H1), section_rule()]
    story += [P("购买", CN_H2)]
    story += bullets(["价格为数值的牌：弃置铜币、银币和／或金币，使总货币价值至少达到价格。", "价格X的救生船：弃置手牌中的所有货币；没有货币时可以免费购买。", "圣典和救生船不能在同一回合同时购买；每种牌每位玩家最多1张。"], CN_BODY)
    story += [P("逃离后", CN_H2)]
    story += [P("购买救生船后立即逃离。逃离玩家仍要进行自己的回合，但不再收集遗迹牌；改为选择岛上的1张遗迹牌弃置，再由牌库补充。", CN_BODY)]
    story += [P("游戏结束", CN_H2)]
    story += bullets(["所有玩家都已逃离。", "补充后岛上全是海洋牌。", "回合开始时只有1张非海洋遗迹牌，并完成该回合的购买步骤。"], CN_BODY)
    story += [P("计分", CN_H2)]
    story += bullets(["没有救生船的玩家不计分，自动排在所有逃离玩家之后。", "逃离玩家计算手中所有遗迹牌的得分。", "平分时，回合顺序中距离首位玩家最远的玩家获胜。"], CN_BODY)
    story += [PageBreak()]

    story += [P("5. 卡牌效果速查", CN_H1), section_rule()]
    card_data = [
        ["卡牌", "数量", "成本", "得分／效果"],
        ["铜币", "4", "1", "每张1分；逃离前货币价值1"],
        ["银币", "6", "2", "每张3分；逃离前货币价值3"],
        ["金币", "5", "3", "每张6分；逃离前货币价值6"],
        ["恶魔雕像", "8", "1", "每张2分；受恶魔契约倍率影响"],
        ["古代手稿", "8", "1", "每2张5分"],
        ["文物碎片", "9", "2", "每3张20分"],
        ["伟大雕像", "8", "1", "数量的平方"],
        ["恶魔契约", "4", "2", "恶魔雕像得分乘-3；2张为+9，3张为-27，4张为+81"],
        ["贤者", "3", "2", "不同卡牌种类数；圣典、救生船、贤者也计入"],
        ["祭司", "1", "3", "恶魔雕像0分；持有圣典时圣典15分"],
        ["化石", "7", "1", "化石最多者15分；同数则无人得分；无救生船者按0张处理"],
        ["海洋", "22", "不可收集", "无效果，只能留在岛上"],
    ]
    story += [table(card_data, [78, 32, 43, 162], font_style=CN_TABLE)]
    story += [PageBreak()]

    story += [P("6. 可购买卡牌与实战速查", CN_H1), section_rule()]
    buy_data = [
        ["卡牌", "购买", "效果"],
        ["圣典", "货币总价值达到价格", "逃离前每回合开始拥有4点行动；每人最多1张"],
        ["救生船", "数值价格：货币总价值达到价格；X：弃置所有货币", "立即逃离；以后弃置岛上1张遗迹代替收集；每人最多1张"],
    ]
    story += [table(buy_data, [62, 130, 123])]
    story += [P("一回合判定", CN_H2)]
    story += bullets(["先至少收集1张遗迹牌。", "行动点可以剩余，但不能保留。", "然后最多购买圣典或救生船其中一种。", "购买救生船后立即逃离，之后每回合弃置岛上1张遗迹并补充。", "最终只有逃离玩家计分。"], CN_BODY)
    story += [P("规则优先顺序", CN_H2)]
    story += [P("规则基准：Pralaya Revised Edition。中文商品资料和讨论帖仅作参考；规则冲突时以修订版规则书为准。", CN_BODY)]
    story += [PageBreak()]

    story += [P("8. 三语术语表与版本说明", CN_H1), section_rule()]
    story += [table(term_data, [105, 105, 105])]
    story += [P("版本说明", CN_H2)]
    story += [P("规则基准：2018 Revised Edition（修订版）。中文商品资料仅作术语参考；规则冲突时以修订版规则书为准。", CN_BODY)]
    story += [Spacer(1, 7), section_rule(), P("参照：Pralaya Revised Edition rulebook；中文术语参考《王国沉没》相关商品资料。", CN_SMALL)]

    doc.build(story, onFirstPage=footer_fn, onLaterPages=footer_fn)


def build_summary_a5():
    _build_summary_source(
        SUMMARY_A5,
        A5,
        15 * mm,
        15 * mm,
        15 * mm,
        19 * mm,
        "《王国沉没》（Pralaya）修订版规则摘要",
        summary_footer,
    )


def build_summary_b5():
    _build_summary_source(
        SUMMARY_B5_OUT,
        B5,
        17 * mm,
        17 * mm,
        16 * mm,
        19 * mm,
        "《王国沉没》（Pralaya）修订版规则摘要 - B5 direct print",
        summary_footer,
    )


def build_summary_b7():
    """Build the small Chinese insert before imposing four pages on A4."""
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(SUMMARY_B7),
        pagesize=B7_PAGE,
        leftMargin=6 * mm,
        rightMargin=6 * mm,
        topMargin=6 * mm,
        bottomMargin=11 * mm,
        title="《王国沉没》（Pralaya）修订版规则摘要 - 箱内保存用",
        author="Codex",
    )
    story = []
    table_kwargs = {"font_style": B7_TABLE, "head_style": B7_TABLE_HEAD, "padding": 1.8}

    # 1. Cover and overview
    story += [Spacer(1, 8 * mm), P("《王国沉没》", B7_COVER), P("Pralaya Revised Edition", B7_COVER_SUB)]
    story += [P("简体中文规则摘要｜箱内保存用", B7_COVER_SUB), Spacer(1, 3 * mm), section_rule()]
    story += [P("在岛屿沉入海底之前收集遗迹并逃离。带着最多遗迹逃离的玩家获胜；太晚逃离会与岛屿一起沉没。", B7_BODY)]
    story += [P("游戏范围", B7_H2), table([["玩家", "时间", "卡牌"], ["2～5人", "15～30分钟", "95张"]], [72, 72, 77], **table_kwargs)]
    story += [P("三步记忆", B7_H2)] + bullets(["收集：每回合至少拿1张面朝上的遗迹牌。", "购买：收集之后，最多买圣典或救生船其中一种。", "逃离：救生船立即使你逃离；之后弃置岛上遗迹来推进沉没。"], B7_BODY)
    story += [Spacer(1, 3), section_rule(), P("版本：本摘要只对应2018 Revised Edition（修订版）。若与其他资料冲突，以修订版规则书为准。", B7_SMALL), PageBreak()]

    # 2. Components and terms
    story += [P("1. 内容物与基本术语", B7_H1), section_rule()]
    story += [P("内容物", B7_H2)] + bullets(["遗迹牌95张（包括海洋牌）。", "圣典牌与救生船牌：按玩家人数各使用同样数量。"], B7_BODY)
    story += [P("三语术语表", B7_H2)]
    term_data = [
        ["日本語", "English", "简体中文"],
        ["遺物カード", "Relic card", "遗迹牌"],
        ["行動力", "Vitality", "行动点"],
        ["聖典", "Veda", "圣典"],
        ["ドーニー", "Dhoni", "救生船"],
        ["海", "Ocean", "海洋"],
    ]
    story += [table(term_data, [53, 58, 110], **table_kwargs)]
    story += [P("牌面信息", B7_H2), P("遗迹牌有名称、行动点、牌张数量、货币价值和效果／得分文字。只有铜币、银币、金币具有货币价值。圣典和救生船是购买牌，不是遗迹牌。海洋牌不能收集。", B7_BODY)]
    story += [PageBreak()]

    # 3. Setup
    story += [P("2. 游戏准备", B7_H1), section_rule()]
    story += bullets([
        "洗匀所有遗迹牌，背面朝上组成遗迹牌库。",
        "取出与玩家人数相同数量的圣典和救生船。圣典叠放；救生船按价格X在最上、其余从低到高叠放。",
        "2～3人：抽15张，面朝上摆成3×5。4～5人：抽18张，面朝上摆成3×6。",
        "共同决定首位玩家；之后依次由左手边玩家进行回合。",
    ], B7_BODY)
    story += [P("救生船价格配置", B7_H2)]
    story += [table([["人数", "本局使用的价格"], ["2人", "X、7"], ["3人", "X、7、4"], ["4人", "X、7、4、2"], ["5人", "X、7、4、2、10"]], [45, 176], **table_kwargs)]
    story += [Spacer(1, 3), P("无人数标记的救生船牌始终使用；有标记的牌按人数加入。Veda和Dhoni各使用与玩家人数相同数量。", B7_SMALL), PageBreak()]

    # 4. Turn flow
    story += [P("3. 回合流程", B7_H1), section_rule()]
    turn_data = [
        ["步骤", "处理"],
        ["1", "回合开始：通常有3点行动。第一轮首位玩家第一次回合为1点，第二位玩家第一次回合为2点。圣典持有者在逃离前每回合开始有4点。"],
        ["2", "收集：消耗行动点，从岛上至少收集1张面朝上的遗迹牌。可以留有行动点，但不能带到下回合。"],
        ["3", "购买：完成收集后，可弃置货币购买圣典或救生船牌叠最上方的一张；同回合不能两种都买。"],
        ["4", "补充：从遗迹牌库面朝上补足空位。"],
        ["5", "结束：补充完成后回合结束，由左手边玩家继续。"],
    ]
    story += [table(turn_data, [21, 200], **table_kwargs)]
    story += [Spacer(1, 4), P("关键限制", B7_H2)] + bullets(["每回合必须至少收集1张遗迹牌。", "行动点可以不使用完，但不能储存。", "购买必须在遗迹收集之后。每种购买牌每位玩家最多1张。"], B7_BODY) + [PageBreak()]

    # 5. Purchase and escape
    story += [P("4. 圣典、救生船与脱出", B7_H1), section_rule()]
    buy_data = [
        ["牌", "购买与效果"],
        ["圣典（Veda）", "用铜币、银币、金币支付达到牌上价格的总价值。购买后，在逃离前每回合开始拥有4点行动；每人最多1张。"],
        ["救生船（Dhoni）", "数值价格：支付总价值达到价格，超过不找零。购买后立即逃离；每人最多1张。"],
        ["价格X的救生船", "弃置手牌中的所有铜币、银币、金币；没有货币时可免费购买。X不是数值价格。购买后立即逃离。"],
    ]
    story += [table(buy_data, [48, 173], **table_kwargs)]
    story += [P("脱出后", B7_H2), P("你仍继续自己的回合，但不再收集遗迹牌；改为选择岛上的1张遗迹牌弃置，再从牌库补充1张。", B7_BODY)]
    story += [P("支付顺序", B7_H2)] + bullets(["先至少收集1张遗迹牌。", "然后最多购买圣典或救生船其中一种。", "购买救生船会立即脱出，并改变你之后回合的收集动作。"], B7_BODY) + [PageBreak()]

    # 6. End and scoring
    story += [P("5. 游戏结束与计分", B7_H1), section_rule()]
    story += [P("满足任一条件时结束", B7_H2)] + bullets(["所有玩家都已从岛上逃离。", "第4步补充后，岛上全是海洋牌。", "回合开始时只有1张非海洋牌，并完成该回合的购买步骤。"], B7_BODY)
    story += [P("计分", B7_H2)] + bullets(["未逃离（面前没有救生船）的玩家不计分，自动排在所有逃离玩家之后。", "逃离玩家计算自己所有遗迹牌的得分，包括仍在手中的货币牌按卡牌得分计。", "即使逃离玩家得分为负，也排在未逃离玩家之前。", "平分时，按回合顺序距离首位玩家最远者获胜。"], B7_BODY)
    story += [P("注意：救生船购买后的弃置与补充仍会推进岛屿沉没，因此逃离玩家必须继续回合。", B7_SMALL), PageBreak()]

    # 7. Card effects
    story += [P("6. 卡牌效果一览", B7_H1), section_rule()]
    card_data = [
        ["卡牌", "收集／价", "得分／效果"],
        ["铜币", "1", "每张1分；逃离前货币值1。"],
        ["银币", "2", "每张3分；逃离前货币值3。"],
        ["金币", "3", "每张6分；逃离前货币值6。"],
        ["恶魔雕像", "1", "每张2分；受恶魔契约倍率影响。"],
        ["古代手稿", "1", "每2张5分；不足2张不得分。"],
        ["文物碎片", "2", "每3张20分；不足3张不得分。"],
        ["伟大雕像", "1", "得分为持有数量的平方。"],
        ["恶魔契约", "2", "恶魔雕像得分乘(-3)^n；n=1/2/3/4时为-3/+9/-27/+81倍。"],
        ["贤者", "2", "得分等于不同卡牌种类数；含圣典、救生船、贤者。"],
        ["祭司", "3", "恶魔雕像0分；持有圣典时圣典15分。"],
        ["化石", "1", "化石最多者15分；平分无人得分；无救生船者按0张。"],
        ["海洋", "不可收集", "无效果。"],
        ["圣典", "购买", "逃离前每回合开始4点行动。"],
        ["救生船", "购买", "立即逃离；之后弃置岛上1张遗迹代替收集。"],
    ]
    story += [table(card_data, [48, 39, 134], **table_kwargs)]
    story += [PageBreak()]

    # 8. Quick reference and glossary
    story += [P("7. 一回合速查与三语术语", B7_H1), section_rule()]
    story += [P("一回合速查", B7_H2)] + bullets(["① 回合开始获得行动点（通常3；圣典持有者4；第一轮首位1、第二位2）。", "② 至少拿1张面朝上的遗迹牌；行动点可剩余但不保留。", "③ 收集后，最多买圣典或救生船其中一种。", "④ 普通玩家补空位；救生船持有者弃置岛上1张遗迹并补1张。", "⑤ 依左手边玩家继续，直到满足结束条件。"], B7_BODY)
    story += [P("术语快速对照", B7_H2)]
    story += [table(term_data, [53, 58, 110], **table_kwargs)]
    story += [P("最终检查", B7_H2)] + bullets(["只有逃离玩家计分。", "恶魔契约倍率：1=-3×、2=+9×、3=-27×、4=+81×。", "规则冲突时：修订版规则书 > 适用的官方FAQ > 社区讨论。"], B7_BODY)
    story += [Spacer(1, 2), section_rule(), P("离线可用。Web资料只用于术语和出处追踪；本页不依赖网络。", B7_SMALL)]

    doc.build(story, onFirstPage=b7_footer, onLaterPages=b7_footer)


def impose_summary_b7_4up():
    reader = PdfReader(str(SUMMARY_B7))
    a4w, a4h = A4
    b7w, b7h = B7_PAGE
    cut_canvas = Canvas(str(SUMMARY_B7_CUT_OVERLAY), pagesize=A4)
    cut_canvas.setStrokeColor(MUTED)
    cut_canvas.setLineWidth(0.35)
    cut_canvas.setDash(2, 2)
    # The four B7 pages are centered on an A4 portrait sheet: 2 x 2, one-sided.
    x_positions = [15 * mm, 105 * mm]
    # Keep page order intuitive after cutting: 1-2 on the top row, 3-4 below.
    y_positions = [161 * mm, 11 * mm]
    cut_canvas.line(105 * mm, 8 * mm, 105 * mm, a4h - 8 * mm)
    cut_canvas.line(15 * mm, 148.5 * mm, 195 * mm, 148.5 * mm)
    cut_canvas.setDash()
    cut_canvas.setFont("CJK", 5.5)
    cut_canvas.setFillColor(MUTED)
    cut_canvas.drawCentredString(105 * mm, 145 * mm, "CUT / 裁断")
    # Short crop marks make the intended 90 x 125 mm trim visible without
    # placing heavy lines across the printed pages.
    mark = 3 * mm
    for x in x_positions:
        for y in y_positions:
            cut_canvas.line(x - mark, y, x, y)
            cut_canvas.line(x, y - mark, x, y)
            cut_canvas.line(x + b7w, y, x + b7w + mark, y)
            cut_canvas.line(x + b7w, y - mark, x + b7w, y)
            cut_canvas.line(x - mark, y + b7h, x, y + b7h)
            cut_canvas.line(x, y + b7h, x, y + b7h + mark)
            cut_canvas.line(x + b7w, y + b7h, x + b7w + mark, y + b7h)
            cut_canvas.line(x + b7w, y + b7h, x + b7w, y + b7h + mark)
    cut_canvas.save()
    overlay = PdfReader(str(SUMMARY_B7_CUT_OVERLAY)).pages[0]
    writer = PdfWriter()
    for start in range(0, len(reader.pages), 4):
        page = PageObject.create_blank_page(width=a4w, height=a4h)
        for slot in range(4):
            index = start + slot
            if index >= len(reader.pages):
                continue
            row = slot // 2
            col = slot % 2
            page.merge_transformed_page(
                reader.pages[index],
                Transformation().translate(tx=x_positions[col], ty=y_positions[row]),
                over=True,
            )
        page.merge_page(overlay)
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": "Pralaya Chinese Rule Summary - B7 Box Insert 4-up",
            "/Author": "Codex",
            "/Subject": "2018 Revised Edition Chinese rule summary for single-sided A4 printing and box storage",
        }
    )
    with SUMMARY_B7_OUT.open("wb") as stream:
        writer.write(stream)


def impose_summary_2up():
    reader = PdfReader(str(SUMMARY_A5))
    a4_landscape = landscape(A4)
    a4w, a4h = a4_landscape
    a5w, a5h = A5
    cut_canvas = Canvas(str(SUMMARY_CUT_OVERLAY), pagesize=a4_landscape)
    cut_canvas.setStrokeColor(MUTED)
    cut_canvas.setLineWidth(0.45)
    cut_canvas.setDash(2, 2)
    cut_canvas.line(a5w, 8 * mm, a5w, a4h - 8 * mm)
    cut_canvas.setDash()
    cut_canvas.setFont("CJK", 6)
    cut_canvas.setFillColor(MUTED)
    cut_canvas.drawCentredString(a5w, 4 * mm, "CUT / 裁断")
    cut_canvas.save()
    overlay = PdfReader(str(SUMMARY_CUT_OVERLAY)).pages[0]
    writer = PdfWriter()
    for start in range(0, len(reader.pages), 2):
        page = PageObject.create_blank_page(width=a4w, height=a4h)
        for slot in range(2):
            index = start + slot
            if index >= len(reader.pages):
                continue
            page.merge_transformed_page(reader.pages[index], Transformation().translate(tx=slot * a5w, ty=0), over=True)
        page.merge_page(overlay)
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": "Pralaya Chinese Rule Summary - A5 Booklet 2-up",
            "/Author": "Codex",
            "/Subject": "2018 Revised Edition Chinese rule summary for single-sided A4 printing",
        }
    )
    with SUMMARY_OUT.open("wb") as stream:
        writer.write(stream)


def faq_entry(st, q, answer):
    return [rich(f"<b>{escape(q)}</b>", st), P(answer, st), Spacer(1, 3)]


FAQ_JA = [
    ("Q1. 行動力は使い切らなくてもよい？", "はい。ただし、その手番に遺物カードを少なくとも1枚獲得します。残った行動力は次の手番へ持ち越せません。"),
    ("Q2. 聖典購入後、残った行動力で遺物を追加取得できる？", "リバイズド版ではこの状況は発生しません。先に遺物を取り、その後で聖典またはドーニーを購入する順序です。旧版FAQの前提を使わないでください。"),
    ("Q3. 聖典とドーニーを同じ手番に購入できる？", "できません。購入できるのはどちらか一方で、同じ種類は1人1枚までです。"),
    ("Q4. 価格Xのドーニーはどう購入する？", "手札の銅貨・銀貨・金貨をすべて捨てます。貨幣を持っていなければ無料です。Xを数値として支払うのではありません。"),
    ("Q5. ドーニー購入後はどうなる？", "購入した瞬間に脱出します。その後も手番は続き、遺物を取る代わりに島の遺物1枚を捨て、山札から1枚補充します。"),
    ("Q6. ドーニーは価格以上の貨幣を支払える？", "はい。お釣りはありません。価格XだけはQ4の特別処理です。"),
    ("Q7. 悪魔の契約の得点は？", "悪魔の像の合計得点への倍率です。1枚=-3倍、2枚=+9倍、3枚=-27倍、4枚=+81倍です。"),
    ("Q8. プンディットが数えるカード種類とは？", "異なるカード名の種類数です。聖典、ドーニー、プンディットも種類に含みます。同名カードの複数枚は1種類です。"),
    ("Q9. 化石の最多判定でドーニーがないプレイヤーは？", "化石0枚として扱います。最多が同数なら、化石の15点は誰も得ません。"),
    ("Q10. 脱出していないプレイヤーは得点できる？", "できません。得点計算をせず、自動的に最下位です。脱出済みなら負の得点でも未脱出より上位です。"),
    ("Q11. 島の遺物がなくなったら即終了？", "即終了とは限りません。全員脱出、補充後に島が全て海、または開始時に非海洋遺物が1枚だけで購入手順を終えた場合に終了します。"),
    ("Q12. 脱出後も手番を続ける理由は？", "遺物を取る代わりに島の遺物を1枚捨てて補充し、島を沈める進行に関与するためです。"),
]

FAQ_EN = [
    ("Q1. Do I have to spend all my Vitality?", "No. You may leave Vitality unused, but you must collect at least one Relic card on your turn. Unused Vitality does not carry over."),
    ("Q2. Can I collect more Relics after buying Veda?", "This situation does not occur in the Revised Edition. You collect Relics first, then purchase Veda or Dhoni. Do not use the old FAQ to change the Revised turn order."),
    ("Q3. Can I buy both Veda and Dhoni on the same turn?", "No. You may buy one or the other, and each player may buy no more than one of each type."),
    ("Q4. How do I buy the price X Dhoni?", "Discard all Copper Coins, Silver Coins, and Gold Coins in your hand. If you have no currency, you may buy it for free. X is not a numeric price."),
    ("Q5. What happens after buying a Dhoni?", "You immediately escape. You still take turns, but instead of collecting a Relic, discard one Relic from the island and refill it from the deck."),
    ("Q6. May I pay more than a numeric Dhoni price?", "Yes. There is no change. The price X Dhoni uses the special all-currency rule in Q4."),
    ("Q7. How does Demonic Pact score?", "It multiplies the total score of your Demon Statues: one Pact = -3x, two = +9x, three = -27x, and four = +81x."),
    ("Q8. Which card types does Pundit count?", "The number of different card types you have. Veda, Dhoni, and Pundit itself count as types; duplicates of one type count once."),
    ("Q9. How does Fossil majority treat a player without Dhoni?", "That player is treated as having zero Fossils. If the highest Fossil count is tied, nobody scores the 15 Fossil points."),
    ("Q10. Do players who have not escaped score?", "No. They do not score and automatically rank last. An escaped player ranks above an unescaped player even with a negative score."),
    ("Q11. Does the game end as soon as no Relic can be collected?", "Not necessarily. It ends when everyone escapes, the island is all Ocean after refilling, or only one non-Ocean Relic remains at the start of a turn and that turn completes the purchase step."),
    ("Q12. Why does an escaped player continue taking turns?", "The player discards one island Relic and refills instead of collecting, so the player still advances the island's sinking process."),
]

FAQ_ZH = [
    ("Q1. 行动点必须全部用完吗？", "不必。但该回合必须至少收集1张遗迹牌。未使用的行动点不能保留到下回合。"),
    ("Q2. 购买圣典后还能用剩余行动点收集遗迹吗？", "修订版中不会出现这个情境。修订版先收集遗迹，再购买圣典或救生船。不要用旧版FAQ改变修订版的回合顺序。"),
    ("Q3. 同一回合能同时购买圣典和救生船吗？", "不能。只能购买其中一种；每位玩家每种牌最多1张。"),
    ("Q4. 价格为X的救生船怎么购买？", "将手牌中的铜币、银币和金币全部弃置。没有货币时可以免费购买。X不是需要支付的数值。"),
    ("Q5. 购买救生船后会怎样？", "购买瞬间立即逃离。之后仍继续回合，但不再收集遗迹；改为弃置岛上1张遗迹，并从牌库补充1张。"),
    ("Q6. 可以支付超过数值救生船价格的货币吗？", "可以，但不找零。价格X的救生船按照Q4的特殊规则处理。"),
    ("Q7. 恶魔契约如何计分？", "作用于恶魔雕像的合计分数：1张为-3倍，2张为+9倍，3张为-27倍，4张为+81倍。"),
    ("Q8. 贤者计算哪些卡牌种类？", "计算你拥有的不同卡牌种类数。圣典、救生船和贤者本身也计入；同名牌多张仍只算1种。"),
    ("Q9. 化石最多判定中，没有救生船的玩家如何处理？", "视为拥有0张化石。最多数量平分时，没有玩家获得化石的15分。"),
    ("Q10. 没有逃离的玩家可以计分吗？", "不能。不进行计分，自动排在最后。逃离玩家即使得分为负，也排在未逃离玩家之前。"),
    ("Q11. 岛上没有可收集的遗迹时会立即结束吗？", "不一定。所有玩家逃离、补充后岛上全是海洋，或回合开始时只有1张非海洋遗迹并完成购买步骤时才结束。"),
    ("Q12. 逃离后的玩家为什么还要继续回合？", "逃离玩家以弃置岛上1张遗迹并补充1张代替收集，因此仍会推进岛屿沉没。"),
]


def build_faq():
    doc = SimpleDocTemplate(
        str(FAQ_OUT),
        pagesize=A4,
        leftMargin=19 * mm,
        rightMargin=19 * mm,
        topMargin=17 * mm,
        bottomMargin=19 * mm,
        title="Pralaya Revised Edition Trilingual FAQ",
        author="Codex",
    )
    story = [
        P("Pralaya Revised Edition｜三言語FAQ", JA_H1),
        P("日本語FAQ", JA_H2),
        section_rule(),
        P("2018 Revised Edition。本文だけでFAQを確認できるよう、Web参照なしで読める形に整理しています。", JA_BODY),
        P("適用順：リバイズド版ルールブック → 適用可能な公式FAQ → BGGコミュニティの議論。BGG投稿は公式裁定とは限らないため、ルールブックと異なる場合はルールブックを優先します。", JA_SMALL),
        P("印刷構成：日本語 → English → 简体中文（各言語は別ページ）", JA_SMALL),
    ]

    story += [P("リバイズド版で実際に発生する疑問を中心に整理しています。Q2は旧版FAQの前提を誤用しないための除外説明です。", JA_BODY)]
    for q, a in FAQ_JA:
        story += faq_entry(JA_BODY, q, a)

    story += [PageBreak(), P("English FAQ", EN_H1), section_rule(), P("This section is based on the Revised Edition turn order and card effects. Q2 records why an old-edition question is not applied here.", EN_BODY)]
    for q, a in FAQ_EN:
        story += faq_entry(EN_BODY, q, a)

    story += [PageBreak(), P("简体中文FAQ", CN_H1), section_rule(), P("本部分以2018年修订版为准；《王国沉没》仅用于术语参考。Q2说明了旧版问题为何不适用于修订版。", CN_BODY)]
    for q, a in FAQ_ZH:
        story += faq_entry(CN_BODY, q, a)

    doc.build(story, onFirstPage=lambda c, d: footer(c, d, "2018 Revised Edition | Trilingual FAQ"), onLaterPages=lambda c, d: footer(c, d, "2018 Revised Edition | Trilingual FAQ"))


def b5_faq_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(doc.leftMargin, 11 * mm, doc.pagesize[0] - doc.rightMargin, 11 * mm)
    canvas.setFont("CJK", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 6 * mm, "2018 Revised Edition | Trilingual FAQ")
    canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 6 * mm, f"Page {canvas.getPageNumber()}")
    canvas.restoreState()


def build_faq_b5():
    """Build a B5 direct-print FAQ."""
    doc = SimpleDocTemplate(
        str(FAQ_B5_OUT),
        pagesize=B5,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=17 * mm,
        title="Pralaya Revised Edition Trilingual FAQ - B5 direct print",
        author="Codex",
    )
    term_data = [
        ["日本語", "English", "简体中文"],
        ["遺物カード", "Relic card", "遗迹牌"],
        ["行動力", "Vitality", "行动点"],
        ["聖典", "Veda", "圣典"],
        ["ドーニー", "Dhoni", "救生船"],
        ["海", "Ocean", "海洋"],
    ]
    source_rows = [
        ["資料", "用途"],
        ["Pralaya Revised Edition rulebook", "修订版规则书；规则冲突时优先"],
        ["Domina Games: Pralaya Official FAQ", "官方FAQ；用于确认修订版适用问题与旧版问题的排除"],
        ["BGG Pralaya Rules forum", "社区问题与讨论；不是官方裁定"],
        ["BGG: Boats work differently in first and later editions?", "救生船购买、立即逃离、逃离后的处理"],
        ["BGG: Demonic Pact scoring", "恶魔契约倍率与符号变化"],
    ]
    source_links = [
        '<link href="https://www.dominagames.com/qa3/">https://www.dominagames.com/qa3/</link>',
        '<link href="https://boardgamegeek.com/boardgame/187590/pralaya/forums/66">https://boardgamegeek.com/boardgame/187590/pralaya/forums/66</link>',
        '<link href="https://boardgamegeek.com/thread/3548807/boats-work-differently-in-first-and-later-editions">https://boardgamegeek.com/thread/3548807/boats-work-differently-in-first-and-later-editions</link>',
        '<link href="https://boardgamegeek.com/thread/2457856/demonic-pact-scoring">https://boardgamegeek.com/thread/2457856/demonic-pact-scoring</link>',
    ]

    story = [
        Spacer(1, 22 * mm),
        P("Pralaya Revised Edition", CN_COVER),
        P("三言語FAQ", CN_COVER_SUB),
        Spacer(1, 8 * mm),
        P("2018 Revised Edition", CN_H2),
        section_rule(),
        P("日本語 / English / 简体中文", JA_BODY),
        P("Rule priority: Revised Edition rulebook first, applicable official FAQ second, BGG community discussion third.", B5_EN_SMALL),
        P("规则优先级：修订版规则书优先，其次是适用于修订版的官方FAQ，最后是BGG社区讨论。", CN_SMALL),
        Spacer(1, 8 * mm),
        PageBreak(),
        P("日本語FAQ｜Q1〜Q6", JA_H1), section_rule(),
    ]
    for q, a in FAQ_JA[:6]:
        story += faq_entry(JA_BODY, q, a)
    story += [PageBreak(), P("日本語FAQ｜Q7〜Q12", JA_H1), section_rule()]
    for q, a in FAQ_JA[6:]:
        story += faq_entry(JA_BODY, q, a)

    story += [PageBreak(), P("English FAQ | Q1-Q6", B5_EN_H1), section_rule()]
    for q, a in FAQ_EN[:6]:
        story += faq_entry(B5_EN_BODY, q, a)
    story += [PageBreak(), P("English FAQ | Q7-Q12", B5_EN_H1), section_rule()]
    for q, a in FAQ_EN[6:]:
        story += faq_entry(B5_EN_BODY, q, a)

    story += [PageBreak(), P("简体中文FAQ｜Q1-Q6", CN_H1), section_rule()]
    for q, a in FAQ_ZH[:6]:
        story += faq_entry(CN_BODY, q, a)
    story += [PageBreak(), P("简体中文FAQ｜Q7-Q12", CN_H1), section_rule()]
    for q, a in FAQ_ZH[6:]:
        story += faq_entry(CN_BODY, q, a)

    story += [
        PageBreak(),
        P("参照资料 / Sources", CN_H1),
        section_rule(),
        table(source_rows, [125, 270], font_style=CN_TABLE, head_style=CN_TABLE_HEAD, padding=2.3),
        Spacer(1, 5 * mm),
        P("Web sources", B5_EN_H2),
    ]
    story += [rich(link, B5_EN_SMALL) for link in source_links]

    doc.build(story, onFirstPage=b5_faq_footer, onLaterPages=b5_faq_footer)


def fold_rule():
    return HRFlowable(width="100%", thickness=0.45, color=LINE, spaceBefore=1, spaceAfter=4)


def fold_panel_footer(panel_no):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.3)
        canvas.line(doc.leftMargin, 6 * mm, doc.pagesize[0] - doc.rightMargin, 6 * mm)
        canvas.setFont("CJK", 5.15)
        canvas.setFillColor(MUTED)
        canvas.drawString(doc.leftMargin, 3.0 * mm, "2018 Revised Edition")
        canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 3.0 * mm, f"Panel {panel_no}/12")
        canvas.restoreState()

    return draw


def build_fold_panel(panel_no, story, prefix):
    FOLD_PANEL_DIR.mkdir(parents=True, exist_ok=True)
    panel_path = FOLD_PANEL_DIR / f"{prefix}-{panel_no:02d}.pdf"
    doc = SimpleDocTemplate(
        str(panel_path),
        pagesize=FOLD_PANEL_PAGE,
        leftMargin=5 * mm,
        rightMargin=5 * mm,
        topMargin=5 * mm,
        bottomMargin=9 * mm,
        title=f"Pralaya Revised Edition - fold panel {panel_no}",
        author="Codex",
    )
    doc.build(story, onFirstPage=fold_panel_footer(panel_no), onLaterPages=fold_panel_footer(panel_no))
    reader = PdfReader(str(panel_path))
    if len(reader.pages) != 1:
        raise ValueError(f"Fold panel {panel_no} overflowed into {len(reader.pages)} pages")
    return panel_path


def impose_fold_panels(panel_paths, output_path, title):
    if len(panel_paths) != 12:
        raise ValueError(f"Expected 12 fold panels, got {len(panel_paths)}")
    panel_pages = [PdfReader(str(path)).pages[0] for path in panel_paths]
    a4_landscape = landscape(A4)
    a4w, a4h = a4_landscape
    panel_w, panel_h = FOLD_PANEL_PAGE
    overlay_path = TMP_DIR / f"{output_path.stem}-fold-overlay.pdf"
    overlay_canvas = Canvas(str(overlay_path), pagesize=a4_landscape)
    overlay_canvas.setStrokeColor(MUTED)
    overlay_canvas.setLineWidth(0.4)
    overlay_canvas.setDash(2, 2)
    overlay_canvas.line(panel_w, 0, panel_w, a4h)
    overlay_canvas.line(panel_w * 2, 0, panel_w * 2, a4h)
    overlay_canvas.line(0, panel_h, a4w, panel_h)
    overlay_canvas.setDash()
    overlay_canvas.setFillColor(MUTED)
    overlay_canvas.setFont("CJK", 5.4)
    overlay_canvas.drawCentredString(panel_w, a4h - 3.0 * mm, "FOLD / 折り線")
    overlay_canvas.drawCentredString(panel_w * 2, a4h - 3.0 * mm, "FOLD / 折り線")
    overlay_canvas.drawCentredString(a4w - 10 * mm, panel_h, "FOLD / 折り線")
    overlay_canvas.save()
    overlay = PdfReader(str(overlay_path)).pages[0]

    writer = PdfWriter()
    for sheet in range(2):
        page = PageObject.create_blank_page(width=a4w, height=a4h)
        for slot in range(6):
            panel_index = sheet * 6 + slot
            col = slot % 3
            row = slot // 3
            y = panel_h if row == 0 else 0
            page.merge_transformed_page(
                panel_pages[panel_index],
                Transformation().translate(tx=col * panel_w, ty=y),
                over=True,
            )
        page.merge_page(overlay)
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": title,
            "/Author": "Codex",
            "/Subject": "2018 Revised Edition A4 duplex, six-panel fold-only insert",
        }
    )
    with output_path.open("wb") as stream:
        writer.write(stream)


def build_summary_fold_panels():
    table_kwargs = {"font_style": FOLD_TABLE, "head_style": FOLD_TABLE_HEAD, "padding": 1.8}
    term_data = [
        ["日本語", "English", "简体中文"],
        ["遺物カード", "Relic card", "遗迹牌"],
        ["行動力", "Vitality", "行动点"],
        ["聖典", "Veda", "圣典"],
        ["ドーニー", "Dhoni", "救生船"],
        ["海", "Ocean", "海洋"],
    ]
    stories = [
        [
            Spacer(1, 4 * mm),
            P("《王国沉没》", FOLD_COVER),
            P("Pralaya Revised Edition", FOLD_COVER_SUB),
            P("简体中文规则摘要", FOLD_COVER_SUB),
            fold_rule(),
            P("游戏目标", FOLD_H2),
            P("在岛屿沉入海底之前收集遗迹并逃离。带着最多遗迹逃离的玩家获胜。", FOLD_BODY),
            P("折叠方法 / FOLD", FOLD_H2),
            P("A4横向双面打印。沿横中央线二つ折り，再沿两条竖线蛇腹折叠；无需裁切，完成约99×105mm。", FOLD_BODY),
            P("本摘要只对应2018 Revised Edition（修订版）。规则冲突时，以修订版规则书为准。", FOLD_SMALL),
        ],
        [
            P("1. 内容物与基本术语", FOLD_H1), fold_rule(),
            P("内容物", FOLD_H2),
            P("遗迹牌95张（包括海洋牌）；圣典牌和救生船牌各按玩家人数使用同样数量。", FOLD_BODY),
            P("三语术语表", FOLD_H2),
            table(term_data, [52, 62, 130], **table_kwargs),
            P("遗迹牌包含名称、行动点、牌张数量、货币价值和效果／得分文字。只有铜币、银币、金币具有货币价值。圣典和救生船是购买牌，不是遗迹牌；海洋牌不能收集。", FOLD_BODY),
        ],
        [
            P("2. 游戏准备", FOLD_H1), fold_rule(),
            *bullets([
                "洗匀所有遗迹牌，背面朝上组成遗迹牌库。",
                "取出与玩家人数相同数量的圣典和救生船。救生船按价格X在最上、其余从低到高叠放。",
                "2～3人：抽15张摆成3×5；4～5人：抽18张摆成3×6，全部面朝上。",
                "共同决定首位玩家；之后依次由左手边玩家进行回合。",
            ], FOLD_BODY),
            P("救生船价格配置", FOLD_H2),
            table([["人数", "本局价格"], ["2人", "X、7"], ["3人", "X、7、4"], ["4人", "X、7、4、2"], ["5人", "X、7、4、2、10"]], [50, 194], **table_kwargs),
            P("无人数标记的牌始终使用；有标记的牌按人数加入。Veda和Dhoni各使用与玩家人数相同数量。", FOLD_SMALL),
        ],
        [
            P("3. 回合流程", FOLD_H1), fold_rule(),
            table([
                ["步骤", "处理"],
                ["1", "回合开始通常3点行动；第一轮首位1点、第二位2点。持有圣典且未逃离时为4点。"],
                ["2", "消耗行动点，至少收集1张面朝上的遗迹牌。行动点可剩余，但不能带到下回合。"],
                ["3", "完成收集后，最多购买圣典或救生船其中一种；同回合不能两种都买。"],
                ["4", "从遗迹牌库面朝上补足空位。"],
                ["5", "补充完成后回合结束，由左手边玩家继续。"],
            ], [21, 223], **table_kwargs),
            P("重点：每回合必须至少收集1张遗迹牌；购买永远发生在收集之后。", FOLD_SMALL),
        ],
        [
            P("4. 圣典、救生船与购买", FOLD_H1), fold_rule(),
            table([
                ["牌", "购买与效果"],
                ["圣典（Veda）", "用铜币、银币、金币支付达到牌上价格的总价值。购买后，在逃离前每回合开始拥有4点行动；每人最多1张。"],
                ["救生船（Dhoni）", "数值价格：支付总价值达到价格，超过不找零。购买后立即逃离；每人最多1张。"],
                ["价格X救生船", "弃置手牌中的所有铜币、银币、金币；没有货币时可免费购买。X不是数值价格。"],
            ], [50, 194], **table_kwargs),
            P("购买限制", FOLD_H2),
            *bullets(["同一回合不能同时购买圣典和救生船。", "每位玩家每种购买牌最多1张。", "数值价格支付超过时不找零。"], FOLD_BODY),
        ],
        [
            P("5. 脱出后的处理", FOLD_H1), fold_rule(),
            P("购买救生船后立即从岛上逃离。", FOLD_H2),
            P("你仍继续自己的回合，但不再收集遗迹牌；改为选择岛上的1张遗迹牌弃置，再从牌库补充1张。", FOLD_BODY),
            P("回合顺序", FOLD_H2),
            *bullets(["① 至少收集1张遗迹牌。", "② 收集后最多购买一种牌。", "③ 若购买救生船，立即脱出。", "④ 之后每回合弃置岛上1张遗迹并补充。"], FOLD_BODY),
            P("救生船持有者仍会推进岛屿沉没，因此不能跳过自己的回合。", FOLD_SMALL),
        ],
        [
            P("6. 游戏结束与计分", FOLD_H1), fold_rule(),
            P("满足任一条件时结束", FOLD_H2),
            *bullets(["所有玩家都已从岛上逃离。", "补充后岛上全是海洋牌。", "回合开始时只有1张非海洋牌，并完成该回合的购买步骤。"], FOLD_BODY),
            P("计分", FOLD_H2),
            *bullets(["未逃离（面前没有救生船）的玩家不计分，自动排在所有逃离玩家之后。", "逃离玩家计算自己所有遗迹牌的得分。", "逃离玩家即使得分为负，也排在未逃离玩家之前。", "平分时，按回合顺序距离首位玩家最远者获胜。"], FOLD_BODY),
        ],
        [
            P("7. 卡牌效果一览（1）", FOLD_H1), fold_rule(),
            table([
                ["卡牌", "收集", "得分／效果"],
                ["铜币", "1", "每张1分；逃离前货币值1。"],
                ["银币", "2", "每张3分；逃离前货币值3。"],
                ["金币", "3", "每张6分；逃离前货币值6。"],
                ["恶魔雕像", "1", "每张2分；受恶魔契约倍率影响。"],
                ["古代手稿", "1", "每2张5分；不足2张不得分。"],
                ["文物碎片", "2", "每3张20分；不足3张不得分。"],
                ["伟大雕像", "1", "得分为持有数量的平方。"],
            ], [54, 35, 155], **table_kwargs),
        ],
        [
            P("8. 卡牌效果一览（2）", FOLD_H1), fold_rule(),
            table([
                ["卡牌", "收集／价", "得分／效果"],
                ["恶魔契约", "2", "恶魔雕像得分乘(-3)^n；n=1/2/3/4时为-3/+9/-27/+81倍。"],
                ["贤者", "2", "不同卡牌种类数；含圣典、救生船、贤者。"],
                ["祭司", "3", "恶魔雕像0分；持有圣典时圣典15分。"],
                ["化石", "1", "化石最多者15分；平分无人得分；无救生船者按0张。"],
                ["海洋", "不可收集", "无效果。"],
                ["圣典", "购买", "逃离前每回合开始4点行动。"],
                ["救生船", "购买", "立即逃离；之后弃置岛上1张遗迹代替收集。"],
            ], [54, 42, 148], **table_kwargs),
            P("恶魔契约倍率：1=-3×、2=+9×、3=-27×、4=+81×。", FOLD_SMALL),
        ],
        [
            P("9. 一回合速查", FOLD_H1), fold_rule(),
            *bullets(["① 回合开始获得行动点：通常3；圣典持有者4；第一轮首位1、第二位2。", "② 至少拿1张面朝上的遗迹牌；行动点可剩余但不保留。", "③ 收集后，最多买圣典或救生船其中一种。", "④ 普通玩家补空位；救生船持有者弃置岛上1张遗迹并补1张。", "⑤ 直到满足结束条件。"], FOLD_BODY),
            P("三项最终检查", FOLD_H2),
            *bullets(["只有逃离玩家计分。", "价格X救生船：弃置所有货币；无货币时免费。", "规则冲突时以修订版规则书为准。"], FOLD_BODY),
        ],
        [
            P("10. 三语术语表", FOLD_H1), fold_rule(),
            table(term_data, [52, 62, 130], **table_kwargs),
            P("版本说明", FOLD_H2),
            P("中文商品资料《王国沉没》仅用于术语参考。本摘要的规则、顺序、救生船处理和计分均以2018 Revised Edition为准。", FOLD_BODY),
            P("本页可单独作为游戏中快速查阅页使用。", FOLD_SMALL),
        ],
        [
            Spacer(1, 12 * mm),
            P("《王国沉没》", FOLD_COVER),
            P("Pralaya Revised Edition", FOLD_COVER_SUB),
            fold_rule(),
            P("2018 Revised Edition", FOLD_H2),
            P("简体中文规则摘要", FOLD_COVER_SUB),
            Spacer(1, 6 * mm),
            P("切らずに折る / 不裁切折叠", FOLD_COVER_SUB),
            P("A4双面打印后，折叠成约99×105mm，放入盒内保存。", FOLD_SMALL),
        ],
    ]
    panel_paths = [build_fold_panel(i + 1, story, "summary") for i, story in enumerate(stories)]
    impose_fold_panels(panel_paths, SUMMARY_FOLD_OUT, "Pralaya Chinese Rule Summary - A4 6-panel duplex fold-only")


def fold_faq_entry(st, q, answer):
    return [rich(f"<b>{escape(q)}</b>", st), P(answer, st), Spacer(1, 1.4)]


def build_faq_fold_panels():
    source_rows = [
        ["资料", "用途"],
        ["Pralaya Revised Edition rulebook", "修订版规则书；规则冲突时优先"],
        ["Domina Games: Pralaya Official FAQ", "官方FAQ中的行动点问题，以及旧版顺序问题的排除依据"],
        ["BGG Rules forum", "社区问题列表；不是官方裁定"],
        ["BGG: Boats work differently in first and later editions?", "修订版救生船购买、立即逃离、逃离后弃置遗迹"],
        ["BGG: Demonic Pact scoring", "恶魔契约倍率与符号变化"],
    ]
    source_links = [
        '<link href="https://www.dominagames.com/qa3/">Domina Games: Pralaya FAQ</link>',
        '<link href="https://boardgamegeek.com/boardgame/187590/pralaya/forums/66">BoardGameGeek: Pralaya Rules forum</link>',
        '<link href="https://boardgamegeek.com/thread/3548807/boats-work-differently-in-first-and-later-editions">BGG: Boats work differently in first and later editions?</link>',
        '<link href="https://boardgamegeek.com/thread/2457856/demonic-pact-scoring">BGG: Demonic Pact scoring</link>',
    ]
    term_data = [
        ["日本語", "English", "简体中文"],
        ["遺物カード", "Relic card", "遗迹牌"],
        ["行動力", "Vitality", "行动点"],
        ["聖典", "Veda", "圣典"],
        ["ドーニー", "Dhoni", "救生船"],
        ["海", "Ocean", "海洋"],
    ]
    faq_table_kwargs_ja = {"font_style": FOLD_TABLE, "head_style": FOLD_TABLE_HEAD, "padding": 1.4}
    faq_table_kwargs_en = {"font_style": FOLD_EN_TABLE, "head_style": FOLD_EN_TABLE_HEAD, "padding": 1.4}
    stories = [
        [
            Spacer(1, 4 * mm),
            P("Pralaya Revised Edition", FOLD_COVER),
            P("三言語FAQ", FOLD_COVER_SUB),
            fold_rule(),
            P("2018 Revised Edition。必要な結論を本文に収録しているため、Web接続なしで確認できます。", FOLD_BODY),
            P("Rule priority: Revised Edition rulebook first, applicable official FAQ second, BGG community discussion third.", FOLD_EN_SMALL),
            P("规则优先级：修订版规则书优先，其次是适用于修订版的官方FAQ，最后是BGG社区讨论。", FOLD_SMALL),
            P("折り方 / FOLD：A4横・両面・100%。横中央で二つ折り、縦2本を蛇腹に折る。切らずに約99×105mm。", FOLD_BODY),
        ],
        [P("日本語FAQ｜Q1〜Q6", FOLD_H1), fold_rule()] + sum((fold_faq_entry(FOLD_BODY, q, a) for q, a in FAQ_JA[:6]), []),
        [P("日本語FAQ｜Q7〜Q12", FOLD_H1), fold_rule()] + sum((fold_faq_entry(FOLD_BODY, q, a) for q, a in FAQ_JA[6:]), []),
        [P("English FAQ | Q1-Q6", FOLD_EN_H1), fold_rule()] + sum((fold_faq_entry(FOLD_EN_BODY, q, a) for q, a in FAQ_EN[:6]), []),
        [P("English FAQ | Q7-Q12", FOLD_EN_H1), fold_rule()] + sum((fold_faq_entry(FOLD_EN_BODY, q, a) for q, a in FAQ_EN[6:]), []),
        [P("简体中文FAQ｜Q1-Q6", FOLD_H1), fold_rule()] + sum((fold_faq_entry(FOLD_BODY, q, a) for q, a in FAQ_ZH[:6]), []),
        [P("简体中文FAQ｜Q7-Q12", FOLD_H1), fold_rule()] + sum((fold_faq_entry(FOLD_BODY, q, a) for q, a in FAQ_ZH[6:]), []),
        [
            P("参照资料 / Sources", FOLD_H1), fold_rule(),
            P("本FAQ已将必要的结论写入正文，游戏时不需要连接外部网站。以下链接仅用于出处追踪。", FOLD_BODY),
            table(source_rows, [110, 134], font_style=FOLD_TABLE, head_style=FOLD_TABLE_HEAD, padding=1.1),
            P("Web sources", FOLD_H2),
            *[rich(link, FOLD_EN_SMALL) for link in source_links],
        ],
        [
            P("オフライン用重要ルール", FOLD_H1), fold_rule(),
            *bullets(["行動力は使い切らなくてもよいが、遺物カードを1枚以上取る。", "購入は遺物収集の後。聖典とドーニーは同じ手番に買えない。", "価格Xのドーニーは貨幣をすべて捨て、貨幣0なら無料。", "ドーニー購入後は即脱出し、以後は島の遺物を1枚捨てて補充する。", "未脱出プレイヤーは得点せず最下位。"], FOLD_BODY),
            P("简体中文", FOLD_H2),
            P("每回合至少收集1张遗迹牌；购买救生船后立即逃离；未逃离玩家不计分。", FOLD_BODY),
        ],
        [
            P("三言語用語表", FOLD_H1), fold_rule(),
            table(term_data, [52, 62, 130], font_style=FOLD_TABLE, head_style=FOLD_TABLE_HEAD, padding=1.4),
            P("Pralaya / 王国沉没", FOLD_H2),
            P("Relic＝遺物カード＝遗迹牌、Vitality＝行動力＝行动点、Veda＝聖典＝圣典、Dhoni＝ドーニー＝救生船、Ocean＝海＝海洋。", FOLD_BODY),
        ],
        [
            P("Revised Editionと旧版FAQ", FOLD_H1), fold_rule(),
            P("日本語", FOLD_H2),
            P("Q2の「聖典購入後に残りの行動力で遺物を取る」という状況は、リバイズド版の順序では発生しません。先に遺物を取り、その後で購入します。", FOLD_BODY),
            P("English", FOLD_H2),
            P("The old-edition timing question in Q2 is not applied: the Revised Edition collects Relics first and purchases afterward.", FOLD_EN_BODY),
            P("简体中文", FOLD_H2),
            P("Q2所述的旧版情境不适用于修订版。修订版先收集遗迹，再进行购买。", FOLD_BODY),
        ],
        [
            Spacer(1, 12 * mm),
            P("Pralaya Revised Edition", FOLD_COVER),
            P("三言語FAQ", FOLD_COVER_SUB),
            fold_rule(),
            P("2018 Revised Edition", FOLD_H2),
            P("切らずに折る / 不裁切折叠", FOLD_COVER_SUB),
            P("表紙・FAQ・Sourcesを1枚のA4両面に収録。", FOLD_SMALL),
        ],
    ]
    panel_paths = [build_fold_panel(i + 1, story, "faq") for i, story in enumerate(stories)]
    impose_fold_panels(panel_paths, FAQ_FOLD_OUT, "Pralaya Trilingual FAQ - A4 6-panel duplex fold-only")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_summary_a5()
    impose_summary_2up()
    build_summary_b5()
    build_summary_b7()
    impose_summary_b7_4up()
    build_faq()
    build_faq_b5()
    build_summary_fold_panels()
    build_faq_fold_panels()
    print(SUMMARY_OUT)
    print(SUMMARY_B5_OUT)
    print(SUMMARY_B7_OUT)
    print(FAQ_OUT)
    print(FAQ_B5_OUT)
    print(SUMMARY_FOLD_OUT)
    print(FAQ_FOLD_OUT)


if __name__ == "__main__":
    main()
