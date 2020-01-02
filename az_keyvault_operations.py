import os
import cmd
import uuid
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = os.environ["KEY_VAULT_NAME"]
KVUri = "https://" + keyVaultName + ".vault.azure.net"

key_value_pair = {}

key_value_pair['key1'] = 'value1'
key_value_pair['key2'] = 'value2'

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = str(uuid.uuid4())
secretValue = "secretValue"

# Set secret
client.set_secret(secretName, key_value_pair)

# Retrieve secret
retrieved_secret = client.get_secret(secretName)
print("Your secret is '" + retrieved_secret.value + "'.")

# Delete Secret
# client.delete_secret(secretName)
