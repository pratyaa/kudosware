import os
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter

for file_name in os.listdir(os.getcwd()):
    if not file_name.endswith(".pdf"):
        continue
    f = open(os.path.join(os.getcwd(), file_name), "rb")
    parser = PDFParser(f)
    # document = PDFDocument(parser, "")

    # if not document.is_extractable:
    #     print("PERMISSION DENIED!!!!")
    #     continue
    
    rsmanager = PDFResourceManager()
    outfile = file_name[:len(file_name)-4]+".txt"
    outfp = open(outfile, 'w', encoding='utf-8')
    laparams = LAParams()
    device = TextConverter(rsmanager, outfp, laparams=laparams,imagewriter=None)
    intrptr = PDFPageInterpreter(rsmanager, device)
    for page in PDFPage.get_pages(f):
        intrptr.process_page(page)
    device.close()
    outfp.close()
    f.close()