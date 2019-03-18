import os
import pymysql
import pandas as pd

#mysql running locally (using Xampp with Mysql Running)
host = "127.0.0.1"
port = 3306
user = "root"
password = ""
db = "data_analysis_db"

conn = pymysql.connect(
    host=host,
    port=int(3306),
    user=user,
    passwd=password,
    db=db,
    charset='utf8mb4')

#gets memembers who have late payments
#this could be part of larger function which increments members balance's adding the late fee amount to to account and/or send alerts to members with late payments
def get_overdue_payments():
	df = pd.read_sql(
		# "SELECT m.id, m.first_name, m.last_name, p.scheduled_date, t.payment_amount FROM payments p left join transcactions t on p.transaction_id = t.transaction_id  left join memmber m on m.member_id = t.members_id where p.closing_date > p.scheduled_date and t.is_active = true",
		"SELECT * FROM members",
    conn)
	print(df.tail(10))

#if interest rate goes up/down, function could be used to update db accordingly
def update_int_rate_amnt(loan_type, value):
	df = pd.read_sql("SELECT * FROM LOANS",conn)
	df[df["loan_type"] == loan_type, "int_rate"] = value
	df.to_sql("loans", if_exists = "replace")
	print("Update complete.")

#main
get_overdue_payments()
update_int_rate_amnt("mortgage", "0.10")

