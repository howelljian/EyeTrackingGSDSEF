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

data = [148, 30, 151, 38, 151, 38, 160, 55, 167, 59, 167, 62, 160, 48, 160, 51, 159, 50, 159, 51, 159, 49, 159, 48, 158, 48, 157, 47, 155, 45, 155, 45, 155, 43, 154, 43, 155, 46, 156, 46, 156, 51, 156, 49, 156, 52, 155, 51, 154, 52, 155, 54, 155, 55, 155, 55, 155, 53, 155, 54, 155, 53, 155, 53, 154, 55, 154, 57, 153, 59, 152, 62, 149, 62, 147, 61, 148, 59, 149, 62, 150, 64, 151, 63, 151, 60, 152, 59, 151, 60, 150, 63, 149, 61, 149, 62, 148, 62, 147, 63, 146, 61, 146, 60, 146, 58, 147, 57, 148, 57, 148, 57, 148, 59, 148, 61, 149, 64, 149, 67, 149, 68, 144, 67, 140, 65, 137, 65, 120, 68, 301, 64, 299, 64, 289, 71, 287, 72, 283, 72, 281, 70, 275, 64, 358, 15, 255, 299, 251, 289, 244, 269]

maximum = max(data)
minimum = min(data)

x_values = data[0::2]
y_values = data[1::2]

colors = plt.cm.viridis(np.linspace(0, 1, len(x_values)))

plt.figure(figsize=(10, 6))

for i in range(len(x_values)):
    plt.scatter(x_values[i], y_values[i], color=colors[i], s=100, label="Point" if i == 0 else None)

plt.plot(x_values, y_values, color="gray", linestyle="-", alpha=0.7)

plt.title("Eye Movements", fontsize=16)
plt.xlabel("X Values", fontsize=12)
plt.ylabel("Y Values", fontsize=12)
plt.grid(True)

plt.tight_layout()
plt.show()

for i in range(len(y_values)-9):
    if i % 2 == 1:
        height_diff = abs(data[i] - data[i+2])
        width_diff = abs(data[i+1] - data[i+3])

    if (data[i+1] + data[i+3] - data[i+5] + data[i+7] - data[i+9]) < threshold_twitch * tuning_value and (data[i+1] + data[i+3] - data[i+5] + data[i+7] - data[i+9]) > -threshold_twitch * tuning_value:
        count += 1
        print("Possible Vertical Eye Twitch Detected at:", data[i], data[i+1])
        twitch_counter += 1

    else:
        height_diff = abs(data[i+1] - data[i+3])
        width_diff = abs(data[i] - data[i+2])

    if (data[i] + data[i+2] - data[i+4] + data[i+6] - data[i+8]) < threshold_twitch * tuning_value and (data[i] + data[i+2] - data[i+4] + data[i+6] - data[i+8]) > -threshold_twitch * tuning_value:
        count += 1
        print("Possible Horizontal Eye Twitch Detected at:", data[i+2], data[i+1])
        twitch_counter += 1

    curr = math.sqrt(height_diff**2 + width_diff**2)

    cat1, cat2, cat3, cat4 = 0, 0, 0, 0

    for curr_val in data:
        if 400 < curr_val <= 800:
            cat2 += 1
        elif curr_val <= 400:
            cat1 += 1
        elif 800 < curr_val <= 1200:
            cat3 += 1
        elif curr_val > 1200:
            cat4 += 1

    greatest_diff = max(greatest_diff, curr)
    least_diff = min(least_diff, curr)

    if curr > threshold:
        print("Anomaly Detected from:")
        print("")
        print(data[i], data[i+1])
        print(data[i+2], data[i+3])
        print("")
        print("With a distance of:", curr)
        print("")

        count += 1
        if curr > greatest_diff:
            greatest_diff = curr

        if curr < least_diff:
            least_diff = curr

print("Greatest Difference", greatest_diff)
print("Least Difference", least_diff)
print("")
print("Confidence", twitch_counter * 2 / 5)

plt.hist(data, bins=50, edgecolor='black', alpha=0.7)
plt.title("Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
