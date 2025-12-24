import json

with open("data.json", "r") as file:
    characters = json.load(file)

character_info = {
    "gojo": characters["gojo"],
    "itachi": characters["itachi"],
    "naruto": characters["naruto"],
    "daniel_park": characters["daniel_park"],
    "gun_yamazaki": characters["gun_yamazaki"],
    "vasco": characters["vasco"],
    "jay": characters["jay"],
    "jace": characters["jace"],
    "luffy": characters["luffy"],
    "zoro": characters["zoro"],
    "sanji": characters["sanji"],
    "nami": characters["nami"],
    "robin": characters["robin"],
    "brook": characters["brook"],
    "chopper": characters["chopper"],
    "gold_roger": characters["gold_roger"]
}
