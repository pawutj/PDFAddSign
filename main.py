# !/usr/bin/python
# Adding a watermark to a multi-page PDF
import PyPDF2
from PIL import Image as PTLImage
from tkinter import *
from tkinter import filedialog
from pathlib import Path
import os
currentPath = os.getcwd()


def addSign(input_file, watermark_file, output_file):

    # input_file = "pdf.pdf"
    # watermark_file = "img.png"
    # output_file = "pdf-drafted.pdf"

    im1 = PTLImage.open(watermark_file)
    background = PTLImage.new('RGBA', im1.size, (255, 255, 255))
    alpha_composite = PTLImage.alpha_composite(background, im1)
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


pdf_filename = []
img_filename = ''


def convert():
    print(pdf_filename, 'pdf name')
    print(img_filename, 'img name')
    for x in pdf_filename:
        print(Path(x).stem)
        addSign(x, img_filename, Path(x).stem+'_sign.pdf')

# Function for opening the
# file explorer window


def browsePDF():
    global pdf_filename
    filename = filedialog.askopenfilename(initialdir=currentPath,
                                          title="Select a PDF",
                                          filetypes=(("PDF",
                                                      "*.pdf*"),
                                                     ("all files",
                                                      "*.*")),
                                          multiple=True
                                          )
    pdf_filename = filename
    print(filename)
    # Change label contents
    #label_file_explorer.configure(text="File Opened: "+filename)


def browseIMG():
    global img_filename
    filename = filedialog.askopenfilename(initialdir=currentPath,
                                          title="Select a IMG",
                                          filetypes=(("IMG",
                                                      "*.png*"),
                                                     ("all files",
                                                      "*.*"))
                                          )
    img_filename = filename
    print(filename)
    # Change label contents
    #label_file_explorer.configure(text="File Opened: "+filename)


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


button_convert = Button(window,
                        text="Convert",
                        command=lambda: convert())

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
button_convert.grid(column=1, row=4)
button_exit.grid(column=1, row=5)

# Let the window wait for any events
window.mainloop()
