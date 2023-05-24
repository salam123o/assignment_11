import pandas as pd
boy1=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\boysname.xls")
print(boy1)
girl2=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\girlsname.xls")
print(girl2)
app_frnd=pd.concat([boy1,girl2],axis=0,ignore_index=True)
print(app_frnd)


import pandas as pd
boy3=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\boysname.xls")
#print(boy3)
girl4=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\girlsname.xls")
#print(girl4)
app_frnd2=pd.concat([boy3,girl4],axis=1)
print(app_frnd2)

import pandas as pd
fatherside=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\fatherfamily_members.xls")
#print(fatherside)
motherside=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\montherfamily_members.xls")
#print(motherside)
app_family=pd.concat([fatherside,motherside],axis=0,ignore_index=True)
print(app_family)

import pandas as pd
sisters=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\Sisters.xls")
#print(sisters)
brothers=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\Brothers.xls")
#print(brothers)
app_sister_bro=pd.concat([sisters,brothers],axis=1)
print(app_sister_bro)

import pandas as pd
dal=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\dal_items.xlsx")
#print(dal)
vegitable=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\vegitable_items.xlsx")
#print(vegitable)
app_dal_veg=pd.concat([dal,vegitable],axis=0,ignore_index=True)
print(app_dal_veg)

import pandas as pd
soup=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\soups_items.xlsx")
#print(soup)
fry=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\fry_items.xlsx")
#print(fry)
app_soup_fry=pd.concat([soup,fry],axis=1)
print(app_soup_fry)

import pandas as pd
chicken=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\chicken_items.xlsx")
#print(chicken)
mutton=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\mutton_items.xlsx")
#print(mutton)
app_chic_moutt=pd.concat([chicken,mutton],axis=0,ignore_index=True)
print(app_chic_moutt)

import pandas as pd
winter=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\winterseason_names.xlsx")
#print(winter)
summer=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\summerseason_names.xlsx")
#print(summer)
rainy=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\rainyseason_names.xlsx")
#print(rainy)
app_all_seasons=pd.concat([winter,summer,rainy],axis=0,ignore_index=True)
print(app_all_seasons)

import pandas as pd
red=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\redflowers_names.xlsx")
#print(red)
white=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\whiteflowers_names.xlsx")
#print(white)
pink=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\pinkflower_names.xlsx")
#print(pink)
yellow=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\yellowflower_names.xlsx")
#print(yellow)
app_all_flower=pd.concat([red,white,pink,yellow],axis=0,ignore_index=True)
print(app_all_flower)








