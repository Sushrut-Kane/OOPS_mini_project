import streamlit as st
from inventory import items

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state["page"] = "selection"

# Function to navigate to a different page
def navigate_to(page_name):
    st.session_state["page"] = page_name

# Selection Page
if st.session_state["page"] == "selection":
    # Page Title
    st.markdown("""
        <div style="padding: 20px;">
            <h1 style="text-align: center;">ELEGANTE CAFE</h1>
        </div>
        """, unsafe_allow_html=True)

    # Page Subtitle
    st.markdown("""
        <div style="padding: 20px;">
            <h3 style="text-align: center;">Please order as you please!</h3>
        </div>
        """, unsafe_allow_html=True)

    # Quantity Selection Section
    st.write("### Select Quantity for Each Item")
    selected_quantities = {}

    for item_name in items.keys():
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
        # Store selected quantities in session_state
        st.session_state["selected_quantities"] = selected_quantities
        # Navigate to the order page
        navigate_to("order")

# Order Page
elif st.session_state["page"] == "order":
    st.markdown("""
        <div style="padding: 20px;">
            <h1 style="text-align: center;">Order Summary</h1>
        </div>
        """, unsafe_allow_html=True)

    # Retrieve selected quantities from session_state
    selected_quantities = st.session_state.get("selected_quantities", {})
    order_summary = {item: qty for item, qty in selected_quantities.items() if qty > 0}

    if order_summary:
        for item, qty in order_summary.items():
            st.write(f"{item}: {qty}")
    else:
        st.write("No items selected. Please go back and add items to your order.")

    # Back button to go to selection page
    if st.button("Back to Selection"):
        navigate_to("selection")
