import re

instring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"><soapenv:Body><logonResponse xmlns=\"http://soap.pm.gemalto.com\"><logonReturn>OAxLz6CcDY755dc/BYqzp+LR6+kiKzSfDSTXs0Br5Hjd22JNdKK1mrh8s2gwcKU/OmXp1kBRGW6WdRqjmRmf7KQy4B7AIdWO9PWmwg7186+YFGlLBTxZB7izbj4Vx0pc9fe30WfWgwTkCzCdcnh+In4z/svymzoI0k/P7U5lUUyz/NeSnVQ8xQ==</logonReturn></logonResponse></soapenv:Body></soapenv:Envelope>"



instring2 = '''<?xml version=\"1.0\" encoding=\"UTF-8\"?><soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"><soapenv:Body><executeSynchronousCommandResponse xmlns="http://pm.soap.pm.gemalto.com"><executeSynchronousCommandReturn><ID>104953</ID><endUser>com4LPM</endUser><endingExecutionDate>1497537135636</endingExecutionDate><endingStatus>1</endingStatus><endingStatusLabel>SUCCEEDED</endingStatusLabel><expirationDate>1497538035167</expirationDate><invoker>wsConnector1</invoker><processingDate>0</processingDate><resultData>
&lt;Order
      transactionId=&quot;Transaction1&quot;
      enduser=&quot;com4LPM&quot;&gt;
    &lt;CreateSubscription
          cardProfile=&quot;01.00&quot;
          iccid=&quot;89470900000001193853&quot;
          imsi=&quot;242090000109385&quot;
          initialState=&quot;INACTIVE&quot;
          msisdn=&quot;&quot;&gt;
        &lt;Ota-security&gt;&lt;MBCard serialNumber=&quot;89470900000001193853&quot;&gt;&lt;SecurityDomain defaultSyncID=&quot;default&quot; implicitRcAlgoNumber=&quot;6&quot; proprietaryRcAlgoNumber=&quot;6&quot; securityDomainID=&quot;A0000000030000&quot;&gt;&lt;Sync value=&quot;0000000002&quot;&gt;&lt;/Sync&gt;&lt;Keyset versionNumber=&quot;1&quot;&gt;&lt;Kic algoNumber=&quot;3&quot; value=&quot;FF0A74980D7B281B0F77E5C99FBC738C&quot;&gt;&lt;/Kic&gt;&lt;Kid algoNumber=&quot;3&quot; value=&quot;EB693BCC2F3E779AABFF0FB01A09B1DE&quot;&gt;&lt;/Kid&gt;&lt;/Keyset&gt;&lt;/SecurityDomain&gt;&lt;/MBCard&gt;&lt;/Ota-security&gt;
    &lt;/CreateSubscription&gt;
&lt;/Order&gt;</resultData><serviceName>CreateSubscription</serviceName><state>5</state><stateLabel>TERMINATED</stateLabel><submissionDate>1497537135167</submissionDate><transactionID>Transaction1</transactionID></executeSynchronousCommandReturn></executeSynchronousCommandResponse></soapenv:Body></soapenv:Envelope>'''


def parse2dict(xml_input):
    
    header = 0
    
    tmp_h = ''
    tmp_c = ''
    last = ''
    avp_list = {}
    last_h =''
    appended_h = 0
    waitlock = 0
    for c in xml_input:
        if c == '<':
            header = 1
            if appended_h == 1:
                avp_list[last_h] = tmp_c
                tmp_c = '' 
                appended_h = 0
      
        elif c == '>':
            if waitlock > 0:
                waitlock -=1
            header = 0
            if tmp_h != '':
                last_h = tmp_h
                appended_h = 1
                tmp_h = ''

           
        if header == 1:
            if c == '/' and last == '<':

                waitlock = 1
            if waitlock == 0:
                if c != '<' and c != '>':
                        tmp_h += c
    
        elif header == 0:
            if waitlock == 0:
                if c != '<' and c != '>':
                    tmp_c += c
            else: waitlock=2
        last = c
        
    return avp_list 


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


def strip_newline_tabs(in_string):
    tmp = in_string.replace('\n', ' ')
    tmp2 = in_string.replace(' ', '$')
    tmp2 = replace 
    return tmp2
instringus = strip_newline_tabs(instring2)
smorseparse = utf8_2_ascii(instringus) 
print smorseparse
dictus = parse2dict(smorseparse)
#print dictus['logonReturn']
print dictus.items()
#print '\n'+dictus['cardProfile']
#print dictus.keys()
