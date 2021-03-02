"""
This script will check specific file content in specific path
#For better result the search text has to be specific
#Useful to search any script location or table name easily
#OS walk function--> Folder name , sub folder name , file name
# Read all the files and get the content
# we can find a specific content as per the need
# Module required OS,logging

"""


def filecontectsearch(path, logfile, text):
    import os  # imported OS module

    import logging  # imported logging module

    import  re

    # import traceback

    logging.basicConfig(filename=logfile, level=logging.DEBUG, filemode='w',
                        format='%(asctime)s -%(levelname)s -%(message)s')
    # set logging basic parameter

    logging.debug('********************Starting the execution::logging enabled::*************************** ')

    logging.debug(f'Present wokring directory is {os.getcwd()}')

    cwd = path

    os.chdir(cwd)

    logging.debug(f'Changing working directory to {cwd}')

    pwd = os.getcwd()

    logging.debug(f'Working directory changed successfully')

    fileext = ['HQL', 'Q', 'SH', 'PY', 'TXT', 'JSON']

    logging.debug(f'The file extension used in this seacrh are {fileext}')

    numfiles = 0
    logging.debug('intializing the numfiles variable')

    logging.debug(f'Starting the search for {text}')

    for folder_name, subfolder, files in os.walk(pwd):  # os walk function to walk through all the folders in the path
        for file in files:
            filepath = os.path.join(folder_name, file)  # getting the file path
            filename_txt, filename_ext = os.path.splitext(filepath)  # splitiing the extension
            filename_ext = filename_ext[1:].upper()  # slicking it to remove '.' like .jar to JAR
            try:
                if filename_ext in fileext:  # checking if the file extension valid or not
                    # logging.debug(f'Opening file path {filepath}')
                    readfile = open(filepath)  # reading the file
                    content = readfile.read()  # reading the content
                    #for contenttxt in content:  # looping over the content to search
                    content_regex = re.compile(f'insert.*\.{text}',re.IGNORECASE)
                        #print(content_regex)
                    contentmatch_bool = bool(content_regex.findall(content))
                        #print(contentmatch)
                    contentmatch = content_regex.findall(content)
                    if contentmatch_bool == True:  # converting everything lower to check
                        logging.debug(f'find the file content in  {filepath}')
                        logging.debug(f'The content looks like {contentmatch}')
                        numfiles = numfiles + 1  # counting the numvber of files
                        print(f'The file path is\n {filepath}')

                        print(f'The content looks like\n {contentmatch}')

                        #return filepath,contentmatch
            except:
                logging.debug(f'This file extenstion {fileext} cannot be opened')

    logging.debug(f'Total number of files found are {numfiles}')

    logging.debug('**********************End of execution******************************************************')


import os

path = r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD'
logfile = 'file_content_seacrh.log'
logfile_path=os.path.join(path,logfile)
text = 'sc_p_md_wrk.omega_omp_plng_prodloc_Daily_R2_base'

#filepath,contentmatch=\
filecontectsearch(path.strip(), logfile_path.strip(), text.strip())

#print(f'The file path is\n {filepath}')

#print(f'The content looks like\n {contentmatch}')