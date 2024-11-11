# Module 7 Notes: Metrics and Model Development

### All code is in knn_analysis.py file

## Metrics

Metrics should be `unbiased`, universal, and concise.

1. A way to obtain similar response
2. A way to measure the performance
3. A way to measure prediction

For our sample analysis we will use `KNN` K-nearest Neighbor
- `K` is an arbitrary pick of nearest Neighbor
- Need a `base case`
- Compare the neighbors
- Sor the results

Dataset for the analysis: 
```bash
icarus.cs.weber.edu:~hvalle/cs4580/data/movies.csv
```

### KNN-Euclidean Distance

The Euclidean distance is the distance between points in `N-dimensional` space.

Formula

$$
d(p, q) = \sqrt{\sum_{i=1}^n (q_i - p_i)^2}
$$
where:
- $p = (p_1, p_2, \dots, p_n)$
- $q = (q_1, q_2, \dots, q_n)$

#### Task:
Find the distance between these points:
- x = (0,0)
- y = (4, 4)

Distance = 5.65685...

```python
# see
def euclidean_similarity_normal()
```

### KNN with Jaccard Similarity Index
Compare members of two individual sets to determine which members are `shared` and which are `distinct`.  The index measure the similarty the two sets.

$$
J(A, B) = \frac{|A \cap B|}{|A \cap B|}
$$

EX: $A = {1, 2, 3, 4}$ and $B = {3, 4, 5, 6}$ = $\frac {2}{6}$ or $0.33$

```python
# see
def jaccard_similarity_normal()
```
### KNN with Weighted Jaccard Similarity Index
The traditional Jaccard works well when doing `one-to-one` comparison between a category.  

One solution is the `weighted` version.
- Build a dictionary for `each genre` of the moives in our preferred list 

```python
# see
def jaccard_similarity_weighted()
```

### KNN with Levenshtein Distance
This is the most common for of edit-based metric which generally quantifies to work required to transform a string from an initital sequence to a target sequence.
- It is used to determine the difference between two sequences (strings)
- It is the distance between two words (minimum number of digits edits)
    - insertions, deletions, or substitution

$$
D(i, j) = 
\begin{cases}
j & \text{if } i = 0 \\
i & \text{if } j = 0 \\
D(i-1, j-1) & \text{if } s[i] = t[j] \\
1 + \min \{D(i-1, j), D(i, j-1), D(i-1, j-1)\} & \text{if } s[i] \neq t[j]
\end{cases}
$$

#### For Example
consider these strings:
- s = 'kitten'
- t = 'sitting'

Find the 'Levenshteain' Distance
1. Substitute `k` with `s` is `kitten` -> `sitten` (1 substantiation)
2. Substitute `e` with `i` is `sitten` -> `sittin` (1 substantiation)
3. Insert `g` at the end of `sittin` -> `sitting` (1 insert)

```python
# see
def knn_levenshtein_title()
```
Need this package
```bash
# VE must be running python 3.11 or less
conda install Levenshtein
```

### KNN Cosine Similarity Distance
It is used to measure the cosine of the angle between two vectors in a multi-dimensional space.  This is commonly use in text analysis to measure similarities between documents.

Get the formula from the post
$$
\text{Cosine Similarity} = \cos(\theta)  
= \frac{A \cdot B}{|A| |B|} 
= \frac{\sum_{i=1}^{n} A_i B_i} { \sqrt{sum_{i=1}^n} A_i^2 \cdot \sqrt{\sum_{i=1}^{n} B_i^2}}
$$

where
- $ A \cdot B$ is the dot product of vectors $A$ and $B$
- $|A|$ and $|B|$ are the magnitude (or Euclidean norms) of vectors $A$ and $B$

### KNN Combining Metrics and Filtering Conditions

Two main concerns with `filtering`:
- Make too complicated (hard SQL queries)
- Too strick (end up with no results)

Combined `metrics` to generate `one` results:
- Weight each metric
    - Should metrics contribute equally? (50% - 50%, 80% - 20%)
- Normalization of the combine metric
    - Make sure they have the same range
    
For our example, we will use:
- `Cosine`: Use 20% of the `plot`
- `Weighted Jaccard`: Use 80% of `genres`

```python
#see 
cosine_and_weighted_jaccard()
```

## Prediction Metrics

A `prediction` is simple a guess about what is going to transpire.  One prediction is `yes` or `no`.

How do we measure `accuracy` of the prediction?

```python
accuracy_metric.py
```
