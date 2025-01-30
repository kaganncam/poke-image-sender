import time
import requests
import pywhatkit as wp
BASE_URL = "https://pokeapi.co/api/v2/"

# Pokemon ismininden json çeken fonskiyon
def get_pokemon_info(name):
    url = f"{BASE_URL}/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Hata {response.status_code} ,{name} bilgisis alınamadı")
        return None
# Key,value uygun türde ve var olup olmadığını deneyen fonksiyon
def key_value_check_return(data,spec = ""):
    if isinstance(data,dict) and spec in data:
        return data[spec]
    else:
        print(f"{spec} yok")
        return None
#resmi indiren fonskiyon
def get_image(image_url,save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open("""C:/Users/kagan/Downloads/indirilen_resim.png""","wb") as file:
            file.write(response.content)
            print(f"Resim indirilidi path:{save_path}")
            return save_path
    else:
        print(f"Resim indirilemedi :{response.status_code}")
        return  None
# Resim ve başlıkla gönderen fonksiyon
def send_image_and_caption(phone_number,image_path,caption):
    wp.sendwhats_image(phone_number, image_path, caption, 15, True, 6)




pokemon_list = [
     "Weedle", "Kakuna", "Beedrill",
    "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
    "Pikachu", "Raichu", "Sandshrew",
    "Nidorina", "Nidoqueen","Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff",
]
IMAGE_PATH = """C:/Users/"""
PHONE_NUMBER = ""

for pokemon in pokemon_list:
    data = get_pokemon_info(name=pokemon)
    time.sleep(5)
    if not data:
        continue
    # pokemon değiskenleri
    pokemon_id =key_value_check_return(data,"id")
    pokemon_name =key_value_check_return(data,"name")
    pokemon_height =key_value_check_return(data,"height")
    formatted_text = f"""Pokemons ===Pokemon Name :{pokemon_name}  , Pokemon id :{pokemon_id}   
    ,Pokemon height :{pokemon_height} """
    # pokemon resimlinleri
    pokemon_sprites =key_value_check_return(data,"sprites")
    pokemon_front_url =key_value_check_return(pokemon_sprites,"front_default")

    downloaded_image = get_image(pokemon_front_url,IMAGE_PATH)
    try:
        if downloaded_image:
            send_image_and_caption(phone_number=PHONE_NUMBER,image_path=IMAGE_PATH,caption=formatted_text)
        else:
            pass
    except Exception as e:
        print(f"Hata {e}")

    time.sleep(4)#opsiyonel




