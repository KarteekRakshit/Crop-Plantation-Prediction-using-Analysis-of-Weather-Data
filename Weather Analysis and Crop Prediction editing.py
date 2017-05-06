import Tkinter as tk
import tkMessageBox

Chennai=[24.725,18.541666,27.683332,22.125,65.899994,126.41668,112.125,115.05833,176.55,243.29167,224.09167,119.5,'Paddy','Cocnut','Groundnut']
Coimbatore=[7.7285714,7.0142856,38.357143,52.14286,86.2,56.985718,113.442856,79.51429,93.91428,175.61427,165.78572,37.928566,"Paddy","Vegetables","Corn","Maize","Pulses"]
Cuddalore=[20.833334,23.991669,57.224995,19.191668,107.38334,105.31666,61.208332,131.55,86.458336,234.69165,329.10834,129.80832,"Paddy","Sugarcane","Cashew","Groundnut","Millets","Pulses"]
Dharmapuri=[39.491665,26.108332,77.34167,60.800003,133.59999,128.93333,52.78333,130.09166,108.99167,118.541664,107.55833,34.100002,"Paddy","Mango","Tomato","Millets","Pulses"]
Dindigul=[17.125,9.625,80.65,71.841675,59.916668,92.06667,32.650005,83.05833,124.74168,183.55833,145.08334,93.975006,"Paddy","Flowers","Tobacco","Fruits","Oil seeds","Millets","Pulses"]
Erode=[47.416668,8,29.650002,66.96667,78.24166,39.325,32.466667,46.316677,73.850006,109.033325,116.700005,78.475,"Turmeric","Paddy","Sugarcane","Tapioca","Cotton","Groundnut","Gingelly"]
Kanchipuram=[10.033334,10.349999,24.833334,52.499996,52.316666,90.30834,45.20001,66.48333,151.38333,171.65833,204.44165,143.45,"Rice","Sugarcane","Groundnut","Pulses","Millets"]
Kanyakumari=[20.625,31.958336,47.13333,106.60833,85.225006,91.85,74.15833,62.791668,114.54168,145.11665,135.34166,162.01666,"Banana","Paddy","Pulses","Tapioca"]
Karur=[6.9166665,18.316666,19.65,51.95,57.808334,62.466663,59.100002,93.049995,94.075005,116.94167,154.85834,123.67501,"Paddy","Sugarcane","Millets","Pulses","Groundnut"]
Krishnagiri=[35.366665,6.3916664,54.483334,31.858332,75.84167,89.13333,91.56667,106.966675,114.458336,175.68333,108.75833,102.00833,"Mango","Paddy","Millets","Pulses"]
Madurai=[19.733332,24.233332,88.94167,41.808334,56.375,75.700005,65.675,165.28333,101.525,169.90834,164.80833,63.716663,"Paddy","Millets","Coconut","Pulses"]
Nagapatinam=[62.100002,29.666664,116.44166,32.5,80.60833,105.38333,141.55833,161.01666,93.40835,309.78336,352.94165,196.05833,"Paddy","Sugarcane","Pulses"]
Namakkal=[10.908333,2.2583334,136.31667,40.725002,171.825,129.34999,109.041664,124.725,92.475006,195.675,132.19167,55.058334,"Sugarcane","Tapioca","Oil Seeds","Groundnut","Gingelly","Cotton"]
Nilgiri=[26.650002,28.558334,114.166664,234.97499,222.93333,178.35834,214.09167,200.075,158.60834,187.31667,177.13335,53.79166,"Vegetables","Fruits","Condiments","Tea","Coffee"]
Perambulur=[9.133332,34.899998,60.658337,86.674995,135.27501,60.425,58.649994,103.64166,138.10832,127.85834,155.13332,76.833336,"Cotton","Paddy","Sugarcane","Maize","Pulses"]
Pudukottai=[12.6833315,45.783337,57.816666,120.50834,218.03334,38.1,46.483334,98.71665,77.666664,136.35,153.73332,120.399994,"Paddy","Millets","Groundnut","Pulses"]
Ramanathapuram=[35.808334,63.108326,100.200005,158.68333,195.95,24.666666,21.716665,43.666668,92.958336,195.74164,163.60834,118.875,"Paddy","Chillies","Millets","Cotton","Groundnut"]
Salem=[20.691668,40.183334,68.833336,114.950005,134.40001,44.86667,81.183334,149.825,122.841675,114.36666,110.30833,67.166664,"Paddy","Turmeric","Sugarcane","Pulses","Groundnut","Gingelly","Coffee"]
Sivaganga=[48.75,29.441668,80.11667,109.86667,138.73332,46.57501,56.058334,110.125,97.33334,154.65,140.40001,108,"Paddy","Sugarcane","Pulses","Groundnut","Cotton"]
Thanjavur=[44.966663,38.25833,64.75833,110.61667,151.1083,43.158337,34.816666,111.908325,132.25835,157.25833,224.54999,154.65833,"Paddy","Sugarcane","Banana","Pulses","Groundnut"]
Theni=[49.84167,14.808333,77.958336,112.19999,110.16668,54.791668,56.008335,63.766666,94.333336,135.38335,139.85834,68.34167,"Paddy","Sugarcane","Cotton","Millets","Pulses"]
Tirunelveli=[36.441666,34.091667,106.25,185.325,155.66667,34.841667,42.75,54.55,80.63334,123.75833,198.28333,110.525,"Paddy","Cotton","Banana","Millets","Groundnut"]
Tiruvallur=[41.720005,25.02,79.61,105.490005,171.99002,63.45,88.43999,105.56,130.45999,179.99002,200.97,106.79,"Paddy","Sugarcane","Millets","Groundnut"]
Tiruvannamalai=[34.524998,18.908333,81.24167,130.9,156.61665,51.59167,94.07499,106.28335,149.24168,121.666664,154.11667,87.54166,"Paddy","Sugarcane","Groundnut","Oil Seeds","Pulses"]
Tiruvarur=[26.875002,13.375,70.183334,108.358345,140.52501,28.791666,39.108334,114.674995,127.783325,177.625,276.35,139.49165,"Paddy","Millets","Pulses"]
Trichy=[10.441667,26.750002,44.38333,103.88333,122.908325,69.924995,51.425,96.80834,110.66668,125.38334,169.13335,132.54167,"Banana","Paddy","Sugarcane","Pulses","Millets"]
Tuticorin=[18.65833,56.3,77.21667,98.88333,95.600006,29.033333,28.1,70.350006,88.083336,121.01666,165.50002,96.958336,"Paddy","Cotton","Millets","Chillies"]
Vellore=[44.025005,7.4083333,72.475,109.80834,144.61668,65.15,79.59167,87.59167,110.75834,90.725,142.19167,96.024994,"Paddy","Millets","Pulses"]
Villupuram=[30.916666,52.491665,66.89167,83.62499,107.50833,52.55833,62.183334,111.23333,106.1,136.12498,254.21667,87.916664,"Paddy","Sugarcane","Groundnut","Millets"]
Virudunagar=[20.591667,21.375,57.391666,47.458332,119.141655,36.325,34.76667,66.87501,43.691666,148.30002,156.92332,65.01667,"Paddy","Cotton","Corn","Groundnut","Gingelly"]
HighRainCrops=["Banana","Chillies","Cotton","Flowers","Fruits","Mango","Paddy","Rice","Sugarcane","Tapioca","Tobacco","Tomato","Turmeric","Vegetables"]
LowRainCrops=["Cashew","Coconut","Coffee","Condiments","Corn","Cotton","Groundnut","Gingelly","Maize","Millets","Oil Seeds","Pulses","Tapioca","Tea"]

rainlevel=99
dict={"January":0,"February":1,"March":2,"April":3,"May":4,"June":5,"July":6,"August":7,"September":8,"October":9,"November":10,"December":11}

choices1 = ['Chennai','Coimbatore','Cuddalore','Dharmapuri','Dindigul','Erode','Kanchipuram','Kanyakumari','Karur','Krishnagiri','Madurai',
           'Nagapatinam','Namakkal','Nilgiri','Perambulur','Pudukottai','Ramanathapuram','Salem','Sivaganga','Thanjavur','Theni',
           'Tirunelveli','Tiruvallur','Tiruvannamalai','Tiruvarur','Trichy','Tuticorin','Vellore','Villupuram','Virudunagar']
choices2 = ["January","February","March","April","May","June","July","August","September","October","November","December"]

root=tk.Tk()

def func(tex):
    return lambda : callback(tex)

def callback(tex):
    root.geometry("%dx%d+%d+%d" % (1000, 500, 180, 100))
    tex.pack(side=tk.RIGHT)
    district = var1.get()
    month = var2.get()
    dist=district
    district = eval(district)
    s1="\n\n   The average rainfall in "+dist+", for the month of "+month+":\n   "+str(district[dict[month]])+".\n\n"
    tex.insert(tk.END,s1)
    if district[dict[month]]>rainlevel:
        s2="   The crops that can be planted in "+dist+" during "+month+":\n   "+str(list(set(district).intersection(HighRainCrops)))
        tex.insert(tk.END,s2)
    else:
        s3="   The crops that can be planted in "+dist+" during "+month+":\n   "+str(list(set(district).intersection(LowRainCrops)))
        tex.insert(tk.END,s3)
    s="\n\n\n               ---X---O---X---O---X---O---X---O---X---\n"
    tex.insert(tk.END,s)
    tex.see(tk.END)
        
root['bg'] = "black"
root.geometry("%dx%d+%d+%d" % (700, 500, 300, 100))
root.title("Program")
tex = tk.Text(master=root)
var1 = tk.StringVar(root)
var2 = tk.StringVar(root)
var1.set("Select a district:")
var2.set("Select a month:")
option1 = tk.OptionMenu(root, var1, *choices1)
option1.pack(side='left',padx=20, pady=20)
option2 = tk.OptionMenu(root, var2, *choices2)
option2.pack(side='left',padx=20, pady=20)
button = tk.Button(root, text="Submit!", command=func(tex))
button.pack(side='left', padx=20, pady=20)
button2 = tk.Button(root, text='Exit', command=root.destroy)
button2.pack(side='left',padx=20,pady=20)
root.mainloop()
