import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Specify the model ID of your fine-tuned model
model_id = 'chatcmpl-7TrmSYx5zuAxfGF3421zTyetajBZq'

# Specify the completion ID of the conversation you want to check
completion_id = 'YOUR_COMPLETION_ID'

# Retrieve the completion details
response = openai.ChatCompletion.retrieve(
    model=model_id,
    chat_completion=completion_id
)

# Print the completion details
print(response['choices'][0]['message']['content'])
