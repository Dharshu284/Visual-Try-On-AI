import requests
import sys

url = 'http://127.0.0.1:5000/tryon'
person = 'try_img/person_img/my_photo.jpg'
garment = 'try_img/garment_img/jacket_v1.jpg'
output = 'results/test_tryon_result.png'

with open(person, 'rb') as p, open(garment, 'rb') as g:
    files = {
        'person_img': ('my_photo.jpg', p, 'image/jpeg'),
        'garment_img': ('jacket_v1.jpg', g, 'image/jpeg')
    }
    print(f"Posting to {url} with files: {person}, {garment}")
    r = requests.post(url, files=files)
    print('Status:', r.status_code)
    if r.status_code == 200:
        with open(output, 'wb') as out:
            out.write(r.content)
        print(f'Saved result to {output}')
    else:
        try:
            print('Response JSON:', r.json())
        except Exception:
            print('Response text:', r.text)
        sys.exit(1)
