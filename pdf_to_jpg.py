import os
from pdf2image import convert_from_path

#�� pdf������ jpg�� ��ȯ(folium�� popup�� ��������)
file_list = os.listdir("C:/Users/����ȯ/OneDrive/���� ȭ��/map_pdf/")

for name in file_list:
    pages=convert_from_path("C:/Users/����ȯ/OneDrive/���� ȭ��/map_pdf/"+name, size = (650,650))
    for i, page in enumerate(pages):
        page.save("C:/Users/����ȯ/OneDrive/���� ȭ��/map_img/"+name.strip(".pdf")+".jpg","JPEG")