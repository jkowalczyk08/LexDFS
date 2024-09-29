# LexDFS
This repository contains the implementation of the general LexBFS algorithm and LexDFS algorithm on chordal graphs. These algorithms are variants of traditional BFS and DFS but have some properties, making them useful in different graph problems. For further details, refer to the [Implementation of LexDFS on Chordal Graphs](Implementation%20of%20LexDFS%20on%20Chordal%20Graphs.pdf) paper.

Algorithms in this repository are based on pseudocode and descriptions from many articles but mostly [Linear Time LexDFS on Chordal Graphs](https://arxiv.org/abs/2005.03523) and [Lex-BFS and partition refinement, with applications to transitive orientation, interval graph recognition and consecutive ones testing](https://www.sciencedirect.com/science/article/pii/S0304397597002417?via%3Dihub). Full list of references is included in the paper.
## Algorithms
In the context of graph search algorithms, a tie is a situation where multiple vertices can be selected as the next vertex.
Many graph algorithms do not specify how to handle ties. For example, in BFS, the order in which unvisited neighbors are added to the queue is usually the order of vertices in the graph adjacency list. To specify this, 'plus' variants of graph search algorithms were introduced. These variants take an additional parameter with a tiebreaking order of all vertices, and if there is a tie, the algorithm chooses the largest vertex according to the tiebreaking order.

- lex_bfs_plus.py - performs the LexBFS+ algorithm in linear time using a technique called partition refinement.
- lex_dfs_plus_on_chordal.py - performs the LexDFS+ algorithm on chordal graph in linear time. There is currently no general case linear time algorithm. However, there are some graph classes with linear algorithms.
- partition refinement - Although it is used just as a building block in LexBFS+ and LexDFS+, there are other use cases of this algorithm that are unrelated to this paper, so it is worth listing. It is implemented as a method of Partition class.
- simple-*.py - these algorithms are not optimal but are based directly on the definition of LexBFS and LexDFS. They are used for testing.
## Installation
1. Ensure you have Python 3.10 or a compatible version installed. You can check the Python version by running:
   ```bash
   python --version
   ```

2. Clone or download the repository

3. Create and activate virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Testing

To run unit tests, run the following command from the root directory:
```bash
python -m unittest
