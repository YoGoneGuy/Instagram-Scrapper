import httpx
from pathlib import Path
from datetime import datetime 

username = input("enter target username")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36",
    "X-IG-App-ID": "936619743392459",
}

url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"

response = httpx.get(url, headers=headers)

data = response.json()

user = data["data"]["user"]





#--------------------------------------------------------------
# print("Name:", user["full_name"])
# print("Bio:", user["biography"])
# print("Followers:", user["edge_followed_by"]["count"])
# print("Profile pic URL:", user["profile_pic_url_hd"]) 
#-----------------------------------------------------------------

pfp_url= user["profile_pic_url_hd"]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{username}_{timestamp}"

Path("downloads").mkdir(exist_ok=True)
image= httpx.get(pfp_url, headers=headers)
Path(f"downloads/{filename}.jpg").write_bytes(image.content)

print("completed, check dowmloads folder ")
