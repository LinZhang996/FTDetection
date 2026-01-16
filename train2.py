# coding:utf-8
from ultralytics import YOLO

# 加载模型
model = YOLO("yolo11n.pt")  # 加载预训练模型
# Use the model
if __name__ == '__main__':
    # Use the model
    results = model.train(data='E:/FTDetection/dataset/mydata/mydata.yaml',
                          device='0',
                          conf=0.5,
                          lr0=0.001,
                          epochs=200,
                          # 数据增强
                          augment=True,
                          mixup=0.1,
                          cutmix=0.1,
                          # 损失权重
                          box=8.5,
                          cls=0.8,
                          cos_lr=True
                          )  # 训练模型
    # 将模型转为onnx格式
    # success = model.export(format='onnx')
