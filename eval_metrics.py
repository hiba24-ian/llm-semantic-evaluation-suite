import json
import time

def load_test_cases(file_path):
    """Load evaluation test cases from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data.get("evaluation_suite", [])

def evaluate_response_length(output, ground_truth):
    """Simulate semantic evaluation by comparing token/word overlap ratios."""
    output_words = set(output.lower().split())
    gt_words = set(ground_truth.lower().split())
    
    # Calculate simple token intersection over union (Jaccard-like similarity)
    intersection = output_words.intersection(gt_words)
    union = output_words.union(gt_words)
    
    score = len(intersection) / len(union) if union else 0.0
    return round(score, 2)

if __name__ == "__main__":
    print("Initializing LLM Semantic Evaluation Suite...\n")
    start_time = time.time()
    
    test_cases = load_test_cases("test_cases.json")
    print("Loaded " + str(len(test_cases)) + " benchmark test cases.\n")
    
    total_score = 0.0
    
    for case in test_cases:
        case_id = case["id"]
        prompt = case["prompt"]
        output = case["model_output"]
        ground_truth = case["ground_truth"]
        category = case["category"]
        
        # Evaluate similarity score
        score = evaluate_response_length(output, ground_truth)
        total_score += score
        
        print("Test ID: " + str(case_id) + " [" + category + "]")
        print("Prompt: " + prompt)
        print("Similarity Score: " + str(score))
        print("-" * 50)
    
    avg_score = total_score / len(test_cases) if test_cases else 0.0
    execution_time = round(time.time() - start_time, 4)
    
    print("\n--- Evaluation Summary ---")
    print("Average Semantic Score: " + str(round(avg_score, 2)))
    print("Total Execution Latency: " + str(execution_time) + " seconds")
    print("Status: Evaluation Completed Successfully!")
