import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['order_id'])
    e2.insert(0,select['date'])
    e3.insert(0,select['name'])
    e4.insert(0,select['quantity'])
    e5.insert(0,select['price'])


def Add():
    order_id = e1.get()
    date = e2.get()
    name = e3.get()
    quantity = e4.get()
    price = e5.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sales_record")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  record (order_id,date,name,quantity,price) VALUES (%s, %s, %s, %s, %s)"
       val = (order_id,date,name,quantity,price)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record inserted Successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


def update():
    order_id = e1.get()
    date = e2.get()
    name = e3.get()
    quantity = e4.get()
    price = e5.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sales_record")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  record set date= %s,name= %s,quantity= %s,price= %s where order_id= %s"
       val = (date,name,quantity,price,order_id)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updated Successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delete():
    order_id = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sales_record")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from record where order_id = %s"
       val = (order_id,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleted Successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="sales_record")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT order_id,date,name,quantity,price FROM record")
        record = mycursor.fetchall()
        print(record)

        for i, (id,date,name, quantity,price) in enumerate(record, start=1):
            listBox.insert("", "end", values=(id,date, name, quantity, price))
            mysqldb.close()

root = Tk()
root.geometry("1000x500")
global e1
global e2
global e3
global e4
global e5

tk.Label(root, text="SALES CRUD APPLICATION", fg="black", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Order ID").place(x=10, y=10)
Label(root, text="Date").place(x=10, y=30)
Label(root, text="Name").place(x=10, y=50)
Label(root, text="Quantity").place(x=10, y=70)
Label(root, text="Price").place(x=10, y=90)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=30)

e3 = Entry(root)
e3.place(x=140, y=50)

e4 = Entry(root)
e4.place(x=140, y=70)

e5 = Entry(root)
e5.place(x=140, y=90)

Button(root, text="Add",fg='blue',bg='white',command = Add,height=3, width= 13).place(x=30, y=130)
Button(root, text="Update",fg='green',bg='white',command = update,height=3, width= 13).place(x=140, y=130)
Button(root, text="Delete",fg='red',bg='white',command = delete,height=3, width= 13).place(x=250, y=130)

cols = ('order_id','date', 'name','quantity','price')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()

