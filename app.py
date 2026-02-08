import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# ----- Data Preparation -----
# Sample inventory data (mocked from provided screenshot)
initial_data = [
    {"Product ID": 101, "Product Name": "Laptop",      "Category": "Electronics",   "Supplier": "Supplier A", "Unit Price": 1200.50, "Quantity":  5, "Date Added": "2025-11-17"},
    {"Product ID": 102, "Product Name": "Monitor",     "Category": "Electronics",   "Supplier": "Supplier B", "Unit Price":  250.00, "Quantity": 12, "Date Added": "2025-11-17"},
    {"Product ID": 103, "Product Name": "Desk Chair",  "Category": "Furniture",     "Supplier": "Supplier C", "Unit Price":   85.00, "Quantity":  4, "Date Added": "2025-11-18"},
    {"Product ID": 104, "Product Name": "Desk Lamp",   "Category": "Office Supplies","Supplier": "Supplier A", "Unit Price":   15.99, "Quantity": 20, "Date Added": "2025-11-17"},
    {"Product ID": 105, "Product Name": "Printer",     "Category": "Electronics",   "Supplier": "Supplier D", "Unit Price":  300.00, "Quantity":  2, "Date Added": "2025-11-19"},
    {"Product ID": 106, "Product Name": "Notebook",    "Category": "Office Supplies","Supplier": "Supplier A", "Unit Price":    2.50, "Quantity": 50, "Date Added": "2025-11-18"},
    {"Product ID": 107, "Product Name": "Pen",         "Category": "Office Supplies","Supplier": "Supplier E", "Unit Price":    1.20, "Quantity":100, "Date Added": "2025-11-19"},
    {"Product ID": 108, "Product Name": "Coffee Mug",  "Category": "Kitchen",       "Supplier": "Supplier F", "Unit Price":    7.99, "Quantity": 25, "Date Added": "2025-11-18"},
    {"Product ID": 109, "Product Name": "Whiteboard",  "Category": "Office Supplies","Supplier": "Supplier C", "Unit Price":   45.00, "Quantity":  3, "Date Added": "2025-11-19"},
    {"Product ID": 110, "Product Name": "Keyboard",    "Category": "Electronics",   "Supplier": "Supplier B", "Unit Price":   30.00, "Quantity": 14, "Date Added": "2025-11-19"}
]
df_initial = pd.DataFrame(initial_data)
df_initial["Date Added"] = pd.to_datetime(df_initial["Date Added"]).dt.date

# Store DataFrame in session state
if 'df' not in st.session_state:
    st.session_state.df = df_initial.copy()
df = st.session_state.df

# ----- Layout and Theme -----
st.set_page_config(page_title="Inventory Management", layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #003366;  /* Dark blue */
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    [data-testid="stAppViewContainer"] > .main {
        background-color: #B0E0E6;  /* Pastel light blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Inventory Management")
page = st.sidebar.radio("Navigate", ["Dashboard", "View Inventory", "Add Item", "Edit Item", "Delete Item"])

# ----- Dashboard -----
if page == "Dashboard":
    st.header("Dashboard")
    # Compute KPIs
    total_products = df.shape[0]
    total_quantity = int(df["Quantity"].sum())
    unique_suppliers = int(df["Supplier"].nunique())
    low_stock_count = int(df[df["Quantity"] <= 10].shape[0])
    # Display KPIs
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Products", total_products)
    k2.metric("Total Quantity", total_quantity)
    k3.metric("Unique Suppliers", unique_suppliers)
    k4.metric("Low Stock (<=10)", low_stock_count)
    st.write("---")
    # Charts: Bar, Pie, Histogram
    fig_bar = px.bar(df, x="Product Name", y="Quantity", title="Product Quantity", color="Category")
    fig_pie = px.pie(df, names="Category", title="Category Distribution")
    fig_hist = px.histogram(df, x="Unit Price", nbins=10, title="Unit Price Distribution", color="Category")
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig_bar, use_container_width=True)
    col2.plotly_chart(fig_pie, use_container_width=True)
    st.plotly_chart(fig_hist, use_container_width=True)
    st.write("---")
    # Date filter widget
    selected_date = st.date_input("Filter by Date Added", value=datetime.date.today())
    if selected_date:
        filtered = df[df["Date Added"] == selected_date]
        st.subheader(f"Products added on {selected_date}")
        if not filtered.empty:
            st.dataframe(filtered)
        else:
            st.info("No products found on this date.")
    # Chatbot panel (basic queries)
    st.subheader("Inventory Chatbot")
    if prompt := st.chat_input("Ask a question about the inventory"):
        st.chat_message("user").text(prompt)
        answer = "Sorry, I don't understand."
        pl = prompt.lower()
        if "total products" in pl:
            answer = f"There are {total_products} products in inventory."
        elif "total quantity" in pl:
            answer = f"The total quantity of all products is {total_quantity}."
        elif "unique suppliers" in pl:
            answer = f"There are {unique_suppliers} unique suppliers."
        elif "low stock" in pl:
            answer = f"There are {low_stock_count} items with low stock (<=10)."
        st.chat_message("assistant").text(answer)

# ----- View Inventory -----
elif page == "View Inventory":
    st.header("View Inventory")
    st.dataframe(df)

# ----- Add Item -----
elif page == "Add Item":
    st.header("Add New Item")
    with st.form("add_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            new_name = st.text_input("Product Name")
            new_category = st.text_input("Category")
            new_supplier = st.text_input("Supplier")
        with col2:
            new_price = st.number_input("Unit Price", min_value=0.0, step=0.01)
            new_qty = st.number_input("Quantity", min_value=0, step=1)
            new_date = st.date_input("Date Added", value=datetime.date.today())
        submitted = st.form_submit_button("Add Item")
        if submitted:
            if new_name and new_category and new_supplier:
                new_id = int(df["Product ID"].max() + 1)
                new_entry = {
                    "Product ID": new_id,
                    "Product Name": new_name,
                    "Category": new_category,
                    "Supplier": new_supplier,
                    "Unit Price": new_price,
                    "Quantity": new_qty,
                    "Date Added": new_date
                }
                st.session_state.df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
                st.success(f"Added product '{new_name}' with ID {new_id}.")

# ----- Edit Item -----
elif page == "Edit Item":
    st.header("Edit Existing Item")
    if df.empty:
        st.warning("No items to edit.")
    else:
        item_id = st.selectbox("Select Product ID to edit", df["Product ID"].tolist())
        item_data = df[df["Product ID"] == item_id].iloc[0]
        with st.form("edit_form"):
            ecol1, ecol2 = st.columns(2)
            with ecol1:
                edit_name = st.text_input("Product Name", item_data["Product Name"])
                edit_category = st.text_input("Category", item_data["Category"])
                edit_supplier = st.text_input("Supplier", item_data["Supplier"])
            with ecol2:
                edit_price = st.number_input("Unit Price", value=float(item_data["Unit Price"]))
                edit_qty = st.number_input("Quantity", value=int(item_data["Quantity"]))
                edit_date = st.date_input("Date Added", value=item_data["Date Added"])
            edit_submit = st.form_submit_button("Update Item")
            if edit_submit:
                idx = st.session_state.df.index[st.session_state.df["Product ID"] == item_id][0]
                st.session_state.df.at[idx, "Product Name"] = edit_name
                st.session_state.df.at[idx, "Category"] = edit_category
                st.session_state.df.at[idx, "Supplier"] = edit_supplier
                st.session_state.df.at[idx, "Unit Price"] = edit_price
                st.session_state.df.at[idx, "Quantity"] = edit_qty
                st.session_state.df.at[idx, "Date Added"] = edit_date
                st.success(f"Updated product ID {item_id}.")

# ----- Delete Item -----
elif page == "Delete Item":
    st.header("Delete Item")
    if df.empty:
        st.warning("No items to delete.")
    else:
        del_id = st.selectbox("Select Product ID to delete", df["Product ID"].tolist())
        if st.button("Delete"):
            st.session_state.df = df[df["Product ID"] != del_id].reset_index(drop=True)
            st.success(f"Deleted product ID {del_id}.")

