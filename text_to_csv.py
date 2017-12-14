import csv

txt_file = r"/home/dalchemy/Data_Anju/apr26_30.txt"
csv_file = r"/home/dalchemy/Data_Anju/apr26_30.csv"

in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'wb'))

out_csv.writerows(in_txt)




