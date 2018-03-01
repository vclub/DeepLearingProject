
# coding: utf-8

# # 泰坦尼克号数据分析
# 
# ## 1. 介绍
# 
# 泰坦尼克号数据：包括泰坦尼克号上 2224 名乘客和船员中 891 名的人口学数据和乘客基本信息。你可以右键点击 [该链接](https://raw.githubusercontent.com/ShiChJ/DAND-Basic-Materials/master/P2/Project_Files/titanic-data.csv) 选择“另存为”下载。你也可以在 [Kaggle](https://www.kaggle.com/c/titanic/data) 网站上查看这个数据集的详细描述。这个数据集就是来自 Kaggle。
# 
# 
# ## 2. 设置报告

# In[23]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numbers import Number
from scipy import stats

get_ipython().magic('pylab inline')


# ## 3 读取数据

# In[24]:


titanic_df = pd.read_csv('titanic-data.csv')


# ## 4 处理冗余数据
# 
# ### 4.1 初步分析原始数据
# 

# In[25]:


titanic_df.info()


# 原始数据在Age,Cabin,Embarked这三个值中有缺失的数据,下面对Age Embarked数据进行处理,并删除不必要的列

# ### 4.2 缺失的年龄数据处理

# In[26]:


missing_ages = titanic_df[titanic_df['Age'].isnull()]

mean_ages = titanic_df.groupby(['Sex','Pclass'])['Age'].mean()

def remove_na_ages(row):
    if pd.isnull(row['Age']):
        return mean_ages[row['Sex'], row['Pclass']]
    else:
        return row['Age']
    
titanic_df['Age'] = titanic_df.apply(remove_na_ages, axis=1)


# ### 4.3 缺失的出发港数据处理

# In[27]:


missing_ports = titanic_df[titanic_df['Embarked'].isnull()]
missing_ports


# In[28]:


titanic_df[titanic_df['Embarked'].notnull() & ((titanic_df['Ticket'] == '113572') | (titanic_df['Cabin'] == 'B28'))]


# In[29]:


titanic_df['Embarked'].fillna('S', inplace=True)


# ### 4.4 删除不需要的列

# In[30]:


titanic_df = titanic_df.drop(['Cabin','Name','Ticket'], axis=1)
titanic_df.info()


# ### 4.5 值转换
# 
# Survived->Boolean (1=True 0=False)
# 
# Embarked -> C=Cherbourg Q=Queestown S=Southampton
# 

# In[41]:


def map_data(df):
    survived_map = {0:False, 1:True}
    df['SurvivedLabel'] =df['Survived'].map(survived_map)
    
    sex_map = {'male':1, 'female':2}
    df['SexLabel'] = df['Sex'].map(sex_map)
    
    port_map = {'C':'Cherbourg', 'Q':'Queestown','S':'Southampton'}
    df['Embarked']=df['Embarked'].map(port_map)
    
    df['FamilySize'] =df['SibSp'] + df['Parch']
    
    return df

titanic_df = map_data(titanic_df)
titanic_df.head(6)


# 对年龄数据进行分组

# In[32]:


age_labels = ['0-9','10-19', '20-29','30-39','40-49','50-59','60-69','70-79']
titanic_df['age_group'] = pd.cut(titanic_df.Age, range(0,81,10), right=False, labels=age_labels)

titanic_df.head(6)


# In[33]:


titanic_df.describe()


# ## 分析数据
# 
# 从三个方面分析
# 
# 第一个性别
# 
# 第二个舱室级别
# 
# 第三个年龄段
# 

# In[34]:


from matplotlib import pyplot as plt

gp = titanic_df.groupby(["Sex","Survived"])["Survived"].count().unstack().plot(kind="bar",stacked="True")
plt.xlabel('Sex',fontsize=18)
plt.ylabel('Number of people',fontsize=18)
plt.title('Sex and survived')

gp = titanic_df.groupby(["Pclass","Survived"])["Survived"].count().unstack().plot(kind="bar",stacked="True")
plt.xlabel('Ticket class',fontsize=18)
plt.ylabel('Number of people',fontsize=18)
plt.title('Ticket class and survived')

gp = titanic_df.groupby(["FamilySize","Survived"])["Survived"].count().unstack().plot(kind="line",stacked="True")
plt.xlabel('FamilySize',fontsize=18)
plt.ylabel('Number of people',fontsize=18)
plt.title('FamilySize and survived')


# 根据上图分析结果
# 
# 1. 女性的幸存率高于男性
# 
# 2. 船票的级别越高生存率越高（1st class代表高等舱 ）
# 
# 3. 家庭成员越少的生存几率越高

# In[49]:


def correlation(x, y):
    std_x = (x - x.mean())/x.std(ddof=0)
    std_y = (y - x.mean())/y.std(ddof=0)
    
    return (std_x*std_y).mean()

print('性别相关性：%s'%correlation(titanic_df['Survived'],titanic_df['SexLabel']))

print('船票级别相关性：%s'%correlation(titanic_df['Survived'],titanic_df['Pclass']))

#print(correlation(titanic_df['Survived'],titanic_df['Age']))

print('家庭成员相关性：%s'%correlation(titanic_df['Survived'],titanic_df['FamilySize']))


# In[ ]:


说明性别有正向相关性，女性高于男性（这里男性是1女性是2）
船票级别有相关性，程负相关，级别越低，幸存率越低
家庭成员数相关性很小

