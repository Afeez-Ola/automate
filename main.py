import pandas as pd

x_list = [-73.0, 256.0, -55.0, -119.0, 69.0, -179.0, 5.0, 313.0, -12.0, -186.0, -46.0, -184.0, -223.0, -85.0, -104.0,
170.0, -112.0, 58.0, -62.0, -15.0, -82.0, -314.0, -136.0, -270.0, -363.0, -39.0, -201.0, -367.0, -255.0,
-280.0, -346.0, 65.0, -123.0, -217.0, 143.0, 185.0, -156.0]
y_list = [-235.0, 36.0, -289.0, -200.0, 98.0, -296.0, -112.0, 206.0, -215.0, -238.0, -186.0, -161.0, -85.0, -177.0,
-13.0, 87.0, -234.0, 231.0, 78.0, 197.0, 235.0, 193.0, -95.0, -17.0, -172.0, -32.0, 44.0, -141.0, -142.0,
-103.0, -49.0, 1.0, -282.0, 287.0, -66.0, 216.0, 218.0]

states = ['Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River', 'Delta',
'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Abuja', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina',
'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers',
'Sokoto', 'Taraba', 'Yobe', 'Zamfara']

data = {"state": states, "x": x_list, "y": y_list}
data_table = pd.DataFrame(data=data)
data_table.to_csv("state.csv")