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
az ad sp create-for-rbac --name <ServicePrincipalName>
```

Output: 
```sh
{
  "appId": "**************************",
  "displayName": "**************************",
  "name": "**************************",
  "password": "**************************",
  "tenant": "**************************
}
```

## Set Environment Variables

```
export AZURE_CLIENT_ID=<appId>

export AZURE_CLIENT_SECRET=<password>

export AZURE_TENANT_ID=<tenant>

export KEY_VAULT_NAME=<your-key-vault-name>
```

Source: https://docs.microsoft.com/en-us/azure/key-vault/quick-create-python