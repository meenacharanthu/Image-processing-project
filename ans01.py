import csv
import os
import re
import temp2
from fpdf import FPDF
from datetime import date
from datetime import datetime

directory = os.getcwd()
destination_folder = 'transcriptsIITP'
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

destination = os.path.join(os.getcwd(), "transcriptsIITP")






def list_generation(ran, stamp):
    # ran = ' 0401CS01 - 0401CS02 '

    temp2.fcallll(ran, stamp)
    

    


# list_generation('0401cs01-  0401cs04','ok','ok')
