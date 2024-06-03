import secwebapi

# Create a new instance of the SecWebAPI class

secwe_client = secwebapi.Secweb(
    "__USERNAME__",
    "__API_KEY__"
)

# Get the prediction for a single domain
prediction = secwe_client.get("google.com")

# Get the prediction for multiple domains from a file
results = secwe_client.read_domains_from_file("domains.txt")

# Print the results
for domain, prediction in results:
    print(f"Domain: {domain}, Prediction: {prediction}")