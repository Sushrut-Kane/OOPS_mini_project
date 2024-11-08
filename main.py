import streamlit as st
from inventory import items
from price import calculate_total_price
from reciept import generate_pdf_receipt  # Import the receipt function

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state["page"] = "selection"

# Function to navigate to a different page
def navigate_to(page_name):
    st.session_state["page"] = page_name

# Selection Page
if st.session_state["page"] == "selection":
    # Page Title and Subtitle
    st.markdown("""
    <style>
    .custom-title {
        font-family: 'Courier New', Courier, monospace; /* Change this to any font you like */
        color: #ff5733; /* Change this color to any HEX or RGB value */
        font-size: 36px;
    }
    .custom-text {
        font-family: 'Verdana', sans-serif;
        color: #3498db; /* Blue color */
        font-size: 24px;
    }
    </style>
    <div class="custom-title">Welcome to Elegante Café</div>
    <div class="custom-text">Order your favorite items with ease!</div>
    """, unsafe_allow_html=True)

    # Quantity Selection Section
    st.write("### Select Quantity for Each Item")
    selected_quantities = {}

    for item_name, item_info in items.items():
        col1, col2 = st.columns([2, 1])
        col1.write(f"**{item_name}**")
        selected_quantities[item_name] = col2.slider(
            label=f"Select quantity for {item_name}",
            min_value=0,
            max_value=10,
            value=0,
            key=item_name
        )

    # Proceed Button
    if st.button("Proceed to Order"):
        st.session_state["selected_quantities"] = selected_quantities
        navigate_to("order")

# Order Page
elif st.session_state["page"] == "order":
    st.markdown("""
        <div style="padding: 20px;">
            <h1 style="text-align: center;">Order Summary</h1>
        </div>
        """, unsafe_allow_html=True)

    selected_quantities = st.session_state.get("selected_quantities", {})
    total_price, detailed_summary = calculate_total_price(items, selected_quantities)

    if detailed_summary:
        for item, qty, item_price, item_total in detailed_summary:
            st.write(f"{item}: {qty} x ${item_price:.2f} = ${item_total:.2f}")
        
        st.write("### Total Price: ${:.2f}".format(total_price))

        # Button to generate and download PDF receipt
        if st.button("Download PDF Receipt"):
            receipt_file = generate_pdf_receipt(items, selected_quantities, total_price)
            with open(receipt_file, "rb") as file:
                st.download_button(
                    label="Download Receipt",
                    data=file,
                    file_name="receipt.pdf",
                    mime="application/pdf"
                )
    else:
        st.write("No items selected. Please go back and add items to your order.")

    # Back button to return to the selection page
    if st.button("Back to Selection"):
        navigate_to("selection")
