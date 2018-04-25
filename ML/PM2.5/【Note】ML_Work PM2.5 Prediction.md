# 【Note】ML_Work PM2.5 Prediction
>
>
>
> 2018.04.24
> 

## Task Description
预测A年B月C日N时的PM2.5：

- 测试集中，每个时间点以一个ID表示，共240个时间点；使用测试集中的资料，预测ID时间点下的PM2.5结果，数据给出不同指标在前九个小时下的观测数据；
- 评比标准：预测值和实际值的平方误差平均值；

**预测根据：**前九个小时的所有观测数据：

- A年B月C日N-1时的PM2.5，CH4，No，No2，o3...
- A年B月C日N-2时的PM2.5，CH4，No，No2，o3...
- ...
- A年B月C日N-9时的PM2.5，CH4，No，No2，o3...

**输入数据：**第N个时刻前九个小时的观测数据；

**输出结果：**第N个时刻的PM2.5结果；

## Three Steps of Machine Learning
