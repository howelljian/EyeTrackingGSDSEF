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



data=[500.2572237863954, 500.10128186589316,498.8251049204046, 499.6492600497174,509.3091350722425, 499.2496068920409,558.1472128838072, 486.5726469525593,603.252590348632, 481.3164826890483,673.5216905573475, 481.6898629475865,730.5817577593807, 495.92312491420535,747.8890588604132, 547.653989793421,819.8537723630229, 583.0381097011759,827.6299649503457, 614.6835185211689,900.4044351074975, 642.2911856556975,948.8976738508136, 591.3042357902826,954.737876723332, 620.3600097635818,941.9822204045639, 679.348451620142,942.7578728990129, 701.1072899584935,837.6706381770476, 676.8714213386356,849.8011665487511, 633.7152353724342,787.6533596857456, 639.0807618588294,655.4281212754576, 665.1381736084661,581.3704463805918, 644.1752715631254,533.8672912335312, 652.6250726338417,542.7165563625315, 609.5603810474543,499.3172809094217, 504.1420351923045,534.6432111031231, 496.4383024699383,555.2362369005369, 460.9069587600508,578.6018591107047, 472.5158937837233,638.6640708398536, 469.97497763840136,717.565500367225, 491.9826926402906,741.2205293285007, 449.9049441271976,873.832180388838, 422.0548816179037,756.3853896433017, 456.3492246526651,786.0142865590982, 416.0225364880922,845.360511861624, 388.09775866484836,899.0241968285171, 379.12072755081465,857.8324964325731, 422.36523419372054,884.3602480548504, 431.90854147636855,965.6561412029575, 429.63011247010365,938.6433542355845, 472.7958699037559,748.8539921643618, 465.33219283529223,641.7081726837499, 471.3648068675922,631.6371620071156, 440.9076870437037,719.5535893889426, 376.7502659266449,822.1672303199059, 369.8302366403723,907.103200190056, 333.5747086633609,901.3398126481719, 328.050041667019,912.7209753228419, 351.95751071940566,989.3737906842539, 343.41082743409584,1015.33992926747, 320.7784755659274,993.0010237562426, 342.98132522663934,1006.7926500664851, 370.0470963945813,1003.9443972491642, 391.80172692023353,1028.898068469287, 367.6663175543689,1006.6375154673646, 298.651582514905,977.8235916097173, 286.9530811918667,947.749017341069, 262.3133004592146,940.817306385898, 276.4062652335015,905.719921640701, 246.1777047492597,878.1878370285178, 277.5248113967648,962.0781154481015, 247.45800441202496,970.6505533420346, 232.23114095108036,1030.8610008641783, 233.1708531711615,997.2251628865043, 310.2416004382445,952.2337923334075, 322.28346572056654,957.0097159197186, 354.8045543743727,927.2242288809067, 399.63128605244094,910.8742772724527, 401.33091079547137,904.8685998492736, 458.16252003900104,949.4620882299163, 540.8844002019823,889.9653684923125, 553.5290685226427,910.7159224851902, 557.0942974363825,951.5038086615085, 503.49258961445537,861.48500297019, 521.5563541121519,969.9256955502486, 478.8286945509243,946.6139425471011, 529.3098110109447,876.2823064955493, 579.0867019392784,852.8640182327428, 567.2835081125841,903.7966717630873, 606.6463776559087,861.6716905123111, 631.6268378238542,912.3968492297631, 651.780784533653,946.1623186242228, 655.6521603981255,853.0274959645513, 701.3926147473906,925.2331898845625, 691.1027264740056,945.9930101298404, 688.9525092166544,909.6078194001235, 679.5876649802219,846.597974040636, 649.4772722447188,825.2726738357832, 627.500801811522,901.9477686702539, 596.8867484075632,893.8336732845529, 626.6289663151684,872.3451572693926, 605.8586808371981,870.0147599620523, 601.238457027219,866.0174327074534, 551.555994847211,877.6034025475017, 586.3486065900479,908.4740893539224, 628.5706421920022,941.8799181285306, 608.0374866511413,899.1707341907435, 623.9445668595062,913.2241034891214, 594.8126245960393,902.8497672680791, 614.8022993043093,915.1917624314983, 590.1886450077484,1012.758737651432, 575.1756727966065,1083.1199848701365, 535.7796746184454,1008.8738384045263, 424.56311472469474,1060.4827401653952, 331.92225485714255,1106.382535823518, 329.2841293617357,1196.7136431867043, 305.1001836553332,1205.227110317259, 274.60719507982424,1109.5107956491042, 242.3078178484383,1019.2753740086664, 238.5870730081683,872.976393259745, 284.0680486272937,766.8095658478787, 205.77795355661675,707.6034685034266, 140.6708023870351,690.963156474039, 67.6841078811639,749.3202606331879, 67.46112432115406,934.0741794950444, 55.21267700189673,1005.8344342992693, 64.83013889788471,1012.2997562607866, 36.69688540350025,1025.2545736320387, 23.719609788156948,1031.08917305476, 62.44970278775896,1020.4515692805398, 89.72868214576141,971.3717273056008, 110.69317141748377,962.004878533231, 97.08189965270394,902.3402793009941, 212.47678519288925,888.5626745662755, 317.5900809011158,820.0515872642576, 362.2095738406463,874.9490553082295, 336.8479704992736,990.7261119412366, 344.6235812003783,1010.9630878401385, 380.4625984933726,1040.8069414289334, 384.1241054478629,1030.5033843715403, 411.19582323848334,1116.9014173609726, 405.87368126838817,1069.2222399607892, 494.8481460895578,971.7266697342667, 566.5330301729738,815.5376520230336, 564.7154828955947,777.504247901042, 566.670661052585,748.5175689311658, 559.6187873214402,829.4716348943018, 566.3025522367674,963.0508464633848, 496.47517015815805,1068.573577350703, 512.3245193318488,1106.682891096141, 517.4292832362853,1131.4034515503142, 501.6943240614488,1113.6229399103024, 491.55837001488953,1148.9886760566183, 462.9968520226836,1183.4253700368586, 445.16436498794627,1187.2270804684126, 462.33789461802115,1190.684311581263, 443.29326122733397,1161.993813236141, 432.3315290572272,1050.2582087449646, 408.37173291692443,1026.5416566007718, 400.16278439138324,1011.1532863805969, 374.2443058633214,1027.4583428430496, 390.0610969351357,886.0171095045023, 423.5922258980194,834.844079095268, 428.80288979364497,868.4440897008257, 479.39521860096056,786.0712792259104, 480.2601287314113,666.3146700145055, 467.5724575982151,611.3480738571229, 485.09423811210013,621.8705548916347, 448.2736818742237,646.3752668373774, 416.84665488684334,678.9378276390566, 407.21511635406733,723.0660712151466, 384.4401470672433,781.2398315769592, 351.6125538146148,861.2838821226132, 344.54868201346324,918.4744667646773, 359.53584920771954,954.9013297932188, 387.9466898444822,931.0539751793913, 357.9641777859903,914.8368033665807, 396.03707715231604,868.9829341248794, 416.01165597816134,855.2635965603647, 433.7229054371299,849.1386442506206, 482.4194038037284,942.1245476309794, 416.6667076919225,1028.6394300786985, 374.59725973216047,1005.4610234504805, 370.20564534206653,900.8774175970489, 398.2988966321068,756.6845637543513, 389.8548136100133,787.1193447166416, 348.73015399075797,833.3658285347788, 312.4099507612097,816.5088914074231, 386.8376531424805,804.3854195276784, 432.88002669414885]
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
confidence=twitch_counter*1/5
print("Confidence", confidence)




def alternating(vh_twitch, tolerance):
    errors=0
    for i in range(len(vh_twitch) - 1):
        if vh_twitch[i] == vh_twitch[i+1]: 
            errors+=1
    if errors>tolerance:  
        return False
    else: return True



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
        print("Signs of pendular Nystagmus", pen1)
    elif jerk==True:
        print("Signs of jerk Nystagmus")
    else:
        print("Did not find signs of Nystagmus")
else:
    print("Did not find signs of Nystagmus")
