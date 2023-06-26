import json
import openai
import signal
import datetime
import time

# Set up your OpenAI API credentials
openai.api_key = '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'

# Preparing the data from jsonl to list of preparation data
training_file_name = "/Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/resources/data_prepared_prepared.jsonl"
training_data = {}


def prepare_data(dictionary_data, final_file_name):
    with open(final_file_name, 'w') as outfile:
        for entry in dictionary_data:
            json.dump(entry, outfile)
            outfile.write('\n')


prepare_data(training_data, "training_data.jsonl")

# Uploading the file to OpenAI to fine tune  the model
purpose = 'fine-tune'
training_file_id = openai.File.create(file=open(training_file_name), purpose=purpose)
print(f"Training File ID: {training_file_id}")
print(training_file_id['id'])
# Creating a fine tune job
create_args = {
    "training_file": training_file_id['id'],
    "model": "davinci",
    "n_epochs": 15,
    "batch_size": 3,
    "learning_rate_multiplier": 0.3
}

response = openai.FineTune.create(**create_args)

print("Rajaji")
print(response.__dict__)
job_id = response["id"]
status = response["status"]

print(f'Fine-tunning model with jobID: {job_id}.')
print(f"Training Response: {response}")
print(f"Training Status: {status}")


# checking the fine tune job status
def signal_handler(sig, frame):
    status = openai.FineTune.retrieve(job_id).status
    print(f"Stream interrupted. Job is still {status}.")
    return


print(f'Streaming events for the fine-tuning job: {job_id}')
signal.signal(signal.SIGINT, signal_handler)

events = openai.FineTune.stream_events(job_id)
try:
    for event in events:
        print(f'{datetime.datetime.fromtimestamp(event["created_at"])} {event["message"]}')

except Exception:
    print("Stream interrupted (client disconnected).")

# TIll above codee is enough for creation of fine tune