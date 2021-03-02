class xmlfiles:
    def getxmlfiles(filepath):
        import os
        fileslist=[]
        for folder_name, subfolder, files in os.walk(filepath):
            for file in files:
                if file.endswith('.xml'):
                    path = os.path.join(folder_name, file)
                    fileslist.append(path)
        return fileslist





#filepath = r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\MD scripts\atom_d1\ATOM_D1_OOZIE_WF\oozie_wf'

#files=xmlfiles.getxmlfiles(filepath)

#print(files)

