
import datetime
import tkinter as tk
from tkinter import messagebox

class Item:
    def __init__(self, item_no, name, unit_price, quantity):
        self.item_no = item_no
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
        self.total_price = unit_price * quantity
        
class Receipt:
    def __init__(self, cashier_name, date, items):
        self.cashier_name = cashier_name
        self.date = date
        self.items = items

    def calculate_total(self):
        return sum(item.total_price for item in self.items)


class ReceiptApp:
    def __init__(self, root):  # Ensure to accept 'root' as argument
        self.root = root
        self.root.title("Store Receipt Management")
        
        self.items = []
        
        # Create interface elements
        self.create_interface()


    def create_interface(self):
        tk.Label(self.root, text="Cashier Name:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.cashier_name_var = tk.StringVar()
        self.cashier_name_entry = tk.Entry(self.root, textvariable=self.cashier_name_var)
        self.cashier_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Item No:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.item_no_var = tk.StringVar()
        self.item_no_entry = tk.Entry(self.root, textvariable=self.item_no_var)
        self.item_no_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Item Name:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.item_name_var = tk.StringVar()
        self.item_name_entry = tk.Entry(self.root, textvariable=self.item_name_var)
        self.item_name_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Unit Price:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.unit_price_var = tk.DoubleVar()
        self.unit_price_entry = tk.Entry(self.root, textvariable=self.unit_price_var)
        self.unit_price_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Quantity:").grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        self.quantity_var = tk.IntVar()
        self.quantity_entry = tk.Entry(self.root, textvariable=self.quantity_var)
        self.quantity_entry.grid(row=4, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.receipt_text = tk.Text(self.root, state='disabled', width=60, height=15)
        self.receipt_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.print_button = tk.Button(self.root, text="Print Receipt", command=self.print_receipt)
        self.print_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_item(self):
        item_no = self.item_no_var.get()
        item_name = self.item_name_var.get()
        unit_price = self.unit_price_var.get()
        quantity = self.quantity_var.get()

        if item_no and item_name and unit_price and quantity:
            item = Item(item_no, item_name, unit_price, quantity)
            self.items.append(item)
            messagebox.showinfo("Success", "Item added to receipt.")
            self.item_no_entry.delete(0, tk.END)
            self.item_name_entry.delete(0, tk.END)
            self.unit_price_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def print_receipt(self):
        cashier_name = self.cashier_name_var.get()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        receipt = Receipt(cashier_name, date, self.items)

        self.receipt_text.config(state='normal')
        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.insert(tk.END, "===================================================\n")
        self.receipt_text.insert(tk.END, "            Store Receipt           \n")
        self.receipt_text.insert(tk.END, "===================================================\n")
        self.receipt_text.insert(tk.END, f"Cashier: {receipt.cashier_name}\n")
        self.receipt_text.insert(tk.END, f"Date: {receipt.date}\n")
        self.receipt_text.insert(tk.END, "===================================================\n")
        self.receipt_text.insert(tk.END, "Item No | Name        | Unit Price | Qty | Total\n")
        self.receipt_text.insert(tk.END, "---------------------------------------------------\n")
        for item in receipt.items:
            self.receipt_text.insert(tk.END, f"{item.item_no:<7} | {item.name:<10} | {item.unit_price:<9} FCFA | {item.quantity:<3} | {item.total_price:<5} FCFA\n")
        self.receipt_text.insert(tk.END, "===================================================\n")
        self.receipt_text.insert(tk.END, f"Total: {receipt.calculate_total()} FCFA\n")
        self.receipt_text.insert(tk.END, "===================================================\n")
        self.receipt_text.config(state='disabled')

        self.save_receipt_to_file(receipt, "receipt.txt")
        messagebox.showinfo("Success", "Receipt printed and saved to 'receipt.txt'")

    def save_receipt_to_file(self, receipt, filename):
        with open(filename, "w") as file:
            file.write("===================================================\n")
            file.write("            Store Receipt           \n")
            file.write("===================================================\n")
            file.write(f"Cashier: {receipt.cashier_name}\n")
            file.write(f"Date: {receipt.date}\n")
            file.write("===================================================\n")
            file.write("Item No | Name        | Unit Price | Qty | Total\n")
            file.write("---------------------------------------------------\n")
            for item in receipt.items:
                file.write(f"{item.item_no:<7} | {item.name:<10} | {item.unit_price:<9} FCFA | {item.quantity:<3} | {item.total_price:<5}\n")
            file.write("===================================================\n")
            file.write(f"Total: {receipt.calculate_total()} FCFA\n")
            file.write("===================================================\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiptApp(root)
    root.mainloop()
