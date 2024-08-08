import base64
import cloudscraper
import json
import requests

# Convert NFT metadata to base64
def encode_to_base64(nft_metadata):
    # Convert the NFT's metadata data to bytes
    nft_data_bytes = nft_metadata.encode('utf-8')
    # Encode the bytes to a base64 string
    base64_message = base64.b64encode(nft_data_bytes).decode('utf-8')
    return base64_message

# Inspect the base64 message using Solscan API
def inspect_base64_message(base64_message):
    url = "https://api.solscan.io/tools/inspect"
    params = {
        "message": base64_message
    }
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

# NFT metadata as a JSON string
nft_metadata = '''
{
  "name": "Cet #5059",
  "symbol": "CoC",
  "description": "",
  "seller_fee_basis_points": 888,
  "image": "https://shdw-drive.genesysgo.net/3tPEmShThSrDVM364dUJPLjKCQMGScdPEP3XxgWgN2Xo/42Pymg6NiqDNCAqnqwdWb3L44sfpo8M58sHFVj9mmMqF.png",
  "external_url": "",
  "edition": 5058,
  "attributes": [
    {
      "trait_type": "Background",
      "value": "Blue"
    },
    {
      "trait_type": "Skin",
      "value": "Irezumi tatt"
    },
    {
      "trait_type": "Clothing",
      "value": "Furreal coat"
    },
    {
      "trait_type": "Mouth",
      "value": "Go fetch"
    },
    {
      "trait_type": "Eye",
      "value": "Oldy specs"
    },
    {
      "trait_type": "Headgear",
      "value": "Creck cap"
    }
  ],
  "properties": {
    "files": [
      {
        "uri": "5058.png",
        "type": "image/png"
      }
    ],
    "category": "image",
    "creators": [
      {
        "address": "9Da5CoqR8H4YGWEYK6jtcTU69rr6XEkffadN8UFjJkeA",
        "share": 30
      },
      {
        "address": "73sKMbDcc8Tze8h8wRKu22jS93NUvq6CwbDfwJPoNAX4",
        "share": 20
      },
      {
        "address": "HMWMLwEcnQBR57yhsyyAhfavzac8vZbx1m4EPtYEdKkM",
        "share": 30
      },
      {
        "address": "4qcJowy8guEuJ1RJx9XDxyneP3H12XTT19nZ7YaVjaFr",
        "share": 20
      }
    ]
  },
  "collection": {}
}
'''
# Encode the metadata to base64
base64_message = encode_to_base64(nft_metadata)
print("Base64 Message:", base64_message)

# Inspect the base64 message using Solscan API
inspection_result = inspect_base64_message(base64_message)
print("Inspection Result:", inspection_result)