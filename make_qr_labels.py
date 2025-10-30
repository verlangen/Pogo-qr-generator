import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os

INPUT_FILE = "codes.txt"
OUTPUT_FILE = "qrcodes.pdf"
TEMP_DIR = "qr_temp"
GROUP_NAME_TEXT = ""

os.makedirs(TEMP_DIR, exist_ok=True)

def read_codes(filename):
    codes = []
    with open(filename, "r") as f:
        for line in f:
            for code in line.split():
                codes.append(code)
    return codes

def make_qr(code, outpath, qr_size=1.0*inch):
    url = f"https://store.pokemongo.com/offer-redemption?passcode={code}"
    img = qrcode.make(url)
    img = img.resize((int(qr_size), int(qr_size)))  # shrink
    img.save(outpath)

def build_pdf(codes, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter, leftMargin=0.25*inch, rightMargin=0.25*inch, topMargin=0.25*inch, bottomMargin=0.25*inch)
    styles = getSampleStyleSheet()
    elements = []

    #2 row x 5 columns / sheet
    #adjust here to make more or less/sheet
    cols = 2               
    rows_per_page = 5

    qr_size = 1.0 * inch   
    col_width = 3.5 * inch 
    row_height = 2 * inch 

    table_data = []
    row = []

    for i, code in enumerate(codes, 1):
        qr_path = os.path.join(TEMP_DIR, f"{code}.png")
        make_qr(code, qr_path, qr_size=qr_size)


        title = Paragraph(
            f'<para align="center"><b>{GROUP_NAME_TEXT}</b></para>',
            styles["Heading5"]
        )
        qr_img = Image(qr_path, width=qr_size, height=qr_size)
        code_text = Paragraph(
            f'<para align="center">{code}</para>',
            styles["Normal"]
        )

        card = [[title], [qr_img], [code_text]]

        cell = Table(card, colWidths=[col_width])
        cell.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("BOX", (0, 0), (-1, -1), 0.25, "black"),
        ]))

        row.append(cell)

        if i % cols == 0:
            table_data.append(row)
            row = []

    if row:
        table_data.append(row)
    if table_data:
        table = Table(table_data, colWidths=[col_width]*cols, rowHeights=row_height)
        table.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ]))

        elements.append(table)
    doc.build(elements)

if __name__ == "__main__":
    codes = read_codes(INPUT_FILE)
    build_pdf(codes, OUTPUT_FILE)
    print(f"PDF saved as {OUTPUT_FILE}")

