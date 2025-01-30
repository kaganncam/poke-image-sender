# Pokemon WhatsApp Bot

This Python bot fetches Pokemon data from **PokeAPI** and sends images and information to a user via WhatsApp. It includes the following functionalities:

## Features:
- **get_pokemon_info(name)**: Fetches the corresponding Pokemon data from PokeAPI using the provided **Pokemon name**.
- **key_value_check_return(data, spec="")**: Checks if a specified **key** exists in the fetched data and returns its corresponding value if present.
- **get_image(image_url, save_path)**: Downloads the image from the provided URL and saves it to the specified location.
- **send_image_and_caption(phone_number, image_path, caption)**: Sends the downloaded image and caption to the specified WhatsApp number.

The bot fetches data for each Pokemon in the **Pokemon list**, downloads the corresponding images, and sends them via WhatsApp along with a description.

## How It Works:
1. The bot fetches Pokemon data from **PokeAPI** based on a list of Pokemon names.
2. It retrieves details such as **name**, **id**, and **height**.
3. It downloads the **Pokemon image** associated with each Pokemon.
4. The bot then sends the image along with a **formatted message** containing the Pokemon details to a specified **WhatsApp number**.

---

# Pokemon WhatsApp Bot (Türkçe)

Bu Python botu, **PokeAPI**'den Pokemon verilerini çeker ve WhatsApp üzerinden kullanıcıya resimler ve bilgiler gönderir. Aşağıdaki işlevselliklere sahiptir:

## Özellikler:
- **get_pokemon_info(name)**: Verilen **Pokemon ismi** ile PokeAPI'den ilgili Pokemon verilerini çeker.
- **key_value_check_return(data, spec="")**: Çekilen veride belirtilen **anahtarın** var olup olmadığını kontrol eder ve varsa ilgili değeri döndürür.
- **get_image(image_url, save_path)**: Pokemon resimlerinin URL'ini kullanarak resmi indirir ve belirtilen yolda kaydeder.
- **send_image_and_caption(phone_number, image_path, caption)**: İndirilen resmi ve açıklamayı belirtilen WhatsApp numarasına gönderir.

Bot, **Pokemon** listesinde bulunan her bir Pokemon için bilgileri çeker ve ilgili resimleri indirip, açıklama ile birlikte belirttiğiniz numaraya WhatsApp üzerinden gönderir.

## Nasıl Çalışır:
1. Bot, **Pokemon isimleri** listesine göre **PokeAPI**'den Pokemon verilerini çeker.
2. **İsim**, **id** ve **height** gibi bilgileri alır.
3. Her Pokemon için **Pokemon resmi**'ni indirir.
4. Son olarak, bot **resmi ve açıklamayı** belirtilen **WhatsApp numarasına** gönderir.
