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