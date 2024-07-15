import streamlit as st

#title section
main_title=st.header("Net Cash Calculator")
st.write("---")

col1, col2 =st.columns(2, gap="large")
with col1:
#account section
    accts_title=st.subheader("Cash Account Balances")

    chase_amount=st.text_input("Chase Bank", placeholder="$0.00")

    capital_one_amount=st.text_input("Capital One", placeholder="$0.00")

    initial_cash_total=st.text_input("Total Initial Cash Balance", placeholder="$0.00")
    st.write("---")
    
    #bills section
    bills_title=st.subheader("Bills")
    total_bills=st.text_input("Total Bill Amount", placeholder="$0.00")

    st.write("---")
    calc_button=st.button("Calculate Cash")
st.write("---")

with col2:
    #pending transactions section
    pending_section_title=st.subheader("Pending Transactions")
    trans1_title=st.text_input("Transaction 1", placeholder="Enter Amount")
    trans2_title=st.text_input("Transaction 2", placeholder="Enter Amount")
    trans3_title=st.text_input("Transaction 3", placeholder="Enter Amount")
    #trans4_title=st.text_input("Transaction 4", placeholder="Enter Amount")
    pending_trans_total=st.text_input("Total Pending Transactions", placeholder="$0.00")
    st.write("---")

    #net cash section
    net_cash_title=st.subheader("Net Cash")
    total_net_cash=st.text_input("Total Net Cash", placeholder="$0.00")





