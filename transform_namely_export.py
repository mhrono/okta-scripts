#!/usr/bin/env python3

"""
 Copyright 2022 Buoy Health, Inc.

 Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.

 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
"""

## Author: Matt Hrono
## MacAdmins: @matt_h

import csv
from datetime import datetime
from pathlib import Path

"""
Namely can export a csv of employees for import into Okta for user provisioning
Unfortunately, Okta can't parse the data as it's exported from Namely
Given a Namely export csv as input, this script will read the data and export the required fields to a new csv
This output file can be uploaded to Okta for provisioning of new employee accounts
"""

# Set some vars and take in the input file
input_file = str(Path(input('Drag and drop exported csv from Namely: ').rstrip().replace("\\", "")).expanduser())
output_file = str(Path(f'~/Desktop/namely_okta_transform_{datetime.now().strftime("%Y-%m-%d")}.csv').expanduser())
fieldnames = ['login', 'firstName', 'lastName', 'middleName', 'honorificPrefix', 'honorificSuffix', 'email', 'title', 'displayName', 'nickName', 'profileUrl', 'secondEmail', 'mobilePhone', 'primaryPhone', 'streetAddress', 'city', 'state', 'zipCode', 'countryCode', 'postalAddress', 'preferredLanguage', 'locale', 'timezone', 'userType', 'employeeNumber', 'costCenter', 'organization', 'division', 'department', 'managerId', 'manager']

with open(input_file, mode='r') as in_file, open(output_file, mode='w') as out_file:
	csv_reader = csv.DictReader(in_file)
	line_count = 0
	writer = csv.DictWriter(out_file, fieldnames=fieldnames)
	writer.writeheader()
	for row in csv_reader:
		line_count += 1
		print(f'Processing {row["Full Name"]}...')
		# Relevant data from the Namely export
		writer.writerow({'login': row["Email"], 'firstName': row["First name"], 'lastName': row["Last name"], 'email': row["Email"], 'title': row["Job Title"], 'displayName': row["Full Name"], 'nickName': row["Preferred name"], 'secondEmail': row["Personal email"], 'city': row["Office Location"], 'userType': row["Employee type"], 'employeeNumber': row["Employee number"], 'division': row["Division"], 'department': row["Department"], 'managerId': row["Reports To Email"], 'manager': row["Reports To Email"]})
	print(f'\nTransformed {line_count} lines.\n')
	print(f'Okta-compatible csv output to {output_file}')