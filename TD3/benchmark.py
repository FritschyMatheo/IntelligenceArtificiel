"""Connect Four TD — benchmarking Minimax, Alpha-Beta and MCTS."""

import matplotlib.pyplot as plt

from algorithms import alphabeta, mcts, minimax
from game import create_board

DEPTHS = [1, 2, 3, 4, 5]
SIMULATIONS = [100, 500, 1000, 2000]
SEED = 42


# q1
def benchmark(board, algorithm, **kwargs):
    result = algorithm(board, **kwargs)
    return {
        "algorithm": algorithm.__name__,
        "config": ", ".join(f"{key}={value}" for key, value in kwargs.items()),
        "move": result["move"],
        "score": result["score"],
        "nodes": result["nodes_explored"],
        "time": result["time"],
    }


# q2/q3/q4
def print_table(results):
    header = f"{'Algorithm':<10} {'Configuration':<32} {'Move':>4} {'Score':>10} {'Nodes':>8} {'Time (s)':>10}"
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r['algorithm']:<10} {r['config']:<32} {r['move']:>4} {r['score']:>10} "
              f"{r['nodes']:>8} {r['time']:>10.4f}")


# q2/q4
def compare_minimax_alphabeta(board, display=True):
    results = []
    for depth in DEPTHS:
        mm = benchmark(board, minimax, depth=depth)
        ab = benchmark(board, alphabeta, depth=depth)
        results += [mm, ab]
        if display:
            same_value = mm["score"] == ab["score"]
            fewer_nodes = ab["nodes"] <= mm["nodes"]
            status = "OK" if same_value and fewer_nodes else "FAIL"
            print(f"depth={depth}: same value={same_value}, "
                  f"alphabeta nodes <= minimax nodes={fewer_nodes} -> {status}")
    if display:
        print()
        print_table(results)
    return results


# q3/q4
def compare_mcts(board, display=True):
    results = [benchmark(board, mcts, num_simulations=n, seed=SEED) for n in SIMULATIONS]
    if display:
        print_table(results)
    return results


# q4
def run_all_experiments(board):
    results = compare_minimax_alphabeta(board, display=False) + compare_mcts(board, display=False)
    print_table(results)
    return results


# q5
def plot_results(results, filename="benchmark.png"):
    fig, (ax_nodes, ax_time) = plt.subplots(1, 2, figsize=(12, 5))

    for name, label in (("minimax", "Minimax"), ("alphabeta", "Alpha-Beta")):
        nodes = [r["nodes"] for r in results if r["algorithm"] == name]
        ax_nodes.plot(DEPTHS, nodes, marker="o", label=label)
    ax_nodes.set_yscale("log")
    ax_nodes.set_xticks(DEPTHS)
    ax_nodes.set_xlabel("Search depth")
    ax_nodes.set_ylabel("Explored nodes (log scale)")
    ax_nodes.set_title("Explored nodes vs. depth")
    ax_nodes.legend()
    ax_nodes.grid(True, alpha=0.3)

    times = [r["time"] for r in results if r["algorithm"] == "mcts"]
    ax_time.plot(SIMULATIONS, times, marker="o", color="tab:green", label="MCTS")
    ax_time.set_xlabel("Number of simulations")
    ax_time.set_ylabel("Execution time (s)")
    ax_time.set_title("MCTS execution time vs. simulations")
    ax_time.legend()
    ax_time.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(filename, dpi=120)
    plt.show()


if __name__ == "__main__":
    board = create_board()

    print("=== Q2: Minimax vs Alpha-Beta ===")
    compare_minimax_alphabeta(board)

    print("\n=== Q3: MCTS ===")
    compare_mcts(board)

    print("\n=== Q4: All experiments ===")
    results = run_all_experiments(board)

    plot_results(results)