import pyexcel
from collections import OrderedDict

data = [
    OrderedDict({
        "Name" : "Loc",
        "Age" : 24,
    }),
    OrderedDict({
        "Name" : "Huy",
        "Age" : 30,
    }),
    OrderedDict({
        "Name" : "Quan",
        "Age" : 24,
    }),
]

pyexcel.save_as(records=data, dest_file_name="your_file.xlsx")