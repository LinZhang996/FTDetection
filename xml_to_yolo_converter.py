import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import glob
import cv2
#改成自己的标签，同时该标签顺序对应了转换后YOLO数据集的标签顺序
classes=["grass","leaf","bottle","milk-box","ball","plastic-bag","branch","plastic-garbage"]

def convert(size, box):
    dw = 1.0 /(size[0] + 1)
    dh = 1.0 /(size[1] + 1)
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(image_name,img_path,xml_path,yolo_path):
    in_file = open(xml_path + image_name[:-3] + 'xml') # xml存放路径
    out_file = open(yolo_path + image_name[:-3] + 'txt', 'w') # 转换后的txt文件存放路径
    f = open(xml_path + image_name[:-3] + 'xml') # xml存放路径
    xml_text = f.read()
    root = ET.fromstring(xml_text)
    f.close()
    size = root.find('size')
    img = cv2.imread(os.path.join(img_path,image_name)) # 图片存放路径
    w = img.shape[1]
    h = img.shape[0]
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

if __name__ == '__main__':
    yolo_path='./labels/' # yolo存放路径，会自动创建一个labels的文件夹
    img_path='./images/' # 图片路径
    xml_path='./Annotations/' # xml路径
    os.mkdir(yolo_path) # 标签存放路径
    for image_path in glob.glob(os.path.join(img_path,'*')):
        image_name = image_path.split('\\')[-1]
        print(image_name)
        convert_annotation(image_name,img_path,xml_path,yolo_path)