"""
 构建CNN模型
"""
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dropout, BatchNormalization, Flatten, Dense, AveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.layers import PReLU


def CNN3(input_shape=(48, 48, 1), n_classes=8):
    """
    参考论文实现
    A Compact Deep Learning Model for Robust Facial Expression Recognition
    :param input_shape:
    :param n_classes:
    :return:
    """
    # input
    #第一层输入层
    input_layer = Input(shape=input_shape)
    x = Conv2D(32, (1, 1), strides=1, padding='same', activation='relu')(input_layer)
    #以边缘来填充，每一步走一个像素点
    # block1
    x = Conv2D(64, (3, 3), strides=1, padding='same')(x)
    x = PReLU()(x)
    x = Conv2D(64, (5, 5), strides=1, padding='same')(x)
    x = PReLU()(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    #最大池化
    # block2
    x = Conv2D(64, (3, 3), strides=1, padding='same')(x)
    #prelu是activation function，带参数的relu方程
    x = PReLU()(x)
    x = Conv2D(64, (5, 5), strides=1, padding='same')(x)
    x = PReLU()(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    # fc全连接层
    x = Flatten()(x)
    x = Dense(2048, activation='relu')(x)
    #dropout防止过拟合
    x = Dropout(0.5)(x)
    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(n_classes, activation='softmax')(x)

    model = Model(inputs=input_layer, outputs=x)
    return model
