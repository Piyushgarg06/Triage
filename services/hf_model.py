from transformers import pipeline
classifier = pipeline('sentiment-analysis')
result = classifier("My car was damaged badly")
claims = [
    "i was rescued while hanging on a cliff while my car fell down the cliff and got completely thrashed",
    "my car was stolen yesterday",
    "my car exploded due to some problem in Air Conditioning vents",
]
for claim in claims:
    res = classifier(claim)
    print(res)