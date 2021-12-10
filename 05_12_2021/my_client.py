import requests

response = requests.post("http://localhost:5001/whatismyname")
expected = "saved new car"
actual = response.text
print(actual)
assert expected == actual
