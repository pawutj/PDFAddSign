# !/usr/bin/python
# Adding a watermark to a multi-page PDF
import PyPDF2
from PIL import Image
from tkinter import *
from tkinter import filedialog

import os
currentPath = os.getcwd()


def addSign():

    input_file = "pdf.pdf"
    watermark_file = "img.png"
    output_file = "pdf-drafted.pdf"

    im1 = Image.open(watermark_file)
    background = Image.new('RGBA', im1.size, (255, 255, 255))
    alpha_composite = Image.alpha_composite(background, im1)
    alpha_composite = alpha_composite.convert('RGB')

    alpha_composite.save('_pdf.pdf', "PDF", resolution=100.0)

    in_pdf = PyPDF2.PdfFileReader(input_file)
    sign_pdf = PyPDF2.PdfFileReader('_pdf.pdf').getPage(0)

    in_page = in_pdf.getPage(0)
    in_page.mergeScaledTranslatedPage(sign_pdf, 0.1,
                                      0, 0)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(in_pdf.getPage(0))
    with open(output_file, 'wb') as out_file:
        writer.write(out_file)


def Convert():
    print('Button bind working!')


# Function for opening the
# file explorer window
def browsePDF():
    filename = filedialog.askopenfilename(initialdir=currentPath,
                                          title="Select a PDF",
                                          filetypes=(("PDF",
                                                      "*.pdf*"),
                                                     ("all files",
                                                      "*.*"))
                                          )

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)


def browseIMG():
    filename = filedialog.askopenfilename(initialdir=currentPath,
                                          title="Select a IMG",
                                          filetypes=(("IMG",
                                                      "*.png*"),
                                                     ("all files",
                                                      "*.*"))
                                          )

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)


# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")


button_explore_1 = Button(window,
                          text="Browse PDF",
                          command=browsePDF)

button_explore_2 = Button(window,
                          text="Browse Sign",
                          command=browseIMG)


button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_explore_1.grid(column=1, row=2)
button_explore_2.grid(column=1, row=3)
button_exit.grid(column=1, row=4)

# Let the window wait for any events
window.mainloop()
