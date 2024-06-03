## Secwe AI Client

Secwe AI Client is a Python library for interacting with the Secwe AI API. 
It provides a simple interface for sending and receiving data from the Secwe AI API.

This library is designed to be easy to use and to provide a malicious web-app detection service for your applications.

## Installation

To install the Secwe AI Client, you can use pip:

```bash
pip install secwebapi
```

## Usage

To use the Secwe AI Client, you need to have an API key.
You can get an API key by signing up at [SecWe AI-Powered Detection](https://secwe.com.tr).

Here is an example of how to use the Secwe AI Client:

```python
import secwebapi

# Create a client
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
```

