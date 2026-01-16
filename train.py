# coding:utf-8
from ultralytics import YOLO

# 加载模型
model = YOLO("yolo11n.pt")  # 加载预训练模型
# Use the model
if __name__ == '__main__':
    # Use the model
    results = model.train(data='E:/FTDetection/dataset/mydata/mydata.yaml',
                          epochs=600,
                          batch=16,
                          patience=100,
                          augment=True,
                          device='0',
                          conf=0.628,
                          # 更精细地学习率策略
                          lr0=0.001,        # 初始学习率
                          lrf=0.01,         # 最终学习率
                          warmup_epochs=5,  # 学习率预热
                          warmup_momentum=0.8,  # 预热动量
                          warmup_bias_lr=0.1,  # 偏置项学习率
                          cos_lr=True,      # 余弦退火
                          # 数据增强
                          hsv_h=0.015,
                          hsv_s=0.7,
                          hsv_v=0.4,
                          degrees=10.0,  # 旋转增强
                          scale=0.5,      # 缩放增强
                          # 提升召回率
                          mosaic=1.0,
                          mixup=0.1,
                          copy_paste=0.1
                          )  # 训练模型
    # 将模型转为onnx格式
    # success = model.export(format='onnx')
