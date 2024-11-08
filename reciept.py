from fpdf import FPDF
import datetime

def generate_pdf_receipt(items, selected_quantities, total_price):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="ELEGANTE CAFE RECEIPT", ln=True, align='C')

    # Date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Date: {current_date}", ln=True, align='C')

    pdf.ln(10)  # Add a line break

    # Table Header
    pdf.set_font("Arial", "B", 12)
    pdf.cell(80, 10, "Item", 1)
    pdf.cell(40, 10, "Quantity", 1)
    pdf.cell(40, 10, "Price ($)", 1)
    pdf.cell(30, 10, "Total ($)", 1)
    pdf.ln()

    # Table Body
    pdf.set_font("Arial", size=12)
    for item, qty in selected_quantities.items():
        if qty > 0:
            item_price = items[item]["price"]
            item_total = item_price * qty
            pdf.cell(80, 10, item, 1)
            pdf.cell(40, 10, str(qty), 1)
            pdf.cell(40, 10, f"{item_price:.2f}", 1)
            pdf.cell(30, 10, f"{item_total:.2f}", 1)
            pdf.ln()

    # Total Price
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, f"Total Price: ${total_price:.2f}", ln=True, align='R')

    # Save the PDF
    receipt_file = "receipt.pdf"
    pdf.output(receipt_file)

    return receipt_file
