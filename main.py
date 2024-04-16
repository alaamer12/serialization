import yaml
import toml
import json
import pickle
import msgpack

# Data to write to files
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland',
    "address": {
        "street": "123 Main St",
        "number": 123,
        "city": "New York"
    }
}


# Write data to YAML file
with open('data.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file)

# Write data to TOML file
with open('data.toml', 'w') as toml_file:
    toml.dump(data, toml_file)

# Write data to JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Read data from YAML file
with open('data.yaml', 'r') as yaml_file:
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print("YAML Data:", yaml_data)

# Read data from TOML file
with open('data.toml', 'r') as toml_file:
    toml_data = toml.load(toml_file)
    print("TOML Data:", toml_data)

# Read data from JSON file
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)
    print("JSON Data:", json_data)

# Write data to pickle file
with open('data.pickle', 'wb') as pickle_file:
    pickle.dump(data, pickle_file)

# Write data to msgpack file
with open('data.msgpack', 'wb') as msgpack_file:
    packed_data = msgpack.packb(data)
    msgpack_file.write(packed_data)

# Read data from pickle file
with open('data.pickle', 'rb') as pickle_file:
    pickle_data = pickle.load(pickle_file)
    print("Pickle Data:", pickle_data)

# Read data from msgpack file
with open('data.msgpack', 'rb') as msgpack_file:
    packed_data = msgpack_file.read()
    msgpack_data = msgpack.unpackb(packed_data, raw=False)
    print("Msgpack Data:", msgpack_data)
