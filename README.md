<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js"></script>
<script type="text/javascript">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
  });
</script>

# MMSQL Dataset

The MMSQL dataset was curated from the CoSQL data, which we refer to as the Multiple type Multi-turn Text-to-SQL test set (MMSQL). For the evaluation, we developed the Accuracy with SQL Matching (AccS) metric.

## Evaluation Metrics

To evaluate our methods, we use two official metrics: Question Match (QM) and Interaction Match (IM). QM measures whether the predicted SQL query matches the ground truth at the single-turn level, while IM assesses whether all predicted SQL queries in a multi-turn interaction achieve QM.

Furthermore, we provide detailed analyses of precision, recall, and F1 scores for user dialogue act prediction across multiple question types. For a holistic assessment, we have devised an integrated metric, AccS, which combines Question Type Recognition and SQL Query Generation. AccS integrates User Dialogue Act Prediction Accuracy (Acc) with Exact Match (QM), offering a comprehensive measure of performance.

### User Dialogue Act Prediction Accuracy (Acc)

Acc is used to evaluate the system's ability to classify questions. It is defined as the proportion of instances where the predicted type matches the expected reference type among all predicted questions. Specifically, for a dataset comprising \( N \) questions, where \( C_i \) denotes the expected classification and \( \hat{C}_i \) represents the predicted classification for the \( i \)-th question, Acc is computed as follows:

$$
\text{Acc} = \frac{1}{N} \sum_{i=1}^{N} \mathrm{I}\left(C_i = \hat{C}_i\right)
$$

where \( \mathrm{I} = 1 \) if \( C_i \) matches \( \hat{C}_i \), and \( \mathrm{I} = 0 \) otherwise.

### Acc with SQL Matching (AccS)

In the context of a database querying dialogue system, it is imperative not only to classify the type of user query accurately but also to furnish the appropriate SQL queries for those answerable questions. To comprehensively evaluate the system's performance, we enhance the Accuracy (Acc) measure by integrating Exact Match (EM) for questions that necessitate SQL query formulation. This integration results in a comprehensive metric, AccS, which assesses both the system’s proficiency in question classification and its precision in SQL query generation within multi-turn dialogues. For a given set of \( N \) questions, where \( S_i \) denotes the ground truth SQL query and \( \hat{S}_i \) represents the predicted SQL query, AccS is computed as follows:

$$
\text{AccS} = \frac{1}{N} \sum_{i=1}^{N} \left\{
\begin{array}{ll}
\mathrm{I}(C_i = \hat{C}_i) \cdot \mathrm{QM}(S_i, \hat{S}_i) & \text{(a)} \\
\mathrm{I}(C_i = \hat{C}_i) & \text{(b)} \\
\end{array}
\right.
$$

$$
\begin{array}{ll}
\text{(a)} & C_i = \text{'Answerable'} \\
\text{(b)} & \text{otherwise}
\end{array}
$$

where \( \mathrm{QM} = 1 \) if \( S_i \) matches \( \hat{S}_i \), and \( \mathrm{QM} = 0 \) otherwise.

AccS can be computed at both the single-turn level and interaction levels. For interaction level AccS (IAccS), if all the predicted SQL queries and question types in an interaction are correct, the IAccS score is 1; otherwise, the score is 0.