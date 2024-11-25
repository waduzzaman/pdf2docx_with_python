from pdf2docx import Converter

old_pdf = "assignment_1.pdf"
new_docx = "assignment2.docx"

obj = Converter(old_pdf)
obj.convert(new_docx)
obj.close()
