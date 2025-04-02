# Fill in this file with the code from parsing JSON exercise
import json
import yaml

with open('myfile_12250124.json', 'r') as json_file:
    ourjson = json.load(json_file)

#print(ourjson)

#print("The access token is: {}".format(ourjson['access_token']))
#print("The token expires in {} seconds.".format(ourjson['expires_in']))
print("This was made by {}".format(ourjson['my_name']))
print("This modification was added from the 12250124_branch as part of the other lag assignment")

#print("\n\n---")
#print(yaml.dump(ourjson))
