

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


np.random.seed(42)
n_samples = 200


# In[4]:


data = pd.DataFrame({
    'Age': np.random.randint(18, 80, n_samples),
    'Billing Amount': np.random.randint(100, 10000, n_samples),
    'Medical Condition': np.random.choice(['Diabetes', 'Hypertension', 'Asthma', 'Healthy'], n_samples)
})


# In[5]:


le = LabelEncoder()
data['Medical Condition Encoded'] = le.fit_transform(data['Medical Condition'])


# In[6]:


features = data[['Age', 'Billing Amount', 'Medical Condition Encoded']]


# In[8]:


scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


# In[ ]:


kmeans = KMeans(n_clusters=4, random_state=42)
clusters = K
