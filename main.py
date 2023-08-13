import requests
import json
from bs4 import BeautifulSoup


def get_country_phone_id() -> dict:
	response = requests.get("https://countrycode.org")
	content = BeautifulSoup(response.text, "html.parser")
	phones = {}

	for tr in content.find("table").find("tbody").find_all("tr"):
		td = tr.find_all("td")
		code = td[1].text.split(",")

		for x in code:
			phones.setdefault("+" + x.strip(), {
				"country_name": td[0].find("a").text.strip(),
				"country_iso2": td[2].text.split("/")[0].strip(),
				"country_iso3": td[2].text.split("/")[1].strip()
			})

	return phones


def main():
	result = get_country_phone_id()

	with open("phone_id.json", "w") as file:
		file.write(json.dumps(result, indent=4, ensure_ascii=False))
		file.close()


if __name__ == "__main__":
	main()
	print("COUNTRY PHONE ID SUCCESSFULLY DOWNLOADED")
