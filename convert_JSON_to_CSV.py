import json

if __name__ == "__main__":
    try:
        # Input file
        with open(r"C:\Users\Mittesh Waghule\Downloads\input.json", "r") as f:
            data = json.loads(f.read())

        output = ",".join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
        # Output file
        with open("output.csv", "w") as f:
            f.write(output)
    except Exception as ex:
        print(f"Error: {str(ex)}")