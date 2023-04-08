import openai
import os
# import requests
import json

""" openai.api_type = "azure_ad"
# NOTE: this token has a lifetime of ~2 hours
openai.api_key = token # generated using `az login`
openai.api_base = https://altana-sandbox.openai.azure.com
openai.api_version = "2022-12-01" """

openai.api_key = "872696230c214e1eabfbcf71f06ff333"
openai.api_base =  'https://mm-openai.openai.azure.com'
openai.api_type = 'azure'
openai.api_version = '2023-03-15-preview' # this may change in the future

print(openai.Deployment.list())


response = openai.ChatCompletion.create(
    engine="chatgpt", 
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."}  
    ],
    temperature=0,
    frequency_penalty=2,
    presence_penalty=2
)
#new response
print(response)
print(response['choices'][0]['message']['content'])
