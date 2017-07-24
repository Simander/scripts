import re
#Tool for parsing UTF-8 to correct ASCII
#replace (&quot;) with ("), (&amp;apos;) with ('), (&lt;) with (<) and (&gt;) with (>)
def utf8_2_ascii(input):
    output = ''
    tmp = input.replace('&quot;', '\"')
    output = tmp
    tmp = output.replace('&amp;apos;', '\'')
    output = tmp
    tmp = output.replace('&lt;', '<')
    output = tmp
    tmp = output.replace('&gt;', '>')
    output = tmp
    return output

#Class representing an Attribute Value Pair
class Avp:
    def __init__(self, a, v):
        self.a = a
        self.v = v

#Class representing a list of Attribute Value Pairs
class Avp_list:
    def __init__(self):
        self.avp_list = []

    def add_avp(self, a, v):
        tmp_avp = Avp(a, v)
        self.avp_list.append(tmp_avp)

    def val(self, a):
        for i in range(0, len(self.avp_list)):
            if self.avp_list[i].a == a:
                return self.avp_list[i].v
    def keys(self):
        print "blob"
        output = 'Keys:\n'
        for i in self.avp_list:
            output+= i+'\n'
        return output

    def printall(self):
        for e in self.avp_list:
            print e

#Class representing an  XML tag
class Tag:
    def __init__(self, name=''):
        self.name = name
        self.avps = Avp_list()
        self.value = ''
    def append_name(self, c):
        self.name+= c
    def append_value(self, c):
        self.value += c
    def add_name(self, name):
        self.name = name
    def add_avp(self, a, v):
        self.avps.add_avp(a,v)

    def val(self, a):
        return self.avps.val(a)
    def get_avps(self):
        output = 'Attributes:\n'
        if self.avps != None:
            for i in self:
                if []:
                    output += i.name+', '+i.value+'\n'
        return output
    def keys(self):
        self.avps.keys();
    def add_value(self, value):
        self.value = value

#Class representing a list of XML tags
class TagList:
    def __init__(self):
        self.lista = []

    def add(self, tag):
        self.lista.append(tag)

    def val(self, attributename):
        for i in self.lista:
            if i.name == attributename:
                return i.value
        else:
            for i in self.lista:
                if i.avps != None:
                    kavps = i.avps
                    tmp_attrib = kavps.val(attributename)
                    if tmp_attrib != None:
                        return tmp_attrib
            return None
          
    def values(self):
        #print 'Len: '+str(len(self.lista))
        for i in self.lista:
            #if i.value == '':
             #   print None
            #else:
            print i.value
    def keys(self):
        output = ''
       # print 'Len: ' + str(len(self.lista))
        #inr = 0
        for i in self.lista:

      #      if i.name != '':
       #         output += i.name+'\n'
        #        inr += 1

            output += i.name+'\n'

        print output
    def avps1(self):
        for i in self.lista:
            i.get_avps()

#1 = start, 2 = stop, 0 = none
def parser(text):
    xml_header =Tag()
    FLAG_header = 0 # HEADER-TAG(start) = 1, HEADER-TAG(end) = 2
    FLAG_start = 0  # START-TAG(start) = 1, START-TAG(end) = 2
    FLAG_end = 0    # END-TAG(start) = 1, END-TAG(end) = 2
    FLAG_avps = 0   #
    tags = TagList() #Holds a list of tags from the xml file
    tmp_a = ''
    tmp_v = ''
    tmp_inside = ''
    tmp_tag = Tag()
    for i in range(1, len(text)):

        #start of END-TAG
        if text[i] == '<' and text[i] == '/':

            FLAG_end = 1
        #start of HEADER-TAG
        elif text[i-2] == '<' and text[i-1] == '?':
            FLAG_header = 1
        #end of HEADER-TAG
        elif text[i] == '?' and text[i+1] == '>':
            FLAG_header = 2
         #   FLAG_end = 0
        #start of START-TAG
        elif text[i-1] == '<' and text[i] != '?' and text[i] != '/':
            FLAG_start = 1
            FLAG_skip = 0
            FLAG_header = 0
            #FLAG_end = 1

        #end of TAG
        elif text[i-1] == '>' and text[i-1] != '?':
            FLAG_start = 2



        elif text[i] == ' ' and FLAG_start == 1:
            FLAG_avps = 1
        #if FLAG_end != 1:
        if FLAG_header == 1:
            xml_header.append_value(text[i])
        elif FLAG_header == 2:
            xml_header.name = 'header'
            tags.add(xml_header)
            FLAG_header = -1

        if FLAG_start == 1:
            # START-TAG name
            if FLAG_avps == 0:
                if text[i] != ' ' and text[i] != '/' and text[i] != '>':
                    tmp_tag.append_name(text[i])

            elif FLAG_avps == 2 and text[i] == '\"' and text[i+1] == ' ' or text[i+1] =='>':
                if tmp_v == '':
                    tmp_v = None
                tmp_tag.add_avp(tmp_a, tmp_v)
                #print 'att:'+tmp_a
                #print 'val:'+tmp_v
                tmp_a = tmp_v = ''
                if text[i+1] == '>':
                    #tags.append(tmp_tag)
                   # tmp_tag = Tag()
                    FLAG_avps = 0
                else:
                    FLAG_avps = 1

            elif FLAG_avps == 2:
                if text[i] != '\"' and text[i]:
                    tmp_v += text[i]
            else:
                if text[i] != '=' and text[i] != ' ' and text[i] != '/':
                    tmp_a+= text[i]
                elif text[i] == '=':
                    FLAG_avps = 2


        elif FLAG_start == 2: #AFTER START-TAG
            if text[i] != '<' and text[i] != '>':
                tmp_inside+=text[i]
            else:
                if tmp_inside != '':
                    tmp_tag.value = tmp_inside
                else:
                    tmp_tag.value = None
                tmp_inside = ''

                if FLAG_end != 1:
                    if tmp_tag.name != '':
                        tags.add(tmp_tag) #Adds Tag to Tag-List
                    tmp_tag = Tag() #RESET TMP TAG
                    FLAG_start = 0

    return tags #Return Tag-List


#Prepares an xml string
def prepareXML(input):
  ascii_xml_string = utf8_2_ascii(input)
  replace_newline_chars = ascii_xml_string.replace('\n', ' ')
  new_string = re.sub(' +', ' ', replace_newline_chars)
  return new_string
#Tag object = parser(prepared_string)
tag = parser(prepared_string)
print tagz.val('endUser')
print tagz.val('iccid')
print tagz.val('imsi')
print tagz.val('endingStatusLabel')
print tagz.val('msisdn')
