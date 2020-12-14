import json
json_file = '/Users/griffinmfalme/Dev/projects/anc/home/pdf/centers.json'
our_file = open(json_file, 'r')
# print(type(list(our_file.read())))
data = json.loads(our_file.read())
# print(our_file.read()[2])
counties = {}
constituencies = []
constituency = {

}
polling_stations = []
# print(data)

print(len(data['counties'][0]))
for i, v in enumerate(data['counties'][0]):
    county_name = v[1]['text']
    county_constituency = v[3]['text']
    polling_station = v[7]['text']
    # print(counties)
    # if i > 2:
    #     print(i)
    #     break
    try:
        # print('county number', v[3]['text'])
        # print(county_name)
        # print('county name', v[1]['text'])
        # print('constituency name', v[3]['text'])
        # print('polling center name', v[7]['text'])
        # print(i)
        if county_name in counties:
            print(counties.keys())
            counties[county_name][county_constituency].append(polling_station)
            print('county name already exists and constituency added' +
                  str(county_name) + str(polling_station))

        else:
            print('sth went wrong', county_name)

            # counties[county_name].update(
            #     {county_constituency: [polling_station]})
            # counties[county_name][county_constituency] = [polling_station]
            counties[county_name] = {county_constituency: [polling_station]}
            # print(v)
            # polling_stations.append()
            # if v[1]['text'] in counties.keys():
            #     for values in counties[v[1]['text']]:
            #         print(counties[v[1]['text']].keys())

            #         if v[3]['text'] in counties[v[1]['text']].keys():
            #             counties[v[1]['text']][v[3]['text']].append(v[7]['text'])
            #             print('county name', v[1]['text'])
            #             print('constituency name', v[3]['text'])
            #             print('polling center name', v[7]['text'])
            #     else:
            #         counties[v[1]['text']][v[3]['text']] = [v[7]['text']]

        print('\n')

    except Exception as e:
        counties[county_name][county_constituency] = [polling_station]
        print("Error occured", e)
    # if v[0][1]['text'] in counties:

print(counties)

# print(counties[0][2][3]['text'])
# print(counties[0][2][3]['text'])
# for index, value in counties:
#     print(index, type(value))
# print(type(data['counties']))
# try:
#     for no, value in v:
#         pass
#         # print(type(value[no]['text']))
# except:
#     print('error occured')
