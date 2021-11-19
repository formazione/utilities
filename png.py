from PIL import Image
from glob import glob
import os

# ============= create pdf =========

files = glob("*.png")
# rgb.save(PDF_FILE, 'PDF', resoultion=100.0)
for f in files:
    print(f)
    print(f[:-4])
    newname = f[:-4] + ".png"
    print(newname)
    os.rename(f, newname)

files = glob("*.png")
print(files)


iml = []
print(f"{files=}")
for img in files:
    imgs = Image.open(img)
    iml.append(imgs)
pdf = "ALL.pdf"
print(iml)
image = iml[0]
iml.pop(0)
image.save(pdf, "PDF" , resolution=100.0, save_all=True, append_images=iml)

os.system("ALL.pdf")