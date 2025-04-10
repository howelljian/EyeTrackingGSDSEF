import matplotlib.pyplot as plt 
import numpy as np
import math
import time

#0.02 secs = 1 datapoint

height_diff = 0
width_diff = 0
threshold = 1000
threshold_twitch = 10
tuning_value = 0.1
num = 0
accuracy = 0
twitch_counter = 0
vh_twitch=[]
pen1=0
timer=0
curve_count=8#thresh for amt of curves

cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0
cat5 = 0
cat6 = 0
seesaw1=0

count = 0
greatest_diff = 0
least_diff = 1000



data=[500.0953871541216, 499.84673749393943,508.61353236775517, 497.3453817302159,528.7937998434726, 491.3662815161761,570.4296045805745, 502.6990924884459,590.3165321973471, 461.82662553343255,642.2882445923867, 495.0440118032849,581.902429014915, 536.7691551935311,685.8190254073594, 528.812203805797,758.2172285825211, 529.2844189213512,890.2933564694089, 522.7349191209925,828.3500551371671, 475.55285626491053,863.052670736552, 457.16649011091573,855.0024845050118, 445.9416328918143,917.7732165698685, 397.9780944949556,961.5482682740901, 367.1603336380374,1020.4693175069327, 371.0120509249444,1200.6864863178944, 354.9576227490585,1296.281273232013, 295.51540032932036,1244.3507260652784, 225.62209377122971,1314.0587551276842, 251.59566316769624,1387.4140185835847, 283.1766290320151,1378.016770340598, 344.35495537724194,1268.3188789135224, 321.92293675238324,1168.1613080104034, 328.7143122280378,1151.140789698646, 363.95089409004567,992.6546122372184, 399.4743637386781,911.0983182548248, 373.15503557299894,783.7502674604033, 377.8378179044425,557.7332414835961, 383.3319059969524,596.1055823293223, 386.0831906137938,491.28769495689767, 468.3703954270327,661.1221510714452, 478.5439403844094,763.7678985324624, 474.4863469998188,869.7052390528731, 489.0391268686784,914.7070418383686, 429.4346472673815,669.3683434918611, 471.102395555458,771.485250606337, 480.4685974997684,763.24126684179, 480.5362874334329,870.493841043585, 481.5647777675618,1039.324454915683, 496.62528223005444,1053.1267973457711, 531.5591932813327,1035.5863049291947, 473.8289284368332,998.0380947267695, 507.2376514181693,1017.0727886149506, 473.5108090030092,939.2095423800923, 433.72253227750014,966.2993495495986, 503.3013319018908,907.2603303499317, 500.58681080242667,901.7679439682335, 605.2569102899813,1007.528330743994, 678.597722987427,774.9829211060518, 500.87436598754675,638.5070277100506, 500.35652456800904,751.6788548105977, 426.2482150923385,769.8575497467218, 454.15685544715296,796.7884237436716, 436.50844057043656,609.3813968863764, 447.2132118520314,629.3327355823844, 470.6753216995313,539.1409703539226, 470.0993630913887,498.8765540548927, 455.91760839195575,623.0586607902643, 526.7296177678498,594.237276267817, 711.8841040332948,637.0421072367891, 611.384616433229,632.1395629882377, 700.0469726211313,641.4581085906659, 731.1637559528523,663.3718668530687, 717.3372137029804,542.1036933475009, 701.8523413074089,504.66963211848645, 682.2355398929813,502.085870625272, 577.5294839895348,616.0868810708571, 481.1634448786335,652.7396755591474, 431.24960417594446,787.8609693519256, 393.5348879334972,797.7634318306095, 395.72955524799227,1109.7024495333262, 400.9118251753127,1114.65393714673, 441.3732658740414,1145.5942847868755, 431.2615277515663,1212.7735325665906, 430.55118838024634,1160.4636502965466, 393.8702262133295,1325.9241815906428, 376.4487216144457,1248.32161080216, 376.6636447190078,1252.4836212652906, 394.830477906306,1185.5552038257017, 388.7686474114949,1213.4483168448746, 334.6537676457371,1099.3366302523218, 287.57296469290134,999.1286400022168, 280.7747534192752,869.290098621412, 361.9116431586817,717.7768278794414, 357.9410093294308,729.311136251557, 347.22369994749954,654.5337385348397, 382.0992811500945,780.3993948755055, 371.333762933373,709.6614522577113, 323.73377797640336,699.4572111592829, 386.8957065381672,726.3809454837103, 362.86006862525454,725.9360041696269, 321.0912287876478,591.4146917127146, 370.4526976476558,677.3787028182189, 322.35962979066056,821.4091208932917, 316.62395273545576,969.6009180887352, 335.6980125713485,923.3899522557689, 458.3036706349616,1030.9679992800686, 378.2419034515455,1013.8165731539118, 408.80791187430793,1139.863653249521, 514.3788293860213]
minimum = min(data)


curr = 0

x_values = data[0::2]  
y_values = data[1::2]  


colors = plt.cm.viridis(np.linspace(0, 1, len(x_values)))


plt.figure(figsize=(10, 6))  




for i in range(len(x_values)):
    plt.scatter(x_values[i], y_values[i], color=colors[i], s=100, label="Point" if i == 0 else None)


plt.plot(x_values, y_values, color="gray", linestyle="-", alpha=0.7)


plt.title("Eye movements", fontsize=16)
plt.xlabel("X Values", fontsize=12)
plt.ylabel("Y Values", fontsize=12)
plt.grid(True)

plt.tight_layout() 
plt.show()

    
    

for i in range(len(y_values)-3):

    if i%2 == 1:
        height_diff = abs(data[i] - data[i+2])
        width_diff = abs(data[i+1] - data[i+3])
        

    if data[i+1]-data[i+3] < threshold_twitch*tuning_value and data[i+1]-data[i+3] >-threshold_twitch*tuning_value:
        count += 1
        print("Possible Vertical Eye Twitch Detected at:", data[i], data[i+1])
        twitch_counter += 1
                
                

    else:
        height_diff = abs(data[i+1] - data[i+3])
        width_diff = abs(data[i] - data[i+2])
        
    
       
    if data[i]-data[i+2]< threshold_twitch*tuning_value and data[i]-data[i+2] > -threshold_twitch*tuning_value:
        count += 1
        print("Possible Horizontal Eye Twitch Detected at:", data[i+2], data[i+1])
        twitch_counter += 1

        


    curr = math.sqrt(height_diff**2 + width_diff**2)

    cat1, cat2, cat3, cat4, cat5, cat6 = 0, 0, 0, 0, 0, 0
    greatest_diff = float('-inf')
    least_diff = float('inf')

# Iterate through the data points
    for curr in data:
        if 400 < curr <= 800:
            cat2 += 1
        elif curr <= 400:
            cat1 += 1
        elif 800 < curr <= 1200:
            cat3 += 1
        elif curr > 1200:
            cat4 += 1

    # Update greatest and least differences
    greatest_diff = max(greatest_diff, curr)
    least_diff = min(least_diff, curr)

# Print summary

    

    if curr > threshold:
        print("Anomaly Detected from:")
        print("")
        print(data[i],data[i+1])
        print(data[i+2], data[i+3])
        print("")
        print("With a distance of:", curr)
        print("")
        
        count+=1
        if curr > greatest_diff:
            greatest_diff = curr
            
        if curr < least_diff:
            least_diff = curr
            

    
        continue




print("Greatest Difference", greatest_diff)
print("Least Difference", least_diff)
print("")
print("")
confidence=twitch_counter*2/5
print("Confidence", confidence)




def alternating(vh_twitch, tolerance):
    errors=0
    for i in range(len(vh_twitch) - 1):
        if vh_twitch[i] == vh_twitch[i+1]: 
            errors+=1
    if errors>tolerance:  
        return True
    else: return False



def pendular():
    global pen1
    global vh_twitch
    global curve_count
    pen1=0
    is_vh=False
    for i in range(len(data)-3):
        if abs(data[i]-data[i+2])<abs(data[i+1]-data[i+3]):
            vh_twitch.append('v')
            pen1+=1
        elif abs(data[i]-data[i+2])>abs(data[i+1]-data[i+3]):
            vh_twitch.append('h')
            pen1+=1
    if pen1>=curve_count and alternating(vh_twitch,50)==True:
        return True

def jerk():
    for i in range(0,len(data)-4,2):
        xdiff=abs(data[i]-data[i+2])
        xdiff2=abs(data[i+2]-data[i+4])
        if abs(xdiff-xdiff2)<=10:
            return True
    return False




# Formatting answers
if confidence>0.5:
    if pendular()==True:
        print("Signs of pendular Nystagmus")
    elif jerk==True:
        print("Signs of jerk Nystagmus")
    else:
        print("Did not find signs of Nystagmus")
else:
    print("Did not find signs of Nystagmus")
