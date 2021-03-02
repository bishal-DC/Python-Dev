#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os,pandas as pd,json,re


# In[ ]:


#os.chdir(r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\MD_config_test2')
os.chdir(r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\MD Configs\Pangea')


# In[ ]:


#path=r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\MD_config_test2'
path=r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\MD Configs\Pangea'


# In[ ]:


files=[]

for i in os.listdir(path):
    if i.endswith('.json'):
        files.append(i)

files


# In[ ]:


listofdfs=[]
for file in files:
    filepath=os.path.join(path,file)
    with open (filepath,"r") as read:
        content=json.load(read)
        content.setdefault("functional_area","NA")
        dfname='df'+str(files.index(file))
        dfname=pd.DataFrame(data=content["tables"])
        dfname.insert(loc=0,column="SLT_ID",value=content["SLT_ID"])
        dfname.insert(loc=1, column="PARENT_TASK_ID", value=content["parent_task"])
        dfname.insert(loc=2, column="TASK_ID", value=content["TASK_ID"])
        dfname.insert(loc=3, column="FUNCTIONAL_AREA", value=content["functional_area"])
        dfname.insert(loc=4, column="FILE_NAME", value=file)
        listofdfs.append(dfname)
        read.close()


# In[ ]:


combine_df=pd.concat(listofdfs,ignore_index=True)
combine_df


# In[ ]:


pd.set_option('display.max_rows',202)


# In[ ]:


combine_df


# In[ ]:


combine_df.rename(columns={"parquet_file": "SOURCE_FILE"},inplace=True)


# In[ ]:


combine_df.rename(columns={"FILE_NAME": "CONFIG_FILE"},inplace=True)


# In[ ]:


combine_df.columns


# In[ ]:





# In[ ]:





# In[ ]:


combine_df.tsv_file.fillna("NA",inplace=True)


# In[ ]:


combine_df.table_name.fillna("NA",inplace=True)


# In[ ]:


import numpy as np


# In[ ]:


combine_df["source_type"]=np.where(combine_df.tsv_file.str.contains('GDM'),'GDM',combine_df.source_type)


# In[ ]:


combine_df["type"]=np.where(combine_df.table_name.str.contains('gdm'),'gdm',combine_df.type)


# In[ ]:


combine_df.loc[combine_df["source_type"]=='project_one']


# In[ ]:


combine_df["FUNCTIONAL_AREA"]=np.where(combine_df["type"]=='gdm','GDM',combine_df.FUNCTIONAL_AREA)


# In[ ]:


combine_df


# In[ ]:


combine_df.SOURCE_FILE.fillna('NA',inplace=True)


# In[ ]:


combine_df["SOURCE_FILE"]=np.where(combine_df["SOURCE_FILE"]=='NA',combine_df["tsv_file"],combine_df["SOURCE_FILE"])


# In[ ]:


df=combine_df.iloc[:,:8]


# In[ ]:


os.chdir(r'C:\Users\bchakra9\OneDrive - JNJ\Desktop')


# In[ ]:


df.to_excel('Pangea_configs.xlsx',index=False)


# In[ ]:




