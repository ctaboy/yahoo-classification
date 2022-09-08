#!/usr/bin/env python
from fairseq import checkpoint_utils, data, options, tasks

CORPUS = 'answers-bin/test.input-label.input'
CORRECT_LABEL = 'answers-bin/test.input-label.label'

# Parse command-line arguments for generation
parser = options.get_generation_parser(default_task='simple_classification')
args = options.parse_args_and_arch(parser)

# Setup task
task = tasks.setup_task(args)

# Load model
print('| loading model from {}'.format(args.path))
models, _model_args = checkpoint_utils.load_model_ensemble([args.path], task=task)
model = models[0]

while  True:
    with open(CORPUS, 'r') as source_corpus, open(CORRECT_LABEL, 'r') as source_label:
        correct_labels = 0
        total_labels = 0

        # Iterate over each sentence in test file & each correct label in label file:
        for sentence, correct_label in zip(source_corpus, source_label):                                                    
                
            # TODO: if the following line is run, it assumes the data
            # is character-level but not yet tokenized, and replaces
            # space with underscore.
            # E.g., if the input is "foo bar", it is converted to
            # "f o o _ b a r".
            # If it is not run, it assumes the data is already
            # space-delimited.
            # sentence = " ".join(sentence.replace(" ", "_"))
            print(sentence)
            print(f'Correct Label: {correct_label}')

            tokens = task.source_dictionary.encode_line(
                sentence, add_if_not_exist=False,
            )

            # Build mini-batch to feed to the model.
            batch = data.language_pair_dataset.collate(
                samples=[{'id': -1, 'source': tokens}],  # bsz = 1
                pad_idx=task.source_dictionary.pad(),
                eos_idx=task.source_dictionary.eos(),
                left_pad_source=False,
                input_feeding=False,
            )

            # Feed batch to the model and get predictions
            preds = model(**batch['net_input'])

            # Print top prediction and its log-probability
            top_scores, top_labels = preds[0].topk(k=1)      # I changed k=3 to k=1 to return top prediction
            for score, label_idx in zip(top_scores, top_labels):
                label_name = task.target_dictionary.string([label_idx])
                print('({:.2f})\t{}'.format(score, label_name))
            print()

            # Calculate accuracy
            if label_name.strip() == correct_label.strip():
                correct_labels += 1
                total_labels += 1
            else:
                total_labels += 1

        if total_labels == 800:
            break

print(f'Correct: {correct_labels}\nTotal: {total_labels}')
print(f'Accuracy: {(correct_labels / total_labels) * 100}')

