#! /usr/bin/python3

import time
import os
from PyPDF2 import PdfFileMerger
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

bgcolor = '#3080c0'



class PDFMergeGui():
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("PDF Merge")
		#self.window['background']=bgcolor
		self.window.geometry("800x250")
		self.create_widgets()
		self.files=[]
		self.output_file = '' 
		self.window_text= ''

	def open_dialog(self):
		
		local_files= fd.askopenfilenames(parent = self.window, title='Choose a file', filetypes = ( ('All Files', '*.*'), ('PDF Files', '*.pdf')) )
		for f in local_files:
			self.files.append(f)
			#print(f)
		
		# debug check appended files
		print('\n'*2)
		for f in self.files:
			print(f)

	def merge_pdf(self):


		if not self.files:
			self.display_files()
			return 0
	
		merge = PdfFileMerger()
		ext = '.pdf'
		
		#iterate thru list and make pdf file
		for pdf in self.files:
			if(pdf.endswith(ext) ):
				merge.append(open(pdf, 'rb'))
			else:
				print("Error: %s is not a pdf", pdf)
		# write pdf files to disk	

		with open(self.output_file, 'wb') as fout:
			merge.write(fout)

		print("%s Saved to File.")


	def list2string(self):
		str_ = []
		for i in self.files:
			str_.append(i.split('/')[-1])
		return '\n'.join(str_)


	def enumerate_list(self, files, switch_frame_):
		checkbutton_list = []
		for c in range(len(files)):
			checkbutton_list.append(ttk.Checkbutton(switch_frame_, text=files[c].split('/')[-1]) )
			checkbutton_list[c].grid(row=c, column=1, sticky=tk.E + tk.W + tk.N + tk.S)
			
		return checkbutton_list
		

	def display_files(self):

		window_checkbutton = tk.Toplevel()
		switch_frame = ttk.LabelFrame(window_checkbutton, text="Files Selected:", relief=tk.RIDGE, padding=6)
		switch_frame.grid(row=1, column=2, padx=6, sticky=tk.E + tk.W + tk.N + tk.S)
		
		#checkbox_label = ttk.Label(switch_frame, text="Checkbuttons")
		#checkbox_label.grid(row=1, rowspan=3, column=1, sticky=tk.W + tk.N)
		        
		if not self.files:
			window_text = "No Files Selected"
			label = tk.Label(switch_frame, text= window_text)
			label.pack(fill='x', padx=50, pady=5)
		else:
			#window_text = self.list2string()
			ret_files = self.enumerate_list(self.files, switch_frame)

			for f in ret_files:
				print(f.state())
		
		
		
		button_close= tk.Button(window_checkbutton, text="close", command= window_checkbutton.destroy)
		button_close.grid(row=2,column = 2, sticky=tk.E + tk.W + tk.N + tk.S) 


	
	def delete_files(self):
		self.files=[]
		
	def create_widgets(self):
		# Create some room around all the internal frames
		button_padx = 0
		button_pady = 2
		
		cmd_frame = tk.LabelFrame(self.window, text="Select Files", relief=tk.RIDGE)
		cmd_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)
		

		
		select_files_button = tk.Button(cmd_frame, text="Select Files", command = self.open_dialog)
		select_files_button.grid(row=1, column = 1, sticky=tk.W, pady=button_pady, padx = button_padx)

		review_files_button = tk.Button(cmd_frame, text="Review Files", command = self.display_files)
		review_files_button.grid(row=1, column = 2, sticky=tk.W, pady=0, padx = 2)

		
		delete_files_button = tk.Button(cmd_frame, text="Delete Files", command = self.delete_files)
		delete_files_button.grid(row=1, column = 3, sticky=tk.W, pady=0, padx = 2)


		# text entry to save output file
		save_files_label = tk.Label(cmd_frame, text="Save File As:")
		save_files_label.grid(row=3, column=1, sticky=tk.W + tk.N)
	
		self.output_file = time.strftime("Merged_Form_%m-%d-%Y.pdf")
		
		my_entry = ttk.Entry(cmd_frame, width=50)
		my_entry.grid(row=3, column=2, sticky=tk.W, padx = 3, pady=3)
		my_entry.insert(tk.END, self.output_file)
		
		#Button to create pdf 
		make_pdf_button = tk.Button(cmd_frame, text="Make PDF", command = self.merge_pdf)
		make_pdf_button.grid(row = 4, column = 1, pady=button_pady, padx = button_padx )
		
		# Quit button in the lower right corner
		quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy)
		quit_button.grid(row=1, column=3)

		

#Create Gui
program = PDFMergeGui()

#Start Event loop
program.window.mainloop()


