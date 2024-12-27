import os
import glob
from collections import defaultdict, Counter
import re

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def read_annotation_file(file_path):
    annotations = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('T'):  # Only process entity annotations
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    tag_id, tag_info, text = parts
                    tag_type = tag_info.split()[0]
                    annotations.append({
                        'id': tag_id,
                        'type': tag_type,
                        'text': text
                    })
    return annotations

def analyze_cadec_dataset():
    # Paths
    base_path = 'CADEC.v2/cadec'
    text_path = os.path.join(base_path, 'text')
    ann_path = os.path.join(base_path, 'original')
    
    # Analysis variables
    total_documents = 0
    total_annotations = 0
    annotation_types = Counter()
    drugs = defaultdict(int)
    annotation_texts = defaultdict(int)
    
    # Process each text file
    for text_file in glob.glob(os.path.join(text_path, '*.txt')):
        total_documents += 1
        
        # Get corresponding annotation file
        base_name = os.path.basename(text_file)
        ann_file = os.path.join(ann_path, base_name.replace('.txt', '.ann'))
        
        # Extract drug name from filename
        drug_name = base_name.split('.')[0]
        drugs[drug_name] += 1
        
        # Read annotations
        if os.path.exists(ann_file):
            annotations = read_annotation_file(ann_file)
            total_annotations += len(annotations)
            
            # Count annotation types and texts
            for ann in annotations:
                annotation_types[ann['type']] += 1
                annotation_texts[ann['text'].lower()] += 1
    
    # Print analysis results
    print("=== CADEC Dataset Analysis ===")
    print(f"\nTotal number of documents: {total_documents}")
    print(f"Total number of annotations: {total_annotations}")
    
    print("\nDrug distribution:")
    for drug, count in sorted(drugs.items(), key=lambda x: x[1], reverse=True):
        print(f"{drug}: {count} documents")
    
    print("\nAnnotation types distribution:")
    for ann_type, count in annotation_types.most_common():
        print(f"{ann_type}: {count}")
    
    print("\nTop 20 most common annotated terms:")
    for text, count in sorted(annotation_texts.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"{text}: {count}")

if __name__ == "__main__":
    analyze_cadec_dataset() 