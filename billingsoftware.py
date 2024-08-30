from tkinter import *
import math
import os
import random
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ========== Variables ==========
        # Cosmetics
        self.soap_price = IntVar()
        self.face_cream_price = IntVar()
        self.face_wash_price = IntVar()
        self.hair_spray_price = IntVar()
        self.hair_gel_price = IntVar()
        self.body_lotion_price = IntVar()

        # Grocery
        self.rice_price = IntVar()
        self.food_oil_price = IntVar()
        self.daal_price = IntVar()
        self.wheat_price = IntVar()
        self.sugar_price = IntVar()
        self.tea_price = IntVar()

        # Cold Drinks
        self.maza_price = IntVar()
        self.cock_price = IntVar()
        self.frooti_price = IntVar()
        self.thumbsup_price = IntVar()
        self.limca_price = IntVar()
        self.sprite_price = IntVar()

        # Total Product Price and Tax Variables
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # Customer
        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        # ========== Customer Details Frame ==========
        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white",
                          font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cphone_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                               column=3,
                                                                                                               pady=5,
                                                                                                               padx=10)

        cbill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                  column=5,
                                                                                                                  pady=5,
                                                                                                                  padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0,
                                                                                                               column=6,
                                                                                                               padx=10,
                                                                                                               pady=10)

        # ========== Cosmetics Frame ==========
        F2 = LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.soap_price, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream_price, font=("times new roman", 16, "bold"),
                               bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2, width=10, textvariable=self.face_wash_price, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10, textvariable=self.hair_spray_price, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2, width=10, textvariable=self.hair_gel_price, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10, textvariable=self.body_lotion_price, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ========== Grocery Frame ==========
        F3 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.rice_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.food_oil_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.daal_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.wheat_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.sugar_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.tea_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ========== Cold Drink Frame ==========
        F4 = LabelFrame(self.root, text="Cold Drinks", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        c1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.maza_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(F4, text="Coca Cola", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.cock_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.frooti_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.thumbsup_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.limca_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.sprite_price, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ========== Bill Area Frame ==========
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000, y=180, width=350, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ========== Button Frame ==========
        F6 = LabelFrame(self.root, text="Billing Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Cosmetic Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=740, width=580, height=105)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white", pady=15, width=11,
                           bd=5, font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        GBill_btn = Button(btn_F, command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white", pady=15,
                           width=11, bd=5, font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, command=self.clear_data, text="Clear", bg="cadetblue", fg="white", pady=15, width=11,
                           bd=5, font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, command=self.exit_app, text="Exit", bg="cadetblue", fg="white", pady=15, width=11,
                          bd=5, font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        # Calculating Cosmetic Prices
        self.total_cosmetic_price = (
            self.soap_price.get() * 40 +
            self.face_cream_price.get() * 120 +
            self.face_wash_price.get() * 60 +
            self.hair_spray_price.get() * 180 +
            self.hair_gel_price.get() * 140 +
            self.body_lotion_price.get() * 180
        )
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.cosmetic_tax.set("Rs. " + str(round(self.total_cosmetic_price * 0.05, 2)))

        # Calculating Grocery Prices
        self.total_grocery_price = (
            self.rice_price.get() * 80 +
            self.food_oil_price.get() * 180 +
            self.daal_price.get() * 60 +
            self.wheat_price.get() * 240 +
            self.sugar_price.get() * 45 +
            self.tea_price.get() * 150
        )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.grocery_tax.set("Rs. " + str(round(self.total_grocery_price * 0.1, 2)))

        # Calculating Cold Drink Prices
        self.total_cold_drink_price = (
            self.maza_price.get() * 60 +
            self.cock_price.get() * 60 +
            self.frooti_price.get() * 50 +
            self.thumbsup_price.get() * 45 +
            self.limca_price.get() * 40 +
            self.sprite_price.get() * 60
        )
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.cold_drink_tax.set("Rs. " + str(round(self.total_cold_drink_price * 0.05, 2)))

        self.total_bill = float(
            self.total_cosmetic_price +
            self.total_grocery_price +
            self.total_cold_drink_price +
            float(self.cosmetic_tax.get()[4:]) +
            float(self.grocery_tax.get()[4:]) +
            float(self.cold_drink_tax.get()[4:])
        )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Our Store")
        self.txtarea.insert(END, f"\n\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number : {self.c_phone.get()}")
        self.txtarea.insert(END, "\n===================================")
        self.txtarea.insert(END, "\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END, "\n===================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer Details are Must")
        elif self.cosmetic_price.get() == "Rs. 0" and self.grocery_price.get() == "Rs. 0" and self.cold_drink_price.get() == "Rs. 0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # Cosmetics
            if self.soap_price.get() != 0:
                self.txtarea.insert(END, f"\nBath Soap\t\t{self.soap_price.get()}\t\t{self.soap_price.get() * 40}")
            if self.face_cream_price.get() != 0:
                self.txtarea.insert(END, f"\nFace Cream\t\t{self.face_cream_price.get()}\t\t{self.face_cream_price.get() * 120}")
            if self.face_wash_price.get() != 0:
                self.txtarea.insert(END, f"\nFace Wash\t\t{self.face_wash_price.get()}\t\t{self.face_wash_price.get() * 60}")
            if self.hair_spray_price.get() != 0:
                self.txtarea.insert(END, f"\nHair Spray\t\t{self.hair_spray_price.get()}\t\t{self.hair_spray_price.get() * 180}")
            if self.hair_gel_price.get() != 0:
                self.txtarea.insert(END, f"\nHair Gel\t\t{self.hair_gel_price.get()}\t\t{self.hair_gel_price.get() * 140}")
            if self.body_lotion_price.get() != 0:
                self.txtarea.insert(END, f"\nBody Lotion\t\t{self.body_lotion_price.get()}\t\t{self.body_lotion_price.get() * 180}")

            # Grocery
            if self.rice_price.get() != 0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice_price.get()}\t\t{self.rice_price.get() * 80}")
            if self.food_oil_price.get() != 0:
                self.txtarea.insert(END, f"\nFood Oil\t\t{self.food_oil_price.get()}\t\t{self.food_oil_price.get() * 180}")
            if self.daal_price.get() != 0:
                self.txtarea.insert(END, f"\nDaal\t\t{self.daal_price.get()}\t\t{self.daal_price.get() * 60}")
            if self.wheat_price.get() != 0:
                self.txtarea.insert(END, f"\nWheat\t\t{self.wheat_price.get()}\t\t{self.wheat_price.get() * 240}")
            if self.sugar_price.get() != 0:
                self.txtarea.insert(END, f"\nSugar\t\t{self.sugar_price.get()}\t\t{self.sugar_price.get() * 45}")
            if self.tea_price.get() != 0:
                self.txtarea.insert(END, f"\nTea\t\t{self.tea_price.get()}\t\t{self.tea_price.get() * 150}")

            # Cold Drinks
            if self.maza_price.get() != 0:
                self.txtarea.insert(END, f"\nMaza\t\t{self.maza_price.get()}\t\t{self.maza_price.get() * 60}")
            if self.cock_price.get() != 0:
                self.txtarea.insert(END, f"\nCoca Cola\t\t{self.cock_price.get()}\t\t{self.cock_price.get() * 60}")
            if self.frooti_price.get() != 0:
                self.txtarea.insert(END, f"\nFrooti\t\t{self.frooti_price.get()}\t\t{self.frooti_price.get() * 50}")
            if self.thumbsup_price.get() != 0:
                self.txtarea.insert(END, f"\nThumbs Up\t\t{self.thumbsup_price.get()}\t\t{self.thumbsup_price.get() * 45}")
            if self.limca_price.get() != 0:
                self.txtarea.insert(END, f"\nLimca\t\t{self.limca_price.get()}\t\t{self.limca_price.get() * 40}")
            if self.sprite_price.get() != 0:
                self.txtarea.insert(END, f"\nSprite\t\t{self.sprite_price.get()}\t\t{self.sprite_price.get() * 60}")

            self.txtarea.insert(END, "\n-----------------------------------")
            if self.cosmetic_tax.get() != "Rs. 0":
                self.txtarea.insert(END, f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0":
                self.txtarea.insert(END, f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0":
                self.txtarea.insert(END, f"\nCold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\nTotal Bill : \t\t\tRs. {str(self.total_bill)}")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.soap_price.set(0)
            self.face_cream_price.set(0)
            self.face_wash_price.set(0)
            self.hair_spray_price.set(0)
            self.hair_gel_price.set(0)
            self.body_lotion_price.set(0)

            self.rice_price.set(0)
            self.food_oil_price.set(0)
            self.daal_price.set(0)
            self.wheat_price.set(0)
            self.sugar_price.set(0)
            self.tea_price.set(0)

            self.maza_price.set(0)
            self.cock_price.set(0)
            self.frooti_price.set(0)
            self.thumbsup_price.set(0)
            self.limca_price.set(0)
            self.sprite_price.set(0)

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()

