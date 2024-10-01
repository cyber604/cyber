import PyPDF2
from docx import Document

def pdf_to_word(pdf_file, word_file):
    """Converts a PDF file to a Word file.

    Args:
        pdf_file (str): The path to the PDF file.
        word_file (str): The path to the output Word file.
    """

    with open(pdf_file, 'rb') as pdf_reader:
        pdf = PyPDF2.PdfReader(pdf_reader)

        document = Document()

        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            text = page.extract_text()

            document.add_paragraph(text)

        document.save(word_file)

if __name__ == '__main__':
    pdf_file = '/home/user/path_to_pdf file/redT-test.pdf'
    word_file = '/home/user/path_to_where the pdf file you want to store/redTea1.docx'

    pdf_to_word(pdf_file, word_file)
