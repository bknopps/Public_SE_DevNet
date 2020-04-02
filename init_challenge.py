#! Python3
import csv

import requests


# TOKEN GOES HERE.
# LAST FOR 12 hours.
# reference this url: https://developer.webex.com/docs/api/v1/memberships/list-memberships
# This page will give you access to how to use the membership api and how to get your token.
USER_TOKEN = "Bearer XXXXXXXXXXXXXXX" # your token goes here

def get_webex_api(room_id="Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli"):
    # pass in different room id's to this function to see the rooms membership data
    url = "https://api.ciscospark.com/v1/memberships"
    querystring = {"roomId": room_id}
    headers = {
        'Authorization': USER_TOKEN,
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

if __name__ == '__main__':
    # Step 1) Get membership data:
    membership_data = get_webex_api()
    # Step 2) create a CSV File
    csv_headers = ["Name", "Email"]
    with open("membership.csv", mode="w") as membership_out:
        writer = csv.DictWriter(membership_out, fieldnames=csv_headers)
        writer.writeheader()
        # Step 3) loop over membership_data and write it to the csv file.
        for member in membership_data["items"]:
            writer.writerow({"Name": member.get("personDisplayName"), "Email": member.get("personEmail")})
    #Done!
