
#                        UPDATED 05/11/18
#            ----  HARDWHERECLOUD_HOME_TABLES  ----




#Standalone pydal outside web2py



#from pydal import DAL and Field
from pydal import DAL, Field


#Root user



#DATABASE NAME MIGHT BE WRONG CONFERM<<+++++++++++++++++++NOTE:
#NOTE user Thulani is root use hommey | password is Thulan12
##########################################db = DAL('mysql://Thulani:Neoblox@localhost/CLOUD_home_storage')
db = DAL('mysql://hommey_CLOUD:Thulan12@localhost/CLOUD_home_storage')
   #use root#msql://user:password@localhost/database



#HARDWHERE_CLOUD_home tables


#---------Cloud_IP addres
#stores cloud IP
db.define_table('IP',
   Field('NevIP','string'),
   Field('CloudIP','string')
   )


#----------Alarm
#motion sensors = 1/0
#panic button = 1/0
db.define_table('Alarm',
   Field('AlarmNAME','string'),
   Field('AlarmCND', 'integer'),
   Field('AlarmOOS','integer'),
   Field('AlarmSR', 'integer')
   )


#-----------Lights
#state from payload = 1/0
#feedback from switches = on/off
db.define_table('Lights',
   Field('Name','string'),
   Field('OnCode','string'),
   Field('OffCode','string'),
   Field('State','string')
   )


#--------Irrigation
#feedback will be the result of the database state 1=on 0=off
#need a python script to monitor irrigation state changes
db.define_table('Irrigation',
   Field('Name','string'),
   Field('state','string')
   )

#-------Plugs
#This is for future use when i have RF plugs
#need a python script to monitor plugs state changes
db.define_table('Plugs',
   Field('Plug_Name','string'),
   Field('Plug_Onbin','string'),
   Field('Plug_Offbin','string'),
   Field('Plug_State','string')
   )







#*-----------------------------------------------------------------------------------------------------------------LATER
#-------Curtain
#This is for future use when i have RF curtain
#need a python script to monitor curtain state changes
db.define_table('Curtain',
   Field('Name','string'),
   Field('onbin','string'),
   Field('offbin','string'),
   Field('state','string')
   )

#--------Remote Control
#RF gate
#RF Aircon
#anything RF and TVs RADIOs goes in here
db.define_table('Rf_signal',
   Field('Name','string'),
   Field('code','string')
   )
#*-----------------------------------------------------------------------------------------------------------------------|





#---------Cam_ip addres
#stores camera IP
db.define_table('Cam_ip',
   Field('Name','string'),
   Field('IP','string')
   )

#---------Motivation
#This is subscrition and is valid for 35 days
#i use a python script that reads payload activ variable
#and update Activator to 1 counts down and update
#Activator back to 0 when time laps

db.define_table('Motivation',
   Field('Activator','string')
   )


