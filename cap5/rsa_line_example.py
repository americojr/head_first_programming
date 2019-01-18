# Example

line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"

s = {}

(s["ID"],s["Name"],s["Country"],s["Average"],s["Board_type"],s["Age"]) = line.split(";")

print("ID:          "+s["ID"])
print("Name:        "+s["Name"])
print("Country:     "+s["Country"])
print("Average:     "+s["Average"])
print("Board type:  "+s["Board_type"])
print("Age:         "+s["Age"])
