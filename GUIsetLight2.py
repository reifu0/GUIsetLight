import tkinter as tk
import sys
import paho.mqtt.client as paho
# install paho>> pip install paho-mqtt


# for mqtt server, 

# below is for using yellow mango router 
broker="192.168.6.210"
LEDlevel = "100"
port=1883
## user , pw> test, no#goodpw


mytransport = 'tcp'

# for fields
fields = 'ID','Encrypt','Size(2 digits)','proto v','Channel', 'Light level(3 digits)', 'Func', 'Sleep/xx', 'sss'
#sfields = 'ID','Channel', 'Light level(3 digits)', 'Func', 'Sleep/xx', 'sss'

##################
## 
## 
##  called when button "Show" is pused. 
###################
def fetch(entries):
    print(" *********    FETCH  ");
    outStr =""
    print("entries")
    print(entries)
    print("============")
#    print(entries[1])
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
 #        text  = entry[4].get()
   
        print('%s: "%s"' % (field, text))
   ##     client1= paho.Client("pyTest")                           #create client object
        client1 = paho.Client(paho.CallbackAPIVersion.VERSION1, client_id="myPy",
                         transport=mytransport,
                         protocol=paho.MQTTv311,
                         clean_session=True)             #create client object paho v2
        client1.username_pw_set("telegraf", "owredi42kdk1Hw")
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)
        cmdString = "55MM110990" + text + "0010XX******* "
        print(cmdString)
        ret= client1.publish("actuator/roomX/no",cmdString)
        outStr = outStr + text
    print(outStr)

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries



def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def sendLEDCmd():
    print(" *****    sendLEDCmd   ****")
#    x1 = entry1.get()
#    channel = entry2.get()
    text  = entries[1].get()
    text  = entries[1][1].get()
#    client1= paho.Client("pyTest")                           #create client object paho v1
    client1 = paho.Client(paho.CallbackAPIVersion.VERSION1, client_id="myPy",
                         transport=mytransport,
                         protocol=paho.MQTTv311,
                         clean_session=True)             #create client object paho v2

    print(channel)
    client1.username_pw_set("telegraf", "owredi42kdk1Hw")
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port)                                 #establish connection
    #ret= client1.publish("house/bulb1","on")                   #publish
    print ('Argument List:', str(sys.argv) )

    cmdString = "55MM11099" + x1 + "0010XX******* "
    print(cmdString)
    ret= client1.publish("actuator/roomX/no",cmdString)



##    if len(sys.argv) == 1:
##        ret= client1.publish("actuator/room1/no",cmdString)                   #publish
##    else:
##        print("arg 2")
##        LEDlevel = str(sys.argv[1])
##        cmdString = "55MM11099" + LEDlevel + "0010XX******* "
##        print(cmdString)
##        ret= client1.publish("actuator/room1/no",cmdString) 

####
### ********************
##  channel, level, 
##
##
##  is sent when "Send to LED stripe"-button is pushed
################
def sendCmd(entries):
    print(" *****    sendCmd   ****")
    outStr =""
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text))
        outStr = outStr + text
        
    print("outStr")
    print(outStr)
##    client1= paho.Client("pyTest")                           #create client object
    client1 = paho.Client(paho.CallbackAPIVersion.VERSION1, client_id="myPy",
                         transport=mytransport,
                         protocol=paho.MQTTv311,
                         clean_session=True)             #create client object paho v2
    client1.username_pw_set("telegraf", "owredi42kdk1Hw")
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port)
#    cmdString = "55MM1109" + outStr + "0010XX*****GI** "
    cmdString = "55MM" + outStr + "0010XX*****GI** "
    print(cmdString)
    ret= client1.publish("actuator/roomX/no",cmdString)



if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    button1 = tk.Button(text='Send to LED stripe', command=(lambda e=ents: sendCmd(e))  )
    button1.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()


 