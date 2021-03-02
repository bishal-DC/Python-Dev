import re,os

import pandas as pd

pd.options.display.max_rows=200
pd.options.display.max_colwidth=300

scriptpath=r'D:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\MD scripts\Table_omega_reports'

listoffilename=os.listdir(scriptpath)

listofdfs=[]

for filename in listoffilename:
    filepath=os.path.join(scriptpath,filename)
    fileopen=open(filepath)
    filecontent=fileopen.read()
    content_regex=re.compile('sc_[A-Za-z_]+\.[A-Za-z0-9_]+',re.IGNORECASE)
    v_table_name='table'+str(listoffilename.index(filename))
    v_table_name=list(set(content_regex.findall(filecontent)))
    dfname='df'+str(listoffilename.index(filename))
    dfname=pd.DataFrame(data=tables,columns=['table_used'])
    dfname.insert(loc=0,column='Script_Name',value=filename)
    listofdfs.append(dfname)
    fileopen.close()
fileopen.close()
combine_df=pd.concat(listofdfs,ignore_index=True)
combine_df

os.chdir(r'D:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\Omega')
combine_df.to_excel('Omega_Report_tables_list.xlsx',index=False)
