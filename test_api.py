import requests

response = requests.get('http://127.0.0.1:8000/health')
print(response.json())

claim_data = {
    'claim_id' : '12345678',
    'description' : 'been in a huge accident',
    'claim_type' : 'accident',
    'audio_file_path' : None
}
post = requests.post('http://127.0.0.1:8000/claim', json=claim_data)
print(post.json())
file = {'file' : open("uploads/PKG_Elite_Planner_V2.pdf", 'rb')}


post_file = requests.post('http://127.0.0.1:8000/claim/upload', files=file)
print(post_file.json())