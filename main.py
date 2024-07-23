import streamlit as st
#import math


#title section
main_title=st.header(":blue[Cash Calculator] :chart_with_upwards_trend:", divider="rainbow")
#st.container(height=1,border=False)

#Account Balance Section
st.write("#### Current Account Balances")
col1, col2, col3 = st.columns(3, gap="large")
bank_1_balance = col1.number_input("Bank 1")
bank_2_balance = col2.number_input("Bank 2")
calc_total_cash_balance = bank_1_balance + bank_2_balance
display_total_cash_balance = col3.metric(label=":green[Total Initial Cash]", value=f"${calc_total_cash_balance:,.2f}")

st.write("---")

#Pending Tranactions Section
st.write("#### Pending Transactions")
col1, col2 = st.columns(2, gap="large")
with col1:
    amount_1 = st.number_input("Amount 1")
    amount_2 = st.number_input("Amount 2")
    amount_3 = st.number_input("Amount 3")
with col2:
    amount_4 = st.number_input("Amount 4")
    amount_5 = st.number_input("Amount 5")
    amount_6 = st.number_input("Amount 6")

calc_total_pending_transactions = amount_1 + amount_2 + amount_3 + amount_4 + amount_5 + amount_6

col1, col2 = st.columns(2, gap="large")
with col1:
    st.text("")
with col2:
    display_total_pending_transactions = col2.metric(label=":red[Total Pending Transactions]", value=f"${calc_total_pending_transactions:,.2f}")

st.write("---")

# Upcoming Bills Section 
st.write("#### Upcoming Bills")
col1, col2 = st.columns(2, gap="large")
with col1:
    total_upcomming_bills = st.number_input("Total Upcoming Bills")
calc_total_upcoming_bills = total_upcomming_bills
with col2:
    display_total_upcoming_bills = col2.metric(label=":orange[Total Bills]", value=f"${calc_total_upcoming_bills:,.2f}")

st.write("---")

# Net Cash Section
st.write("#### Remaining Cash")
col1, col2 = st.columns(2, gap="large")
with col1:
    st.write("")
positive_flows = bank_1_balance + bank_2_balance
negative_flows = amount_1 + amount_2 + amount_3 + amount_4 + amount_5 + amount_6 + total_upcomming_bills
with col2:
    display_net_cash = col2.metric(label=":green[Net Cash]", value=f"${positive_flows - negative_flows:,.2f}")
