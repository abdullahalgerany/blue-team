# import xml.etree.ElementTree as ET
# tree = ET.parse('pythonday1/data/food.xml')
# root = tree.getroot()
# data=root.findall("food")
# my_foods = []
# for food in data:
#     my_foods.append(
#         {
#             "name": food.findtext("name"),
#             "price": food.findtext("price"),
#             "description": food.findtext("description"),
#             "calories": food.findtext("calories")

#         }
#     )
    
# print(my_foods)
#    # print(menu.tag)
########################################

import re
re.findall