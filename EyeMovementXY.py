import matplotlib.pyplot as plt 
import numpy as np
import math
 

height_diff = 0
width_diff = 0
threshold = 1000
threshold_twitch = 10
tuning_value = 0.1
num = 0
accuracy = 0
twitch_counter = 0

cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0
cat5 = 0
cat6 = 0

count = 0
greatest_diff = 0
least_diff = 1000



data = [502.21389728214956, 431.8765220302101, 536.226237546654, 406.6492995472898, 522.2035655482847, 370.71757776597474, 495.64992600582934, 464.7937831285434, 537.9153040687302, 459.9209914890695, 478.46202990728364, 472.4126684980109, 527.7054917350556, 457.8991716348911, 531.7134306331681, 452.327793914069, 493.7014257453526, 462.01239578795526, 463.00542287510405, 426.45563035940023, 447.5866353006947, 392.57877302913175, 512.2550491683572, 392.91483695810234, 483.45501801293597, 353.64471285859486, 454.8652515419334, 344.0536192195506, 447.90377289063014, 284.1415194325545, 477.3065405165274, 252.55558730901157, 452.583214752614, 236.4604482608855, 420.99940907251823, 241.07849017161075, 427.94594745353004, 238.62333462862486, 406.07131612695923, 264.28154486677647, 372.7732442858517, 287.69187601250326, 479.20264730342154, 263.4990323847301, 434.9915984855043, 246.72189399492092, 396.80339946997293, 249.42395231373087, 612.4235960658621, 303.66592990478557, 787.6647409593882, 303.65411596994386, 851.7819212106112, 281.88089242755433, 1005.519991431635, 262.85413427227695, 1070.5597814476662, 273.52698368419243, 1018.156085870871, 259.4950638949789, 1022.7167606980055, 224.99842724377538, 1143.667837786471, 223.8252312994656, 1241.0292118270672, 200.4651096046608, 1327.204495121779, 205.49577795577503, 1419.0980296185446, 210.33129387556153, 1408.1078125721301, 259.2452803300043, 1328.035828861766, 259.574788142534, 1378.7657674069997, 258.7722952007701, 1326.8114269958567, 312.00953047359263, 1292.0053090320469, 310.73404124123414, 1349.7238031435309, 317.4729900415026, 1326.6587322456676, 286.4540095370166, 1295.711804208497, 267.5907444726823, 1230.8201771548381, 247.93990934847605, 1172.1378178175257, 221.42806520206483, 1153.993474135539, 212.42753339767125, 1162.6154124833297, 201.41957812448956, 1217.398220409077, 190.56382932352057, 1109.5352449068155, 240.8762621955102, 1026.1687533331533, 225.1927209958302, 1013.6173845026037, 227.78815625952683, 1037.0177166531435, 248.0253245587912, 1109.5934692855362, 264.3356095869875, 1101.9883243556806, 336.8771757405985, 1156.0955951840974, 370.86722972233264, 1128.7307665808037, 421.43993291338364, 1128.4874629813048, 418.77619373932487, 1119.651545617868, 395.683682904690
,499.94212464806105, 499.98070821602033, 507.1776824617772, 499.14251185044265, 520.911474944544, 495.96269027925695, 548.760444336794, 487.7121036561766, 610.0037985911961, 478.8195027658403, 762.0603630662254, 405.42279427418055, 884.0954117593204, 334.03619847367804, 984.2499832385931, 285.25133309745723, 1071.835592741557, 239.12227181085456, 1160.4764345509177, 206.96048548048753, 1238.2687730695948, 160.9787197117779, 1347.734171947598, 160.04735271321601, 1337.5751703401775, 162.01977689963536, 1404.9204507101867, 99.52256903802598, 1382.2697280647394, 90.99523223110674, 1370.0749891339299, 112.87134434574392, 1394.624686214384, 137.34139127517935, 1335.5420463784083, 136.1203971208637, 1422.0809687912592, 133.63326830652318, 1356.6726500536818, 138.1238714983334, 1332.161424977922, 124.29520900678483, 1372.2032269098697, 83.60854550277173, 1293.3190449774313, 59.87015808591898, 1327.1996738816163, 77.22101037770881, 1306.33436826689, 126.66913228026203, 1260.4702391131066, 138.3813947883156, 1164.016470307172, 195.84352045819605, 1217.5745966843015, 209.38177408851328, 1219.8668236443307, 295.7455390571887, 1257.9206175795227, 335.6510775114556, 1240.1315457063247, 354.8912881405052, 1355.7439476959373, 412.25023566326394, 1248.52395873256, 418.87460856040354, 1232.7972845512618, 481.50780464493977, 1238.3102179707014, 563.0742009769149, 1165.5251202420982, 574.2582207511449, 1140.641443917285, 580.2385259531414, 1139.0749279680804, 566.5557431733539, 1170.082259904283, 520.6743708991428, 1104.4909636774996, 482.97184449291893, 1117.2535882516086, 442.66571792521313, 1153.3915737547134, 463.81770774086203, 1151.3427848169956, 466.0123950066729, 1143.2496058705026, 482.8518142278195, 1187.8254257124809, 489.3644178601517, 1188.5225717901224, 486.32201994687074, 1244.0028514847331, 443.18680444012324, 1101.6399476354227, 432.05265814257695, 1127.043276449951, 395.77870083825934, 1192.6983288698043, 442.68923601035635, 1240.1064638099986, 413.23168117411933, 1315.2707473163975, 458.1850463782562, 1223.8082165877481, 512.4353799564362, 1233.5395031771002, 527.1503563626575, 1191.949574121179, 492.45945431416146, 1160.020401646822, 494.21089136379237, 1110.6490957027956, 510.961359653854, 1072.5982008352164, 537.0968918579526, 1235.6871213487361, 516.8107219769191, 1334.0994935827825, 512.201329295213, 983.4622172788073, 442.3679149231958, 848.6991544302788, 447.0570589963725, 739.9381405059174, 426.0325474380665, 619.9300264383802, 453.8617692823295, 554.195346025874, 523.9958205822406, 570.9858476513268, 539.4450546838509, 586.4544048883454, 538.8408787253146, 427.6901845572098, 535.9827747078591, 305.20029927656935, 549.9583431672622, 303.43492182953776, 521.8907500565973, 293.31443756787144, 469.7289154028123, 281.4729730632161, 412.3414726883846, 174.93476792022753, 433.34890381725864, 83.5256533287955, 417.43492695645944, 221.39809424506308, 356.98021495153563, 316.6142373231719, 294.90363883820316, 430.5699802204772, 238.58791854826535, 332.19113763999223, 277.1736837360849, 250.6213468502889, 311.9149688655907, 296.10209318696843, 360.5637514952575, 328.85427725691784, 430.8589082020864, 447.04483531219864, 475.6269707280476, 450.7937117660093, 550.6064926276484, 660.8973044385107, 590.730116909154, 651.1390655957517, 546.2854813121029, 602.9526046654395, 573.1002760273742, 692.0698241493502, 546.265278167508, 501.22900092816667, 540.6347031176874, 542.9073229111442, 548.8023753297033, 589.7308597546242, 584.6770000230829, 569.0118376575753, 600.1332531108, 613.7079650951066, 594.8833943244437, 572.1786030120139, 629.296762070064, 486.28266697185273, 614.2413088422669, 417.5009965765006, 675.2836276646765, 458.2301201076405, 640.5402199167297]

maximum = max(data)
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
print("Confidence", twitch_counter*2/5)









# Visualize data distribution
plt.hist(data, bins=50, edgecolor='black', alpha=0.7)
plt.title("Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


plt.show()
