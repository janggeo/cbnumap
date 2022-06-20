#pip install python-dateutil
from PyPDF2 import PdfFileReader, PdfFileWriter

#����л��� ���� �г����ǽü����̵� pdf
origin = PdfFileReader(open("C:/Users/����ȯ/Downloads/201.pdf", 'rb'))


#pdf����(����л��� ����)�� �ִ� N���� �ǹ���ȣ
#N_building_num=["2","4","5","7","9","10_1","10_2","11","12_1","12_2","13","14","15","16_1","16_2","16_3","18","19","20_1"]
#S_building_num=["1-1","1-2","1-3","1-4","1-5","1-6","1-7","2","4-1","4-2","9","14","20","21-3","21-4","21-5"]
#E_building_num=["1-1~1-2","2","3","3-1","4-3","7-1","7-2","7-3","8-1","8-2","8-3","8-4","8-5","8-6","8-7","8-8","8-10","9","10","12-1","12-2","12-3"]
domi_building_num=["17-4","17-5","17-6","17-2~3","17-1","8-11"]
n_list=[]
#�� �ǹ���ȣ�� ���� pdfFileWriter��ü ���� �� ����Ʈ�� �߰�
for name in domi_building_num:
    name = PdfFileWriter()
    n_list.append(name)
    
# ���� pdf���Ͽ��� ���ϴ� �������� �����ؼ� �� pdfFileWriter��ü�� �߰�
for i, j in zip(range(0,len(domi_building_num)),range(70,76)):
    n_list[i].addPage(origin.getPage(j))

# �� �ǹ��� ���� �� pdf���Ϸ� ����
for name , j in zip(domi_building_num,range(0,len(domi_building_num))):
    n_list[j].write(open("C:/Users/����ȯ/OneDrive/���� ȭ��/map_pdf/domi"+name+".pdf",'wb'))