import time
import datetime
from plyer import notification
if __name__=="__main__":
        a=int(datetime.datetime.now().hour)
        if(a>6 and a<7):
                notification.notify(
                title ="Exercise Time",
                message="activity requiring physical effort, carried out to sustain or improve health and fitness.",
                app_icon="D:\Chrome\excercise.ico.ico",
                timeout=2
                )
        elif(a>7 and a<8):
                notification.notify(
                title ="Breakfast Time",
                message="Breakfast is the first meal of the day eaten after waking up, usually in the morning. The word in English refers to breaking the fasting period of the previous night",
                app_icon="D:\Chrome\breakfast.ico.ico",
                timeout=2
                )
        elif(a>8 and a<9):
                notification.notify(
                title ="Dress Management",
                message="Decorate (something) in an artistic or attractive way.",
                app_icon="D:\Chrome\icon.ico.ico",
                timeout=2
                )
        elif(a>12 and a<13):
                notification.notify(
                title ="Lunch Time",
                message="A meal eaten in the middle of the day, typically one that is lighter or less formal than an evening meal.",
                app_icon="D:\Chrome\lunch.ico.ico",
                timeout=2
                )
        elif(a>16 and a<17):
                notification.notify(
                title ="Snack Time",
                message="A  small amount of food eaten between meals..",
                app_icon="D:\Chrome\snacks.ico.ico",
                timeout=2
                )
        elif(a>17 and a<18):
                notification.notify(
                title ="Sleeping Time",
                message="A condition of body and mind that typically recurs for several hours every night, in which the nervous system is relatively inactive, the eyes closed, the postural muscles relaxed, and consciousness practically suspended.",
                app_icon="D:\Chrome\icon.ico.ico",
                timeout=2
                )
        elif(a>18 and a<20):
                notification.notify(
                title ="Playing  Time",
                message="deal with someone or something in a way that lacks due seriousness or respect.",
                app_icon="D:\Chrome\icon.ico.ico",
                timeout=2
                )
        elif(a>20 and a<21):
                notification.notify(
                title ="Dinner  Time",
                message="The main meal of the day, taken either around midday or in the evening.",
                app_icon="D:\Chrome\icon.ico.ico",
                timeout=2
                )
        elif(a>21 and a<24):
                notification.notify(
                title ="Study Time",
                message="The devotion of time and attention to gaining knowledge of an academic subject, especially by means of books..",
                app_icon="D:\Chrome\study.ico.ico",
                timeout=5
                )
        elif(a>0 and a<6):
            notification.notify(
                title ="Sleeping Time",
                message="TA condition of body and mind that typically recurs for several hours every night, in which the nervous system is relatively inactive, the eyes closed, the postural muscles relaxed, and consciousness practically suspended.",
                app_icon="D:\Chrome\icon.ico.ico",
                timeout=2
                )
        else:
             notification.notify(
                title ="No Task At time",
                message="Hello,Thank for using my notification system",
                #app_icon="D:\Chrome",
                timeout=2
                )
