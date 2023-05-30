import os
from PyPDF2 import PdfMerger

source_dir = r"C:\Users\Mittesh Waghule\Desktop\pdf_r"
# merger = PyPDF2.PdfMerger() (This is an old method and is changed now to PdfMerger)
merger = PdfMerger()

for item in os.listdir(source_dir):
    if item.endswith("pdf"):
        merger.append(os.path.join(source_dir, item))

output_path = os.path.join(source_dir, "Complete_4.pdf")
merger.write(output_path)
merger.close()