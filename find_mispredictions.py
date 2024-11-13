import json

with open('./eval_output/eval_predictions.jsonl', 'r') as jfile:
    jsonl = list(jfile)

for obj in jsonl:
    prediction = json.loads(obj)

    gold, predicted = prediction['label'], prediction['predicted_label']
    if gold != predicted:
        if abs(predicted-gold) > 1:
            prediction['category'] = 'False Positive' if prediction == 0 else 'False Negative'
        else:
            prediction['category'] = 'Neutral'
        print(json.dumps(prediction))
