from time import sleep
from pandas.core.algorithms import mode
import pandas as pd
from datetime import datetime
import pytz


def time_function():
    caracas_tz = pytz.timezone("America/Caracas") 
    caracas_date = datetime.now(caracas_tz) 
    time_zone = caracas_date.strftime("%d/%m/%y %H:%M:%S")
    print("\n\nFecha de reporte\n\n")
    print("\nCaracas: ",time_zone ) 
    time_zone = caracas_date.strftime("%d_%m_%y_%H%M%S")
    return time_zone


def handler_files(df,m_w): 
    print("\n\nGuardando data \n\n") 
    sleep(2)
    time = time_function()
    name_csv = 'files_data/'+"Reporte_"+time+'.csv'
    df.to_csv(name_csv,mode=m_w)
    print("\n\nArchivo creado: \n\n", name_csv)
    return name_csv


def reading(file):
    df = pd.read_csv(file,index_col=0)
    print("\n",df)


