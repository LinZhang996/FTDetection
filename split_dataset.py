import os
import shutil
import random
from tqdm import tqdm


def split_img(root_path, img_path, label_path, split_list):
    try:  # 创建数据集文件夹
        Data = root_path
        os.mkdir(Data)
        train_img_dir = Data + '/images/train'
        val_img_dir = Data + '/images/val'
        test_img_dir = Data + '/images/test'  # 新增测试集
        train_label_dir = Data + '/labels/train'
        val_label_dir = Data + '/labels/val'
        test_label_dir = Data + '/labels/test'  # 新增测试集
        # 创建文件夹
        os.makedirs(train_img_dir)
        os.makedirs(train_label_dir)
        os.makedirs(val_img_dir)
        os.makedirs(val_label_dir)
        os.makedirs(test_img_dir)  # 新增测试集
        os.makedirs(test_label_dir)  # 新增测试集
    except:
        print('文件目录已存在')

    train, val, test = split_list  # 修改为三个比例
    all_img = os.listdir(img_path)
    all_img_path = [os.path.join(img_path, img) for img in all_img]

    # 随机打乱
    random.shuffle(all_img_path)
    total = len(all_img_path)

    # 计算各集合数量
    train_count = int(total * train)
    val_count = int(total * val)

    train_img = all_img_path[:train_count]
    val_img = all_img_path[train_count:train_count + val_count]
    test_img = all_img_path[train_count + val_count:]  # 剩余作为测试集

    train_img_copy = [os.path.join(train_img_dir, img.split('\\')[-1]) for img in train_img]
    train_label = [toLabelPath(img, label_path) for img in train_img]
    train_label_copy = [os.path.join(train_label_dir, label.split('\\')[-1]) for label in train_label]

    for i in tqdm(range(len(train_img)), desc='train', ncols=80, unit='img'):
        _copy(train_img[i], train_img_dir)
        _copy(train_label[i], train_label_dir)

    val_img_copy = [os.path.join(val_img_dir, img.split('\\')[-1]) for img in val_img]
    val_label = [toLabelPath(img, label_path) for img in val_img]
    val_label_copy = [os.path.join(val_label_dir, label.split('\\')[-1]) for label in val_label]

    for i in tqdm(range(len(val_img)), desc='val', ncols=80, unit='img'):
        _copy(val_img[i], val_img_dir)
        _copy(val_label[i], val_label_dir)

    test_img_copy = [os.path.join(test_img_dir, img.split('\\')[-1]) for img in test_img]  # 新增测试集
    test_label = [toLabelPath(img, label_path) for img in test_img]  # 新增测试集
    test_label_copy = [os.path.join(test_label_dir, label.split('\\')[-1]) for label in test_label]  # 新增测试集

    for i in tqdm(range(len(test_img)), desc='test', ncols=80, unit='img'):  # 新增测试集
        _copy(test_img[i], test_img_dir)
        _copy(test_label[i], test_label_dir)


def _copy(from_path, to_path):
    shutil.copy(from_path, to_path)


def toLabelPath(img_path, label_path):
    img = img_path.split('\\')[-1]
    if '.jpg' in img:
        label = img.split('.jpg')[0] + '.txt'
    # elif:
    #     label = img.split('.JPG')[0] + '.txt'
    else:
        label = img.split('.png')[0] + '.txt'
    return os.path.join(label_path, label)


if __name__ == '__main__':
    img_path = './images'  # 图片路径
    label_path = './labels'  # yolo标签路径
    root_path = './mydata'  # 数据集文件名
    split_list = [0.7, 0.2, 0.1]  # 修改为 7:2:1 比例 [train:val:test]
    # split_list = [2000/2400, 350/2400, 50/2400]  # 修改为 2000:350:50 比例 [train:val:test]
    split_img(root_path, img_path, label_path, split_list)