import csv
import json

# Set the input and output filenames
input_filename = 'scenarios_moralchoice_low_ambiguity.csv'
output_filename = 'scenarios_moralchoice_low_ambiguity_cleaned.jsonl'

# Open the input CSV file and process each row
with open(input_filename, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    with open(output_filename, mode='w', newline='') as jsonlfile:
        for row in reader:
            # Ensure 'context', 'action1', and 'action2' are present in the row
            if 'context' in row and 'action1' in row and 'action2' in row:
                context = row['context'].replace("'", "").strip()
                action1 = row['action1'].replace("'", "").strip()
                action2 = row['action2'].replace("'", "").strip()
                
                # Create the prompt object
                prompt = f"{context} Choice 1: {action1} Choice 2: {action2}"
                prompt_object = {'prompt': prompt}
                
                # Write the JSON object to the file
                jsonlfile.write(json.dumps(prompt_object) + '\n')

print(f'Output saved to {output_filename}')