# Azure Key Vault

## Prerequisites
1. Create Resource Group

```sh
az group create --name "myResourceGroup" -l "EastUS"
```

2. Create Key Vault

```sh
az keyvault create --name <your-unique-keyvault-name> -g "myResourceGroup"
```

3. Create a service principal

```sh
az ad sp create-for-rbac -n "http://mySP" --sdk-auth
```

Source: https://docs.microsoft.com/en-us/azure/key-vault/quick-create-python