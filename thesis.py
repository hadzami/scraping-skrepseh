import requests
from typing import cast
import schema

url = "https://etd.repository.ugm.ac.id/home/do_pencarian_advance"

payload = "draw=6&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=99999999999999999999&search%5Bvalue%5D=&search%5Bregex%5D=false&key_one=penJudul&keyword_one=&logic_two=AND&key_two=penJudul&keyword_two=&logic_three=AND&key_three=penJudul&keyword_three=&sort=desc&thn_awal=1990&thn_akhir=2025&filter_jenis%5B%5D=3&asal_instansi%5B%5D=5236"
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'pll_language=id; s_fid=5162BF82AE5FBD9F-2A471DA52BBDF08C; _gcl_au=1.1.1573116868.1729925895; _ga_N9Z0RY7XEN=GS1.1.1729925895.1.1.1729925942.0.0.0; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=179643557%7CMCIDTS%7C20023%7CMCMID%7C00580606415161250888413414557071390433%7CMCAID%7CNONE%7CMCOPTOUT-1730007856s%7CNONE%7CvVersion%7C5.5.0; s_pers=%20v8%3D1730000656246%7C1824608656246%3B%20v8_s%3DLess%2520than%25201%2520day%7C1730002456246%3B%20c19%3Dsd%253Apdfft%253Apdf%253Aurl%7C1730002456248%3B%20v68%3D1730000655782%7C1730002456250%3B; __gads=ID=e611d1b187fb3898:T=1729927788:RT=1730390841:S=ALNI_MZcVaBBWnBBLhuQWCbbeTg7uQjmSw; __gpi=UID=00000f5662ffdcfe:T=1730001016:RT=1730390841:S=ALNI_Mb5NNfLnUXY4MePmE0OW-6MX3juWQ; __eoi=ID=5ec25cf942632132:T=1729927788:RT=1730390841:S=AA-AfjZ6hexHSY3QYiDmEmwUs-EE; _rollupGA=GA1.3.328363876.1729925583; wisepops=%7B%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A43%2C%22cid%22%3A%222914%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_visits=%5B%222024-10-31T16%3A07%3A23.191Z%22%5D; wisepops_visitor=%7B%22FOt6c31007%22%3A%223d1a34d8-0f61-4b16-93e3-171d9360e5df%22%7D; _ga_EXTSVLH45V=GS1.1.1730390843.1.1.1730390913.0.0.0; _ga_L4JC39NX24=GS1.1.1730430336.8.0.1730430336.0.0.0; _ga_EZ13HM83FM=GS1.1.1730430336.8.0.1730430336.60.0.0; _ga_WPG9ZXVEGK=GS1.1.1730430336.8.0.1730430336.0.0.0; _gid=GA1.3.1258600854.1730521232; ugmfw_sessions=une062qhoikard6i6v9818fg844tub2t; _ga_WK4RVDYE24=GS1.1.1730521231.2.1.1730521677.3.0.0; _ga=GA1.1.328363876.1729925583; ugmfw_sessions=une062qhoikard6i6v9818fg844tub2t',
  'Origin': 'https://etd.repository.ugm.ac.id',
  'Referer': 'https://etd.repository.ugm.ac.id/home/result_pencarianlanjut/search?key_one=penJudul&keyword_one=sistem&logic_two=AND&key_two=penJudul&keyword_two=&logic_three=AND&key_three=penJudul&keyword_three=&tahunawal=2020&tahunakhir=2024&jeniskarya=&prodi=',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = requests.request("POST", url, headers=headers, data=payload)
response_json = response.json()

api_response: schema.ApiResponse = cast(schema.ApiResponse, response_json)

schema.generate_csv(api_response['data'], "irfan.csv")