'''
We are trying to create a script which will check all the files and store the output and then check for specific content

#OS walk function--> Folder name , sub folder name , file name
# Read all the files and get the content
# we can find a specific content as per the need
# module required OS

'''
def filecontectsearch(path,logfile,text):

    import os  # imported OS module

    import logging  # imported logging module

    #import traceback

    logging.basicConfig(filename=logfile, level=logging.DEBUG,filemode='w',format='%(asctime)s -%(levelname)s -%(message)s')
                                # set logging basic parameter

    logging.debug('********************Starting the execution::logging enabled::*************************** ')

    logging.debug(f'Present wokring directory is {os.getcwd()}')

    cwd=path

    os.chdir(cwd)

    logging.debug(f'Changing working directory to {cwd}')

    pwd=os.getcwd()

    logging.debug(f'Working directory changed successfully')

    fileext = ['HQL', 'Q', 'SH', 'PY', 'TXT', 'JSON']

    logging.debug(f'The file extension used in this seacrh are {fileext}')

    numfiles = 0
    logging.debug('intializing the numfiles variable')

    logging.debug(f'Starting the search for {text}')

    for folder_name, subfolder, files in os.walk(pwd): #os walk function to walk through all the folders in the path
        for file in files:
            filepath = os.path.join(folder_name, file) # getting the file path
            filename_txt, filename_ext = os.path.splitext(filepath) # splitiing the extension
            filename_ext = filename_ext[1:].upper() # slicking it to remove '.' like .jar to JAR
            try:
                if filename_ext in fileext: # checking if the file extension valid or not
                    # logging.debug(f'Opening file path {filepath}')
                    readfile = open(filepath) # reading the file
                    content = readfile.readlines()  # reading the content as a list
                    for contenttxt in content: # looping over the content to search
                        if text.lower() in contenttxt.lower(): #converting everything lower to check
                            logging.debug(f'find the file {filepath}')
                            #print()
                            numfiles=numfiles+1 # counting the numvber of files
                            print(filepath)
            except:
                logging.debug(f'This file extenstion {fileext} cannot be opened')

    logging.debug(f'Total number of files found are {numfiles}')

    logging.debug('**********************End of execution******************************************************')

import os

path=r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\MD scripts'

logfile='file_content_seacrh.log'

logfile_path=os.path.join(path,logfile)

text='sc_p_md_wrk.omega_omp_plng_prodloc_Daily_R2_base'

filecontectsearch(path.strip(),logfile_path.strip(),text.strip())