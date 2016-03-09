import pyowm

"""apothhkeush suntetagmenwn apo ton xrhsth"""
x = float(raw_input("Dwse suntetagmenh x: "))
y = float(raw_input("Dwse suntetagmenh y: "))

"""eisagwgh dedomenwn kai dhmiourgia listas gia ton kairo"""
API_key = 'a711d9b24b3abef4e83f6be9d8483282' 
data1 = pyowm.OWM(API_key)  
data2 = data1.weather_around_coords(x,y)
kairos = data2[0]

"""emfanish polhs sumfwna me tis syntetagmenes"""
topothesia = kairos.get_location()
polh=topothesia.get_name()
print "Polh: ",polh


weather = kairos.get_weather()
thermokrasia = weather.get_temperature('celsius')
kairikessunthhkes = weather.get_status()

"""emfanish mhnumatos ean vrexei"""
if (kairikessunthhkes == 'rain') or (kairikessunthhkes =='Rain') or (kairikessunthhkes =='rainy') or (kairikessunthhkes =='Rainy') :
    print "I'm singing in the rain!"

"""elegxos timhs thermokrasias kai emfanish katallhlou mhnumatos"""
if thermokrasia['temp']>20:
    print "nice..."
elif thermokrasia['temp']<5:
    print "brrrr"
else:
    print "Cool, thermokrasia:",thermokrasia['temp']


