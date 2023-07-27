import json
import xmltodict

with open(r"E:\Notepad Python\input_xml.txt") as xml_file:
    parsed_data = xmltodict.parse(xml_file.read())

    xml_file.close()

    json_conversion = json.dumps(parsed_data)

    with open("output_1.json", "w") as json_file:
        json_file.write(json_conversion)

        json_file.close()