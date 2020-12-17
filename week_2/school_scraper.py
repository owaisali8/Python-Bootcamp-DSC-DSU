import json
import csv
import requests as req

link = 'https://directory.ntschools.net/api/System/GetAllSchools'
api_link = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
response = req.get(link)
json_data = json.loads(response.content)
school_codes = []

for i in json_data:
    school_codes.append(i["itSchoolCode"])

j = 0

for i in school_codes[0:50]:
    school_data = req.get(f'{api_link}{i}')
    parsed_data = json.loads(school_data.content)

    name = parsed_data['name']
    address = parsed_data['physicalAddress']['displayAddress']
    try:
        admin_name = parsed_data['schoolManagement'][1]['firstName'] + \
            " " + parsed_data['schoolManagement'][1]['lastName']
        admin_position = parsed_data['schoolManagement'][1]['position']
        admin_email = parsed_data['schoolManagement'][1]['email']
        phone_no = parsed_data['schoolManagement'][1]['phone']
    except IndexError:
        admin_name = parsed_data['schoolManagement'][0]['firstName'] + \
            " " + parsed_data['schoolManagement'][0]['lastName']
        admin_position = parsed_data['schoolManagement'][0]['position']
        admin_email = parsed_data['schoolManagement'][0]['email']
        phone_no = parsed_data['schoolManagement'][0]['phone']

    with open("school_data.csv", 'a', newline='') as file:
        file_writer = csv.DictWriter(file, fieldnames=[
            "Name", "Address", "Principal/Admin Name", "Principal/Admin Position", "Principal/Admin Email", "School Telephone number"])
        file_writer.writerow({'Name': name, 'Address': address, 'Principal/Admin Name': admin_name,
                              "Principal/Admin Position": admin_position, "Principal/Admin Email": admin_email, "School Telephone number": phone_no})
    print(j)
    j += 1

print("Done!")
