from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_App:
	def __init__(self,root):
		self.root = root
		self.root.geometry('1350x700+0+0')
		self.root.title('Billing Software With Kewal')
		bg_colour='#074463'
		title=Label(self.root,text='Billing Software With Kewal',bd=12,relief=GROOVE,bg=bg_colour,fg='white',font=('times new roman',30,'bold'),pady=2).pack(fill=X)


#===================================== variables ===================================
	
	#============================ Cosmetics
		self.soap=IntVar()
		self.face_cream=IntVar()
		self.face_wash=IntVar()
		self.spray=IntVar()
		self.gell=IntVar()
		self.loshan=IntVar()
		
		#============= grocery
		self.rice=IntVar()
		self.food_oil=IntVar()
		self.daal=IntVar()
		self.wheat=IntVar()
		self.sugar=IntVar()
		self.tea=IntVar()

		#================== cold drinks
		self.maza=IntVar()
		self.coke=IntVar()
		self.frooti=IntVar()
		self.thumbsup=IntVar()
		self.limca=IntVar()
		self.sprite=IntVar()

		#============= total product price & tax variable
		self.cosmetics_price=StringVar()
		self.grocery_price=StringVar()
		self.cold_drink_price=StringVar()

		self.cosmetics_tax=StringVar()
		self.grocery_tax=StringVar()
		self.cold_drink_tax=StringVar()

		#====================== Customer
		self.c_name=StringVar()
		self.c_phn=StringVar()

		self.bill_no=StringVar()
		x=random.randint(1000,9999)
		self.bill_no.set(str(x))

		self.search_bill=StringVar()


#========================== customer details=====================================

		F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',bg=bg_colour)
		F1.place(x=0,y=80,relwidth=1)

		cname_lbl=Label(F1,text='Customer Name',bg=bg_colour,fg='white',font=('times new roman',18,'bold')).grid(row=0,column=0,padx=20,pady=5)
		cname_txt=Entry(F1,width=15,bd=7,textvariable=self.c_name,relief=SUNKEN,font='arial 15').grid(row=0,column=1,pady=5,padx=10)

		cphn_lbl=Label(F1,text='Phone No.',bg=bg_colour,fg='white',font=('times new roman',18,'bold')).grid(row=0,column=2,padx=20,pady=5)
		cphn_txt=Entry(F1,width=15,bd=7,textvariable=self.c_phn,relief=SUNKEN,font='arial 15').grid(row=0,column=3,pady=5,padx=10)

		cbill_lbl=Label(F1,text='Bill Name',bg=bg_colour,fg='white',font=('times new roman',18,'bold')).grid(row=0,column=4,padx=20,pady=5)
		cbill_txt=Entry(F1,width=15,bd=7,relief=SUNKEN,textvariable=self.search_bill,font='arial 15').grid(row=0,column=5,pady=5,padx=10)

		bill_btn=Button(F1,text='Search',command=self.find_bill,width=10,bd=7,font='arial 12 bold').grid(row=0,column=6,padx=10,pady=10)

#========================cosmetics frame ========================================

		F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bg=bg_colour)
		F2.place(x=5,y=180,width=325,height=380)

		bath_lbl=Label(F2,text='Bath Soap',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky='w')
		bath_txt=Entry(F2,width=10,textvariable=self.soap,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		Face_cream_lbl=Label(F2,text='Face Cream',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=1,column=0,padx=10,pady=10,sticky='w')
		Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		Face_w_lbl=Label(F2,text='Face Wash',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=2,column=0,padx=10,pady=10,sticky='w')
		Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		Hair_s_lbl=Label(F2,text='Hair Spray',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=3,column=0,padx=10,pady=10,sticky='w')
		Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		Hair_g_lbl=Label(F2,text='Hair Gell',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=4,column=0,padx=10,pady=10,sticky='w')
		Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

		Body_lbl=Label(F2,text='Body Loshan',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=5,column=0,padx=10,pady=10,sticky='w')
		Body_txt=Entry(F2,width=10,textvariable=self.loshan,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#========================Grocery frame ============================================

		F3 = LabelFrame(self.root,bd=10,relief=GROOVE,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bg=bg_colour)
		F3.place(x=340,y=180,width=325,height=380)

		g1_lbl=Label(F3,text='Rice',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky='w')
		g1_txt=Entry(F3,width=10,textvariable=self.rice,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		g2_lbl=Label(F3,text='Food Oil',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=1,column=0,padx=10,pady=10,sticky='w')
		g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		g3_lbl=Label(F3,text='Daal',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=2,column=0,padx=10,pady=10,sticky='w')
		g3_txt=Entry(F3,width=10,textvariable=self.daal,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		g4_lbl=Label(F3,text='Wheat',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=3,column=0,padx=10,pady=10,sticky='w')
		g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		g5_lbl=Label(F3,text='Sugar',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=4,column=0,padx=10,pady=10,sticky='w')
		g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

		g6_lbl=Label(F3,text='Tea',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=5,column=0,padx=10,pady=10,sticky='w')
		g6_txt=Entry(F3,width=10,textvariable=self.tea,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#====================Cold Drink Frame ====================================================

		F4 = LabelFrame(self.root,bd=10,relief=GROOVE,text='Cold Drinks',font=('times new roman',15,'bold'),fg='gold',bg=bg_colour)
		F4.place(x=670,y=180,width=325,height=380)

		g1_lbl=Label(F4,text='Maza',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky='w')
		g1_txt=Entry(F4,width=10,textvariable=self.maza,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		g2_lbl=Label(F4,text='Coke',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=1,column=0,padx=10,pady=10,sticky='w')
		g2_txt=Entry(F4,width=10,textvariable=self.coke,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		g3_lbl=Label(F4,text='Frooti',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=2,column=0,padx=10,pady=10,sticky='w')
		g3_txt=Entry(F4,width=10,textvariable=self.frooti,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		g4_lbl=Label(F4,text='Thumbsup',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=3,column=0,padx=10,pady=10,sticky='w')
		g4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		g5_lbl=Label(F4,text='Limca',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=4,column=0,padx=10,pady=10,sticky='w')
		g5_txt=Entry(F4,width=10,textvariable=self.limca,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

		g6_lbl=Label(F4,text='Sprite',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=5,column=0,padx=10,pady=10,sticky='w')
		g6_txt=Entry(F4,width=10,textvariable=self.sprite,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


#==================== bill area ======================================================

		F5 = Frame(self.root,bd=10,relief=GROOVE)
		F5.place(x=1010,y=180,width=350,height=380)
		bill_title=Label(F5,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
		scroll_y=Scrollbar(F5,orient=VERTICAL)
		self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_y.config(command=self.txtarea.yview)
		self.txtarea.pack(fill=BOTH,expand=1)


#=======================button frame ============================================================

		F6=LabelFrame(self.root,bd=10,relief=GROOVE,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bg=bg_colour)
		F6.place(x=0,y=560,relwidth=1,height=140)

		m1_lbl=Label(F6,text='Total Cosmetic Price',bg=bg_colour,fg='white',font=("times new roman",14,'bold')).grid(row=0,column=0,padx=20,pady=1,sticky='w')
		m1_txt=Entry(F6,width=18,textvariable=self.cosmetics_price,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

		m2_lbl=Label(F6,text='Total Grocery Price',bg=bg_colour,fg='white',font=("times new roman",14,'bold')).grid(row=1,column=0,padx=20,pady=1,sticky='w')
		m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

		m3_lbl=Label(F6,text='Total Cold Drinks Price',bg=bg_colour,fg='white',font=("times new roman",14,'bold')).grid(row=2,column=0,padx=20,pady=1,sticky='w')
		m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


		c1_lbl=Label(F6,text='Cosmetic Tax',bg=bg_colour,fg='white',font=("times new roman",14,'bold')).grid(row=0,column=2,padx=20,pady=1,sticky='w')
		c1_txt=Entry(F6,width=18,textvariable=self.cosmetics_tax,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

		c2_lbl=Label(F6,text='Grocery Tax',bg=bg_colour,fg='white',font=("times new roman",14,'bold')).grid(row=1,column=2,padx=20,pady=1,sticky='w')
		c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

		c3_lbl=Label(F6,text=' Cold Drinks Tax',bg=bg_colour,fg='white',font=("times new roman",14,'bold')).grid(row=2,column=2,padx=20,pady=1,sticky='w')
		c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


		btn_F=Frame(F6,bd=7,relief=GROOVE)
		btn_F.place(x=750,width=580,height=105)

		total_btn=Button(btn_F,command=self.total,text='Total',bg='cadetblue',fg='white',pady=15,padx=2,bd=2,width=10,font='arial 15 bold').grid(row=0,column=0,padx=5,pady=5)
		GBill_btn=Button(btn_F,command=self.bill_area,text='Generate Bill',bg='cadetblue',fg='white',pady=15,padx=2,bd=2,width=10,font='arial 15 bold').grid(row=0,column=1,padx=5,pady=5)
		Clear_btn=Button(btn_F,text='Clear',bg='cadetblue',command=self.clear_data,fg='white',pady=15,padx=2,bd=2,width=10,font='arial 15 bold').grid(row=0,column=2,padx=5,pady=5)
		Exit_btn=Button(btn_F,text='Exit',command=self.Exit_app,bg='cadetblue',fg='white',pady=15,padx=2,bd=2,width=10,font='arial 15 bold').grid(row=0,column=3,padx=5,pady=5)
		self.welcome_bill()

	def total(self):

		self.c_s_p=self.soap.get()*40
		self.c_fc_p=self.face_cream.get()*120                      # cosmetics
		self.c_fw_p=self.face_wash.get()*60
		self.c_hs_p=self.spray.get()*180
		self.c_hg_p=self.gell.get()*140
		self.c_bl_p=self.loshan.get()*180
		self.total_cosmetic_price=float(
									self.c_s_p+
									self.c_fc_p+
									self.c_fw_p+
									self.c_hs_p+
									self.c_hg_p+
									self.c_bl_p
									)
		self.cosmetics_price.set('Rs. '+str(self.total_cosmetic_price))
		self.c_tax=round((self.total_cosmetic_price*0.05),2)
		self.cosmetics_tax.set('Rs. '+str(self.c_tax))  #round(number,how many decimal point)


	
		self.g_r_p=self.rice.get()*40
		self.g_f_p=self.food_oil.get()*120
		self.g_d_p=self.daal.get()*60
		self.g_w_p=self.wheat.get()*180                      # grocery
		self.g_s_p=self.sugar.get()*140
		self.g_t_p=self.tea.get()*180
		self.total_grocery_price=float(
									self.g_r_p+
									self.g_f_p+
									self.g_d_p+
									self.g_w_p+
									self.g_s_p+
									self.g_t_p
									)
		self.grocery_price.set('Rs. '+str(self.total_grocery_price))
		self.g_tax=round((self.total_grocery_price*0.01),2)
		self.grocery_tax.set('Rs. '+str(self.g_tax))  #round(number,how many decimal point)



		self.d_m_p=self.maza.get()*60
		self.d_c_p=self.coke.get()*60            #cold drink
		self.d_f_p=self.frooti.get()*50
		self.d_t_p=self.thumbsup.get()*45
		self.d_l_p=self.limca.get()*40
		self.d_s_p=self.sprite.get()*60
		self.total_drinks_price=float(
									self.d_m_p+
									self.d_c_p+
									self.d_f_p+
									self.d_t_p+
									self.d_l_p+
									self.d_s_p
									)
		self.cold_drink_price.set('Rs. '+str(self.total_drinks_price))
		self.d_tax=round((self.total_drinks_price*0.05),2)
		self.cold_drink_tax.set('Rs. '+str(self.d_tax))  #round(number,how many decimal point)

		self.Total_bill=float(	self.total_cosmetic_price+
								self.total_grocery_price+
								self.total_drinks_price+
								self.c_tax+
								self.g_tax+
								self.d_tax
							)

	def welcome_bill(self):
		self.txtarea.delete('1.0',END)
		self.txtarea.insert(END,f'******   Welcome Kewal Retail   ******\n')
		self.txtarea.insert(END,f'\n Bill Number   : {self.bill_no.get()}')
		self.txtarea.insert(END,f'\n Customer Name : {self.c_name.get()}')
		self.txtarea.insert(END,f'\n Phone Number  : {self.c_phn.get()}')
		self.txtarea.insert(END,f'\n======================================')
		self.txtarea.insert(END,f'\nProducts\t\tQTY\t\tPrice')
		self.txtarea.insert(END,f'\n======================================')

	def bill_area(self):
		if self.c_name.get()=='' or self.c_phn.get()=='':
			messagebox.showerror('Error','Customer Details must be filled')
		elif self.cosmetics_price.get()=='Rs. 0.0' and self.grocery_price.get()=='Rs. 0.0' and self.cold_drink_price.get()=='Rs. 0.0': 	
			messagebox.showerror('Error','No Product has been Purchased')
		else:
			self.welcome_bill()

			#===cosmetic
			if self.soap.get()!=0:
				self.txtarea.insert(END,f'\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}')
			if self.face_cream.get()!=0:
				self.txtarea.insert(END,f'\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}')
			if self.face_wash.get()!=0:
				self.txtarea.insert(END,f'\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}')
			if self.spray.get()!=0:
				self.txtarea.insert(END,f'\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}')
			if self.gell.get()!=0:
				self.txtarea.insert(END,f'\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}')
			if self.loshan.get()!=0:
				self.txtarea.insert(END,f'\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}')

			#===grocery
			if self.rice.get()!=0:
				self.txtarea.insert(END,f'\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}')
			if self.food_oil.get()!=0:
				self.txtarea.insert(END,f'\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}')
			if self.daal.get()!=0:
				self.txtarea.insert(END,f'\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}')
			if self.wheat.get()!=0:
				self.txtarea.insert(END,f'\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}')
			if self.sugar.get()!=0:
				self.txtarea.insert(END,f'\n Sugar\t\t{self.sugar.get()}\t\t{self.g_t_p}')
			if self.tea.get()!=0:
				self.txtarea.insert(END,f'\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}')

			#===cold drinks
			if self.maza.get()!=0:
				self.txtarea.insert(END,f'\n Maza\t\t{self.maza.get()}\t\t{self.g_r_p}')
			if self.coke.get()!=0:
				self.txtarea.insert(END,f'\n Coke\t\t{self.coke.get()}\t\t{self.g_f_p}')
			if self.frooti.get()!=0:
				self.txtarea.insert(END,f'\n Frooti\t\t{self.frooti.get()}\t\t{self.g_d_p}')
			if self.thumbsup.get()!=0:
				self.txtarea.insert(END,f'\n Thumbsup\t\t{self.thumbsup.get()}\t\t{self.g_w_p}')
			if self.limca.get()!=0:
				self.txtarea.insert(END,f'\n Limca\t\t{self.limca.get()}\t\t{self.g_t_p}')
			if self.sprite.get()!=0:
				self.txtarea.insert(END,f'\n Sprite\t\t{self.sprite.get()}\t\t{self.g_t_p}')

			self.txtarea.insert(END,f'\n======================================')
			if self.cosmetics_tax.get()!='Rs. 0.0':
				self.txtarea.insert(END,f'\n Cosmetic Tax\t\t\t{self.cosmetics_tax.get()}') # cosmetic
			if self.grocery_tax.get()!='Rs. 0.0':
				self.txtarea.insert(END,f'\n Grocery Tax\t\t\t{self.grocery_tax.get()}') # grocery
			if self.cold_drink_tax.get()!='Rs. 0.0':
				self.txtarea.insert(END,f'\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}') # cold drink

			self.txtarea.insert(END,f"\n Total Bill :\t\t\tRs. {str(self.Total_bill)}") # total bill
			self.txtarea.insert(END,f'\n======================================')
			self.save_bill()
		
	def save_bill(self):
		op=messagebox.askyesno('Save Bill','Do You Want To Save the Bill?')
		if op>0:
			self.bill_data=self.txtarea.get('1.0',END)
			f1=open('Bills/'+str(self.bill_no.get())+'.txt','w')
			f1.write(self.bill_data)
			f1.close()
			messagebox.showinfo('Saved',f'Bill no : {self.bill_no.get()} saved sucessfully')
		else:
			return

	def find_bill(self):
		present='no'
		for i in os.listdir('Bills/'):
			if i.split('.')[0]==self.search_bill.get():
				f1=open(f'Bills/{i}','r')
				self.txtarea.delete('1.0',END)
				for d in f1:
					self.txtarea.insert(END,d)
				f1.close()
				present='yes'
		if present=='no':
			messagebox.showerror('Error','Invalid Bill Numbers')

	def clear_data(self):
		op=messagebox.askyesno("Clear Data",'Data you have entered will be cleared. Do you want to clear data?')
		if op>0:
			#============================ Cosmetics
			self.soap.set(0)
			self.face_cream.set(0)
			self.face_wash.set(0)
			self.spray.set(0)
			self.gell.set(0)
			self.loshan.set(0)
			
			#============= grocery
			self.rice.set(0)
			self.food_oil.set(0)
			self.daal.set(0)
			self.wheat.set(0)
			self.sugar.set(0)
			self.tea.set(0)

			#================== cold drinks
			self.maza.set(0)
			self.coke.set(0)
			self.frooti.set(0)
			self.thumbsup.set(0)
			self.limca.set(0)
			self.sprite.set(0)

			#============= total product price & tax variable
			self.cosmetics_price.set('')
			self.grocery_price.set('')
			self.cold_drink_price.set('')

			self.cosmetics_tax.set('')
			self.grocery_tax.set('')
			self.cold_drink_tax.set('')

			#====================== Customer
			self.c_name.set('')
			self.c_phn.set('')

			self.bill_no.set('')
			x=random.randint(1000,9999)
			self.bill_no.set(str(x))

			self.search_bill.set('')
			self.welcome_bill()

	def Exit_app(self):
		op=messagebox.askyesno("Exit",'Do you want to Exit ?')
		if op>0:
			self.root.destroy()


root =Tk()
obj = Bill_App(root)
root.mainloop()