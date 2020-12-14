from io import BytesIO
# from pdfreader import PDFDocument, SimplePDFViewer
import tabula

file_name = '/Users/griffinmfalme/Dev/projects/anc/home/pdf/centers.pdf'

json_file = '/Users/griffinmfalme/Dev/projects/anc/home/pdf/centers.json'

# fd = open('/Users/griffinmfalme/Dev/projects/anc/home/pdf/centers.pdf', 'rb')


# doc = PDFDocument(fd)
# with open(file_name, "rb") as f:
#     stream = BytesIO(f.read())
# doc2 = PDFDocument(stream)
# print(doc.header.version)
# print(doc.root.Outlines.First['Title'])


# # tabula
df = tabula.read_pdf(file_name, output_format='json',
                     lattice=True, pages="all")


f = open(json_file, "a")
print(df)
data_read = df[0]['data']
county_data = {}
counties = []

for value, inf in enumerate(df):
    counties.append(df[value]['data'])

# this reads all the data in the first page well and prints it well
for value, inf in enumerate(data_read):
    if value > 6:
        counties.append(inf)


county_data['counties'] = counties
f.write(str(county_data))
f.close()
# for i, v in enumerate(counties):
#     if(v[0]['text'] not in county_data.keys()):
#         county_data[v[1]['text']] = county_data[v[2]['text']]
