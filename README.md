 ![MMSQL](https://github.com/mcxiaoxiao/MMSQL/blob/paper/mmsql.png)
# MMSQL
## Abstract
This repository contains the scripts and code used for the experiments in the "Evaluating and Enhancing Large Language Models for Complex Multi-Turn Text-to-SQL Conversations" paper. The repository is structured to ensure the reproducibility of the experiments and includes scripts, notebooks, test suits, and data outputs. Some of the data used by the MMSQL dataset is generated by [🐦QDA-SQL](https://github.com/mcxiaoxiao/QDA-SQL).

## File Architecture
- `\datasets`: MMSQL test set `MMSQL_test.json`, MMSQL train set `MMSQL_train.json`, CoSQL dataset `cosql_dataset` (Our dataset based on its sqlite databases You can download it [here](https://drive.google.com/uc?export=download&id=1Y3ydpFiQQ3FC0bzdfy3groV95O_f1nXF) and unzip).
- `outputs/`: Directory containing various experimental output JSON files.
- `llm_generation.py`: The script generates responses using the LLM.
- `RQS_eval.py`: Script for evaluating responses using GPT-4o-mini to score RQS and label the response types.
- `ACCS_eval.py`: Script for calculating several metrics including TDEX, EM, EX, ERROR...
- `correlation_analysis.ipynb`: Jupyter notebook for calculating the Spearman and Pearson correlations between human ratings and GPT-4o ratings.
- `analysis_outputs.ipynb`: Jupyter notebook for producing figures in a thesis.


## Getting Started

To reproduce the experiments or test your models, follow the steps below:

### 1. Generate Responses with LLM

Use the `llm_generation.py` script to generate responses for the MMSQL test set. You can choose between huggingface or api based LLMs.

```bash
python python llm_generation.py outputs/Llama-3-70B.json
```

### 2. Evaluate Responses with GPT-4o-mini

Use the `rqs_evaluation.py` script to evaluate the generated responses. The RQS scores will be added to the output JSON file in the `outputs` directory.

```bash
python RQS_eval.py outputs/Llama-3-70B.json outputs/gpt4_scored_Llama-3-70B.json
```

### 3. Calculate Metrics

Use the `accs_eval.py` script to calculate several metrics from the output JSON files, including base metric (e.g. ACCS, IACCS, EM, QM...) and analytical results.

```bash
python python ACCS_eval.py outputs/one-shot/gpt4_scored_Llama-3-70B.json 
```

### Citations

### Output Example

```bash
_____________________________________
A. Overall Result Analysis
_____________________________________
| Metric | Count | Total | Percentage |
|--------|-------|-------|------------|
| TDEX   | 549   | 806   | 68.1%      |
| EM     | 211   | 553   | 43.3%      |
| EX     | 352   | 553   | 72.3%      |
| ACCS   | 408   | 806   | 50.6%      |
| IACCS  | 4     | 149   | 2.7%       |
| ERROR  | 9     | 553   | 1.8%       |
| IM     | 11    | 149   | 7.4%       |
-------------------------------------
B. Category Analysis
__________________________________________________
| Category       | Precision | Recall | F1 Score |
|----------------|-----------|--------|----------|
| Answerable     | 92.1%    | 88.1%  | 90.0%  |
| Unanswerable   | 24.2%    | 76.2%  | 36.8%  |
| Ambiguous      | 54.8%    | 40.5%  | 46.6%  |
| Improper       | 98.7%    | 99.3%  | 99.0%  |
__________________________________________________
| Average F1     |           |        | 68.1%  |
__________________________________________________
C. Turn-wise QM Statistics
_________________________________________
| Turn  | QM Count | Total | Percentage |
|-------|----------|-------|------------|
| 1     | 34       | 122   | 27.9%      |
| 2     | 55       | 124   | 44.4%      |
| 3     | 42       | 118   | 35.6%      |
| 4     | 43       | 89    | 48.3%      |
| 5     | 14       | 41    | 34.1%      |
| 6     | 12       | 28    | 42.9%      |
| 7     | 6        | 19    | 31.6%      |
| 8     | 3        | 6     | 50.0%      |
| 9     | 0        | 3     | 0.0%      |
| 10    | 1        | 1     | 100.0%      |
| 11    | 1        | 1     | 100.0%      |
| 12    | 0        | 1     | 0.0%      |
| >4    | 37       | 100   | 37.0%      |
_________________________________________
D. Answerable QA vs. Ambiguous QA turns QM Analysis
___________________________________________________
| Metric             | Count | Total | Percentage |
|--------------------|-------|-------|------------|
| Ans.Q+ans          | 211   | 553   | 43.3%      |
| Amb.Q+ans          | 7     | 38    | 18.4%      |
| Amb.Q+clarify+ans  | 70    | 149   | 47.0%      |
___________________________________________________
E. RQS Averages by Category
________________________________
| Category       | Average RQS |
|----------------|-------------|
| Unanswerable   | 7.25        |
| Ambiguous      | 3.25        |
| Improper       | 8.50        |
________________________________
| Overall Average | 6.33        |
________________________________
F. Rewritten QA Analysis
_____________________________________________
| Metric       | Count | Total | Percentage |
|--------------|-------|-------|------------|
| Ans.Q+Amb    | 13    | 27    | 48.1%      |
| Amb.Q+Amb    | 3     | 34    | 8.8%      |
_____________________________________________
 __  __ __  __ ____   ___  _     
|  \/  |  \/  / ___| / _ \| |    
| |\/| | |\/| \___ \| | | | |    
| |  | | |  | |___) | |_| | |___ 
|_|  |_|_|  |_|____/ \__\_\_____|
                                 

We appreciate your interest! For more details and if you have any questions, please refer to: https://github.com/mcxiaoxiao/MMSQL

```
