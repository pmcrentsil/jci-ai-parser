import fitz
from PIL import Image
import io

def crop_diagram(pdf_path, page_num, polygon, padding=20):
    doc = fitz.open(pdf_path)
    page = doc[page_num - 1]
    pix = page.get_pixmap(dpi=300)
    img = Image.open(io.BytesIO(pix.tobytes()))

    x_coords = [pt[0] for pt in polygon]
    y_coords = [pt[1] for pt in polygon]
    x0 = max(min(x_coords) - padding, 0)
    x1 = min(max(x_coords) + padding, img.width)
    y0 = max(min(y_coords) - padding, 0)
    y1 = min(max(y_coords) + padding, img.height)

    return img.crop((x0, y0, x1, y1))
