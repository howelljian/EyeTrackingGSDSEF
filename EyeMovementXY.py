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



data=[500.09860245145154, 499.9410528822844,501.4217577394857, 499.85128872518175,497.8130193644509, 499.1415806309553,525.1740423864493, 468.2342500720309,525.1321915640997, 464.0198520188156,512.9267128217793, 437.1687919744384,527.2001044671789, 375.1290014208274,608.6126772409862, 389.99284025275523,724.6294073553638, 438.47589544995566,706.5471684140267, 480.28693680702503,700.7254532258805, 427.3676594559414,638.4828003074464, 472.5601766869977,808.8334378505114, 433.9980149881908,677.8276023302021, 385.4909458301546,728.4377324856154, 460.2806615735627,756.4131819089636, 464.9422427066012,898.9898060332541, 504.808192989373,1302.0909079925207, 617.5390547484734,1179.4878598280409, 597.6713727328469,1081.0634146227453, 536.3595809576746,1008.2251206828654, 560.9024599375175,904.8907455882608, 517.5975528127864,771.632192389885, 513.5571308290657,721.5669080765829, 507.7227608307763,622.9542865939403, 564.898691779615,561.847199163687, 574.0136167511118,517.7738251402454, 597.3728840134064,496.7487675819036, 531.6244692091152,558.9837846387721, 537.5958118708343,500.69938886125453, 543.0763981636901,525.0736595536764, 462.1821993838358,467.24332475390696, 394.1154691557492,419.77301176683227, 411.8815995740842,443.7816687876702, 420.607170701897,401.46765787132034, 444.035327204914,377.77693159590643, 480.87784216334285,381.5342089263222, 542.1510181892801,417.77723167823405, 615.6197351694227,388.51613144611235, 690.8405429947176,376.16515615902637, 756.5289488226834,237.16283015693296, 822.0694087179324,410.2700116098414, 891.0326721216231,474.1953752361144, 984.6123257133861,440.775175238932, 902.5706224597211,431.06334255737136, 894.1571279357256,321.5569828531385, 712.9348755665568,243.62245486573553, 646.9373504649811,352.7284248577646, 606.2137834150159,404.6417372895992, 664.6686072510863,339.43812013220094, 625.1746543837239,473.64673432030224, 538.2660306765987,712.8375118334886, 488.01689124308257,727.4252950470714, 339.59137424636947,930.4461529930884, 397.8904084619978,905.5573418501442, 443.4271397084465,839.9524279762334, 426.3601156643398,960.8882239265173, 439.5930679310828,1076.2167332387642, 493.9971450643642,1096.0828659325202, 540.4633015982063,1189.131753590612, 446.8574768974661,1174.4001705012815, 352.42268845277135,1158.968459066392, 368.34048111070746,1054.6758907043431, 380.02861363637425,1034.2579497127329, 281.7196103701264,840.7420258867954, 251.1602828564475,621.3622521215088, 284.87219494899534,558.5527964011371, 115.23588413338928,761.5071063306185, -6.59946814464179,669.2335954044778, 23.130240199753928,592.5643892933526, 54.57001013900543,746.9414900324293, 89.20656361040726,514.9418399489618, 194.70320128304206,383.691639099422, 71.97518656782033,243.2614036941283, 283.9010418442431,204.67910145249374, 280.6410410398185,232.95284368273886, 246.27148385266548,357.8947454933766, 216.40054589839087,306.7270237938293, 242.9754398052782,213.89030257927882, 367.86385897404875,215.9388201465549, 451.5613545879154,441.3621315504006, 540.0785164952143,463.9489547576594, 454.99245758373206,564.9567550420477, 448.5502148384655,674.8017083251073, 479.41639221113155,560.3028969760943, 389.09708103603595,570.8549723376724, 454.6392031824579,555.2227777695794, 540.6785986867554,577.588342485571, 597.7989816319301,623.0642707096589, 609.9798626391055,756.7951592053018, 643.8464517001781,611.1130300380457, 553.5207296533872,692.3189399207495, 558.4957649468747,518.4844866347169, 524.5082974655446,600.5759557771596, 492.5463018289718,516.6405730256662, 422.98520270716415,529.737136776353, 398.72751033963783,360.6161296292056, 343.4429825580084,174.13552333045277, 440.9947749293404,154.409666027845, 372.8806936258054,164.43043306172848, 287.8248014540992,237.6200061983106, 325.0450723066216,378.6819465130396, 348.0847092785276,365.08929050350343, 396.24985616189116,576.3373630266804, 499.6856780038321,555.5010766558472, 506.238048985716,639.7480114524317, 416.90060717930896,541.7510898546503, 400.62015703719567,748.183105769323, 333.29726589654524,953.8878023079976, 279.1056869651281,1032.9487081092066, 284.2634914586663,1100.2569139834131, 430.59717373479805]
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
        print("Signs of pendular Nystagmus. Possible reasons: birth, trauma")
    elif jerk==True:
        print("Signs of jerk Nystagmus. Possible reasons: neurological conditions")
    else:
        print("Did not find signs of Nystagmus")
else:
    print("Did not find signs of Nystagmus")
