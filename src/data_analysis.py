import pandas as pd
df1 = pd.read_csv('./emotion_recorder.csv')
df1.columns = ['num','emotion']
emo_list = df1['emotion'].tolist()


#每隔一个表情加入换行符以便输出
biaoqing = []
for k in range(len(emo_list)):
    biaoqing.append(emo_list[k])
    biaoqing.append('\t')
#最终输出的是字符串的biaoqing
biaoqingfenxi = ''.join(biaoqing)

#定义记录表情变化的次数为emo_change
emo_change = -1
#上一个的表情
pre_emotion = 'nothing'

for k in range(len(emo_list)):
    if(emo_list[k] != pre_emotion):
        emo_change = emo_change + 1
        pre_emotion = emo_list[k]

# 将下标【所在帧的序号】存入各类
# 基础类型
sad = []
anger = []
disgust = []
fear = []
contempt = []
happy = []
surprised = []
neutral = []

# 积极与消极
positive = []
negative = []

# 倾听理解疑惑抵抗
listen = []
understanding = []
confusing = []
resistant = []

for k in range(len(emo_list)):
    if (emo_list[k] == '伤心'):
        sad.append(k)
        confusing.append(k)
        negative.append(k)

    if (emo_list[k] == '发怒'):
        anger.append(k)
        confusing.append(k)
        negative.append(k)

    if (emo_list[k] == '恐惧'):
        fear.append(k)
        resistant.append(k)
        negative.append(k)

    if (emo_list[k] == '厌恶'):
        disgust.append(k)
        resistant.append(k)
        negative.append(k)

    if (emo_list[k] == '开心'):
        happy.append(k)
        understanding.append(k)
        positive.append(k)

    if (emo_list[k] == '惊讶'):
        surprised.append(k)
        understanding.append(k)
        positive.append(k)

    if (emo_list[k] == '中性'):
        neutral.append(k)
        listen.append(k)
        positive.append(k)

    if (emo_list[k] == '鄙夷'):
        contempt.append(k)
        resistant.append(k)
        negative.append(k)

def frametoSec(frame_num):
    sec = frame_num/25
    return sec

switchTiming = []
for positiveFrame in range(len(positive)):
    for negativeFrame in range(len(negative)):
        switchTiming.append(frametoSec(negative[negativeFrame]) - frametoSec(positive[positiveFrame]))
        negativeFrame=negativeFrame+1
        break
    positiveFrame=positiveFrame+1

#定义记录每一帧为积极/消极的数组 EmotionEveryFrame
EmotionEveryFrame = []
for i in range(len(emo_list)):
    if(emo_list[i]=='开心'or emo_list[i]=='中性' or emo_list[i]=='惊讶'):
        EmotionEveryFrame.append(1)
    if(emo_list[i] == '恐惧'or emo_list[i] == '不屑'or emo_list[i] == '厌恶'or emo_list[i] == '发怒'or emo_list[i] == '伤心'):
        EmotionEveryFrame.append(0)
    if(emo_list[i]=='无'):
        EmotionEveryFrame.append(-1)

#switch_timing 存变换的时间
switch_timing = []
#last_emo_type存最后一次上一个类型出现的下标
#emo_type存变换后的类型的下标
last_emo_type = EmotionEveryFrame[0]


#积极/消极表情占比
positive_percentage = len(positive)/len(emo_list)
negative_percentage = len(negative)/len(emo_list)

xueqing = []

xueqing.append("该学生的课堂积极度指数为"+str(positive_percentage)+"\n"+"课堂消极度指数为"+str(negative_percentage))
xueqing.append("\n")
if(positive_percentage>negative_percentage):
    xueqing.append("课堂活跃度良好！")
    xueqing.append("\n")
else:
    xueqing.append("课堂活跃度一般。")
    xueqing.append("\n")


for emo_type in range(len(EmotionEveryFrame)):
     if(EmotionEveryFrame[emo_type] != EmotionEveryFrame[last_emo_type]):
            if(EmotionEveryFrame[emo_type]==-1):
                xueqing.append("学生在" + str(frametoSec(last_emo_type)) + "到" + str(frametoSec(emo_type)) + "没有看向老师")
                xueqing.append('\n')
            if(EmotionEveryFrame[emo_type]==0):
                xueqing.append("学生在"+str(frametoSec(last_emo_type))+"到"+str(frametoSec(emo_type))+"听懂了")
                xueqing.append('\n')
            if(EmotionEveryFrame[emo_type]==1):
                #这里是大于0.1sec就提示太长，可供自行修改
                if((frametoSec(emo_type) - frametoSec(last_emo_type)) > 3):
                    xueqing.append("该学生在"+str(frametoSec(last_emo_type))+"到"+str(frametoSec(emo_type))+"一直没听懂（长时间处于消极状态），教职工应重点关注该学生。")
                    xueqing.append('\n')
                else:
                   xueqing.append("学生在"+str(frametoSec(last_emo_type))+"到"+str(frametoSec(emo_type))+"听不懂")
                   xueqing.append('\n')
            switch_timing.append(frametoSec(emo_type) - frametoSec(last_emo_type))
            last_emo_type = emo_type
#把数组转换为字符串
xueqingfenxi = ''.join(xueqing)





