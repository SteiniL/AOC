from collections import defaultdict, deque
from pathlib import Path
from typing import List, Tuple, Dict, Set

def read_data(path: str = "input.txt"):
    text = Path(path).read_text().strip().splitlines()

    # Split am ersten Leerstring in Regeln / Updates
    blank = text.index('') if '' in text else len(text)
    rule_lines = text[:blank]
    update_lines = text[blank+1:]

    # Regeln
    edges: Set[Tuple[int, int]] = set()
    succ: Dict[int, Set[int]] = defaultdict(set)
    pred: Dict[int, Set[int]] = defaultdict(set)
    for line in rule_lines:
        a, b = map(int, line.split('|'))
        if (a, b) not in edges:
            edges.add((a, b))
            succ[a].add(b)
            pred[b].add(a)

    # Updates
    updates: List[List[int]] = [list(map(int, u.split(','))) for u in update_lines if u]

    return succ, pred, updates

def is_valid_update(update: List[int], succ: Dict[int, Set[int]]) -> bool:
    """Prüft ein Update effizient: für jede Kante u->v, die im Update vorkommt, muss pos[u] < pos[v] gelten."""
    pos = {v: i for i, v in enumerate(update)}
    # Lokale Bindungen für Speed
    _succ = succ
    _pos = pos
    for u in update:
        for v in _succ.get(u, ()):
            if v in _pos and _pos[u] >= _pos[v]:
                return False
    return True

def topo_sort_subset(nodes: List[int], succ: Dict[int, Set[int]], pred: Dict[int, Set[int]]) -> List[int]:
    """Topologischer Sort nur über die in 'nodes' enthaltenen Knoten (Teilgraph)."""
    node_set = set(nodes)
    # Eingangsgrade innerhalb des Teilgraphen
    indeg = {u: sum(1 for p in pred.get(u, ()) if p in node_set) for u in node_set}
    q = deque([u for u, d in indeg.items() if d == 0])
    order: List[int] = []

    _succ = succ
    while q:
        u = q.popleft()
        order.append(u)
        for v in _succ.get(u, ()):
            if v in indeg:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

    if len(order) != len(node_set):
        # Sollte laut Aufgabenstellung nicht passieren (keine Zyklen). Defensive Guard.
        raise ValueError("Cycle detected or missing nodes in topological sort.")
    return order

def middle_value(update: List[int]) -> int:
    return update[len(update) // 2]

def solve(path: str = "input.txt"):
    succ, pred, updates = read_data(path)

    correct: List[List[int]] = []
    incorrect: List[List[int]] = []
    for u in updates:
        (correct if is_valid_update(u, succ) else incorrect).append(u)

    part_one = sum(middle_value(u) for u in correct)

    corrected: List[List[int]] = []
    for u in incorrect:
        fixed = topo_sort_subset(u, succ, pred)
        corrected.append(fixed)
    part_two = sum(middle_value(u) for u in corrected)

    return part_one, part_two

def main():
    p1, p2 = solve("input.txt")
    print("Part One:", p1)
    print("Part Two:", p2)

if __name__ == "__main__":
    main()
