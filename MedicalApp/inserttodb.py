import csv,os
from MedicalApp.models import MedicalData
from pathlib import Path
def insertData():
    BASE_DIR = Path(__file__).resolve().parent.parent
    filename = (os.path.join(BASE_DIR,"/static/files/meddata.csv"))
    file = open(filename, 'r')
    lines = list(csv.reader(file))
    return lines[1:]
