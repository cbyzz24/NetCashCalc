import streamlit as st

#title section
main_title=st.header(":blue[Net Cash Calculator] :chart_with_upwards_trend:", divider="rainbow")
#st.container(height=1,border=False)

col1, col2 =st.columns(2, gap="large")
with col1:
#account section
    accts_title=st.subheader(":green[Cash Account Balances]")

    chase_amount=st.text_input("Chase Bank", placeholder="0.00")

    capital_one_amount=st.text_input("Capital One", placeholder="0.00")

    initial_cash_total=st.text_input("Total Initial Cash Balance", placeholder="0.00")
    st.container(height=68, border=False)
    st.write("---")
    
    #bills section
    bills_title=st.subheader(":red[Bills]")
    total_bills=st.text_input("Total Bill Amount", placeholder="0.00")


#st.write("---")

with col2:
    #pending transactions section
    pending_section_title=st.subheader(":orange[Pending Transactions]")
    trans1_title=st.text_input("Transaction 1", placeholder="Enter Amount")
    trans2_title=st.text_input("Transaction 2", placeholder="Enter Amount")
    trans3_title=st.text_input("Transaction 3", placeholder="Enter Amount")
    #trans4_title=st.text_input("Transaction 4", placeholder="Enter Amount")
    pending_trans_total=st.text_input("Total Pending Transactions", placeholder="0.00")
    st.write("---")

    #net cash section
    net_cash_title=st.subheader(":rainbow[Net Cash]")
    total_net_cash=st.text_input(":blue[Total Net Cash]", placeholder="0.00")
    calc_button=st.button(":green[Calculate Cash]")




