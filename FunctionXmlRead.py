def ooziejobtext(filepath,text,logfile):
    import  logging
    from getxmlfiles import xmlfiles
    from searchTextXml import searchtextxml
    logging.basicConfig(filename=logfile, level=logging.DEBUG, filemode='w',
                        format='%(asctime)s -%(levelname)s -%(message)s')
    logging.debug("*********************START*******************************************")
    logging.debug("Calling the function getxmlfiles")
    files=xmlfiles.getxmlfiles(filepath)

    record_count=0
    logging.debug("Looping over the files one by one ")
    for file in files:
        message=searchtextxml.searchtextxml(file,text)
        if bool(message):
            record_count=record_count+1
            print(message)
            logging.debug(message)
    print(f"The text is present in {record_count} files")
    logging.debug(f"The text is present in {record_count} files")
    logging.debug("*********************END*******************************************")
#*******************************************************************************************************

print("Welcome! Search any text within XML files of your directory")

filepath = r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\MD scripts\atom_d1\ATOM_D1_OOZIE_WF\oozie_wf'
logfile=r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\MD scripts\atom_d1\serachoozietext.log'

print(f" The path to seacrh the text is {filepath}")

text=input("Enter the text you want to search:- ")

print("Starting the search for this text")

#text = r'atom_comp_calc_set_1'

ooziejobtext(filepath,text.lower(),logfile)

print(f"Get the detail log in {logfile}")

