# LLM Response Similarity — Evaluation Demo

A small Python exercise that compares the unique words in sample model outputs with reference answers and reports a simple overlap score.

## What it demonstrates
- Loading sample evaluation cases from JSON
- Tokenising text with basic whitespace splitting
- Calculating a Jaccard-style word-set overlap score
- Reporting an average score and script execution time

## Run
```bash
python eval_metrics.py
```

## Important scope and limitations
Despite the repository's original name, this implementation does **not** perform semantic evaluation. It uses simple word-set overlap, which does not understand synonyms, meaning, factual correctness, or context. The execution-time figure is a basic local script timing, not a production latency benchmark.

## Files
- `eval_metrics.py` — word-overlap calculation and reporting
- `test_cases.json` — illustrative test cases

## Author
Hiba Almamoori
