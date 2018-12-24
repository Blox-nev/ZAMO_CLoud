"""
MINI V0
PRODUCTION GRADE 06/11/2018

                                                                *
							       / \
							      /   \
          						     /     \
                                                             -------
                                                     STERM  ->  |
                                                                |
                                                               /|\
                                               BLOX WE DONT WRITE CODE WE GROW CODE




SOURCE:: https://stackoverflow.com/questions/23820286/twisted-portforward-proxy-send-back-data-to-client

SETUP
sudo apt-get install python-twisted

FILE::  STERM.mini.py
V0
"""

from twisted.enterprise import adbapi
import ast
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor
#Convert str to original data type
import ast



print 'STERM ONLINE AND READY'

#==========================================================
#                        DATABASE
# THIS CLASS DOES DATABASE CONNECTION AND BASIC OPERATION.
#                        CLOUD CODE
#==========================================================


# ******A global variable for usr and pw is needed so i can use string formating
#***    |HINT| look at BABY.py DBvalue = [] global variable


#usr = []
#pwd = []

#print usr,pwd

dbpool = adbapi.ConnectionPool("MySQLdb",
                               db = "CLOUD_home_storage",
                               user = "hommey_CLOUD",
                               passwd = "Thulan12",
                               cp_reconnect = True ) # cp_reconnect = True %(usr,pw))




class CLOUD_DATABASE():

    # NOTE comment this and see what happens
    def __init__(self):
        self.DBvalue = []


    #---|ALARM update|

# All cloud Alarm fields will be updated all at once because controll over the
# table is in the hands of the hardware
# The reason behind this is boomareng effect this will help
# determine the hardware state and functionality.


   # db.UPDATE_alarm(Alarm_Name,Alarm_CND,Alarm_OOS,Alarm_SR,Alarm_ID)
    def UPDATE_alarm(self,alm_name,alm_cnd,alm_oos,alm_sr,alm_id):
        query = ("UPDATE Alarm SET AlarmNAME = '%s',AlarmCND = '%s',AlarmOOS = '%s', AlarmSR = '%s'  WHERE id ='%s'" %(alm_name,alm_cnd,alm_oos,alm_sr,alm_id))
        print 'Alarm state updated ]<'
        return dbpool.runQuery(query)


    #---|LIGHTS update|
    #Note: lght_id is default database id that is auto generated
    def UPDATE_lights(self,light_name,on_code,off_code,light_state, light_id):
        query = ("UPDATE Lights SET Name = '%s',OnCode = '%s',OffCode = '%s', State = '%s' WHERE id ='%s'" %(light_name,on_code,off_code,light_state,light_id))
#        print 'Lights state updated  *', ALARMCND,ID
        return dbpool.runQuery(query)


    #---|IRRIGATION update|
    def UPDATE_irrigation(self,irriga_name,irriga_state,irriga_id):
        query = ("UPDATE Irrigation SET Name = '%s', State = '%s' WHERE id ='%s'" %(irriga_name,irriga_state,irriga_id))
#        print 'UPDATE_alarm',
        return dbpool.runQuery(query)


#==========================================================
#                        WEB2PY-RECIEVER
#                  DATA FROM WEB2PY TO CLIENT
#==========================================================

#DATA_FROM_APPLICATION
#class DATA_FROM_APPLICATION(Protocol):



class serverprotocol(Protocol):

#@    def __init__(self, username,password):
#@        self.usr = username
#@        self.pwd = password



    def dataReceived(self,data):

        print data
        #convert string to original data type
        index = ast.literal_eval(data)
        destination_IP = index["NEVIP"]

        print  "\n""\n [Recieved from WEB2PY(TREE-TOP)] got \n" + data
        print destination_IP

        endpoint = TCP4ClientEndpoint(reactor,"%s" % destination_IP ,8001)

        #NOTE: nested function
        def clientProtocol():
            return Clientp(data)

        endpoint.connect(Factory.forProtocol(clientProtocol))

#-----------------------------------------WEB2py SENDER TX----------------------------------

#Without this class Sterm.py wont be able to send data to units
class Clientp(Protocol):

    def __init__(self, dataToSend):
        self.dataToSend = dataToSend

    def connectionMade(self):
        self.transport.write(self.dataToSend)
        self.transport.loseConnection()


##NOTE: comment this out and see what happens
    def dataReceived(self,data):
        print "+ from pi got reply" + data

##NOTE: comment this out and see what happens
print 'RECIVER ONLINE AND READY'


#==========================================================
#                          RPI-RECIEVER
#                  DATA FROM RASPI TO DATABASE
#==========================================================

# new name = HARDWAHRE RECIEVER
class R_serverprotocol(Protocol):

    print 'HARDWARE - RECIEVER UP AND RUNNING :)'

    def dataReceived(self,data):
        #CONVERT STRING TO original data type(string to dic)
        converter = ast.literal_eval(data)


        ALARMS_STATUS = converter['alarm_status']
        LIGHTS_STATUS = converter['light_status']
#        IRRIGATION_STATUS = convert['irrigation_status']

        #CONVERT STRING TO original data (string to turple)
        alarms =  ast.literal_eval(ALARMS_STATUS)
        lights = ast.literal_eval(LIGHTS_STATUS)
#        irrigation = ast.literal_eval(IRRIGATION_STATUS)


        for Alarm_state in alarms:

            Alarm_ID = Alarm_state[0];
            Alarm_Name = Alarm_state[1];
            Alarm_CND = Alarm_state[2];
            Alarm_OOS = Alarm_state[3];
            Alarm_SR = Alarm_state[4];

            print 'Alarm_ID',Alarm_ID
            print 'Alarm_Name',Alarm_Name
            print 'Alarm_CND', Alarm_CND
            print 'Alarm_OOS',Alarm_OOS
            print 'Alarm_SR', Alarm_SR

            #CLOUD ALARM UPDATOR
            #NOTE: This function call has to be the same format as def function
            #      else you will strugle by updating wrong things
            db.UPDATE_alarm(Alarm_Name,Alarm_CND,Alarm_OOS,Alarm_SR,Alarm_ID)











########################################### Resived Names need attension before doing anything Test and see what is what
        for LIGHT_state in lights:

            Light_NAME = LIGHT_state[0];
            Light_ID = LIGHT_state[1]; #Light_off
            Light_ONCODE = LIGHT_state[2];
            Light_OFFCODE = LIGHT_state[3];
            Light_STATE = LIGHT_state[4]; #Light_On

            print'Light-dbid',  Light_NAME
            print'Light-id',Light_ID
            print'Light-name',Light_ONCODE
            print'Light-state',Light_STATE
            print'Light-switch',Light_STATE

            #CLOUD LIGHTS UPDATOR
########---------------------------------------------------THIS IS ARCORDING TO DATA BASE TABLES SHOULD BE OK
            db.UPDATE_lights  (Light_NAME,Light_ONCODE,Light_OFFCODE,Light_STATE,Light_ID)

#######################################################################################________________________________________






#        for IRRIGATION_state in irrigation:
#
#            irrigation_id = IRRIGATION_state[0];
#            irrigation_name = IRRIGATION_state[1];
#            irrigation_state = IRRIGATION_state[2];

#            print 'Irrigation id',irrigation_id
#            print 'Irrigation Name',irrigation_name
#            print 'Irrigation State', irrigation_state

            #CLOUD IRRIGATION UPDATOR
#            db.UPDATE_irrigation(irrigation_name,irrigation_state,irrigation_id)






        #NOTE: nested function
        def clientProtocol():
            return Re_Clientp(data)

#-----------------------------------------CLIENT2---------------------------------
class Re_Clientp(Protocol):

    def __init__(self, dataToSend):
        self.dataToSend = dataToSend  #<<<<<<<<<<<<<<<<<<<<<<<<++=============================|======================|=================|============

    def connectionMade(self):
        self.transport.write(self.dataToSend)
        self.transport.loseConnection()


    def dataReceived(self,data):
        print "+ got reply" + data

#listen for raspi
#reactor.listenTCP(5678,Factory.forProtocol(HARDWARE_RECIEVE))
reactor.listenTCP(5678,Factory.forProtocol(R_serverprotocol))
#listen for App
#reactor.listenTCP(4321,Factory.forProtocol(DATA_FROM_APPLICATION))
reactor.listenTCP(4321,Factory.forProtocol(serverprotocol))

db = CLOUD_DATABASE()
reactor.run()

