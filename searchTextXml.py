class searchtextxml:
    def searchtextxml(filetoseacrh,text):

        import xml.etree.ElementTree as ET

        parsefile = ET.parse(filetoseacrh)

        xmlroot = parsefile.getroot()

        filecontent = []

        for shell_iter in xmlroot.iter('{uri:oozie:shell-action:0.1}file'):
            # print(shell_iter.text)
            if shell_iter.text.endswith('.sh') or shell_iter.text.endswith('.txt') \
                    or shell_iter.text.endswith('.hql'):
                shell_text = shell_iter.text.lower()
                slashindex = shell_text.rfind('/')
                shell_text_wo_slash = shell_text[slashindex + 1:]
                hashindex = shell_text_wo_slash.find('#')
                if hashindex > 0:
                    filecontent.append(shell_text_wo_slash[:hashindex])
                else:
                    filecontent.append(shell_text_wo_slash)

        filecontentwoext = []

        for i in filecontent:
            dotindex = i.find('.')
            filecontentwoext.append(i[:dotindex])

        if text in filecontentwoext:
            return (f"This text {text} is presnt in {filetoseacrh}")

#file=r'C:\Users\bchakra9\OneDrive - JNJ\Desktop\MD\Learning\XML_parse_testing\workflow.xml'
#text=r'atom_comp_calc_set_1'

#message=searchtextxml.searchtextxml(file,text)

#print(message)