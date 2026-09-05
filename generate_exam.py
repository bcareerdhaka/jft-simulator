import csv
import json
import random

def generate_questions(csv_file):
    vocab = []
    # Read the CSV data
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row
        for row in reader:
            if len(row) >= 2:
                vocab.append({"word": row[0], "meaning": row[1]})
    
    questions = []
    # Generate a question for each word
    for item in vocab:
        correct = item["meaning"]
        # Pick 3 wrong answers randomly
        wrong_options = [v["meaning"] for v in vocab if v["meaning"] != correct]
        # Ensure we don't crash if the CSV is too small
        distractors = random.sample(wrong_options, min(3, len(wrong_options)))
        
        all_options = distractors + [correct]
        random.shuffle(all_options)
        correct_index = all_options.index(correct)
        
        questions.append({
            "q": f"この 言葉の 意味を 選んでください。<br><br><span style='font-size: 2rem; border: 1px solid #ccc; padding: 10px; display: inline-block;'>{item['word']}</span>",
            "options": all_options,
            "answer": correct_index
        })
    
    # Save the output directly as a JSON file
    with open('vocab_questions.json', 'w', encoding='utf-8') as out:
        json.dump(questions, out, ensure_ascii=False, indent=4)
    print("Successfully generated vocab_questions.json!")

if __name__ == "__main__":
    generate_questions('irodori_vocab.csv')
