import os
import pandas as pd
from ydata_profiling import ProfileReport

data_path = '/Users/victordashuaibi/Desktop/is477-fall2023-final-project/data/car.csv'
col = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
profiling_directory = "/Users/victordashuaibi/Desktop/is477-fall2023-final-project/profiling"

df = pd.read_csv(data_path,header=None,names=col)
profile = ProfileReport(df, title="Profiling Report")

report_path = os.path.join(profiling_directory, "report.html")
profile.to_file(report_path)