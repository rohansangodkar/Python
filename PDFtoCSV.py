import tabula
df = tabula.read_pdf("/Users/rohan/Desktop/CIF form.pdf", pages = 1)

tabula.convert_into("/Users/rohan/Desktop/CIF Form.pdf", "iplmatch.csv", output_format="csv", pages='all')
print(df)
