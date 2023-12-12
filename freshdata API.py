import requests

url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

querystring = {"linkedin_url":"https://www.linkedin.com/in/benjamin-david-auer/","include_skills":"false"}

headers = {
	"X-RapidAPI-Key": "a7d95ce70fmsh77213dac6ebbcbdp123c2djsn5845994ca213",
	"X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())