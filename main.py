# !/usr/bin/python
# Adding a watermark to a multi-page PDF
import PyPDF2
from PIL import Image

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
