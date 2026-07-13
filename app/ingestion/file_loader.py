from pypdf import PdfReader
from pathlib import Path
from ..utils.utils import compute_file_hash
def pdf_loader(file:Path): #returns each page of a pdf
    source_hash = compute_file_hash(file)
    reader = PdfReader(file)
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        page = {"page": i+1,
                "source":file.name,
                "text":text,
                "source_hash":source_hash
                }
        yield page

def txt_loader(file:Path): #returns all text as single page
    source_hash = compute_file_hash(file)
    with open(file, "r") as f:
        text = f.read()
        page = {"page": 1,
                "source":file.name,
                "text":text,
                "source_hash":source_hash
                }
        yield page


def file_loader(file:Path): #returns each page of different filetypes
    if file.suffix==".pdf":
        yield from pdf_loader(file)
    elif file.suffix==".txt":
        yield from txt_loader(file)
    else:
        print("This filetype is not yet supported:")
        print(file)
    



