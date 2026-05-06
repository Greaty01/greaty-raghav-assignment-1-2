import numpy as np

def bankers_algorithm():
    # Task 1: System Input and Data Representation
    print("--- Task 1: Input System Data ---")
    n_processes = int(input("Enter number of processes: "))
    n_resources = int(input("Enter number of resources: "))

    print("\nEnter Allocation Matrix (row by row):")
    allocation = np.array([list(map(int, input().split())) for _ in range(n_processes)])

    print("\nEnter Max Matrix (row by row):")
    maximum = np.array([list(map(int, input().split())) for _ in range(n_processes)])

    print("\nEnter Available Resources:")
    available = np.array(list(map(int, input().split())))

    # Task 2: Need Matrix Calculation
    # Need = Max - Allocation
    need = maximum - allocation
    print("\n--- Task 2: Calculated Need Matrix ---")
    print(need)

    # Task 3 & 4: Safety Algorithm & Safe Sequence
    finish = [False] * n_processes
    safe_sequence = []
    work = np.copy(available)

    while len(safe_sequence) < n_processes:
        allocated_in_round = False
        
        for i in range(n_processes):
            if not finish[i]:
                # Check if Need <= Work
                if all(need[i] <= work):
                    # Process can finish
                    work += allocation[i]
                    finish[i] = True
                    safe_sequence.append(f"P{i}")
                    allocated_in_round = True
                    print(f"Process {i} finished. Updated Work: {work}")
        
        if not allocated_in_round:
            break

    # Task 5: Result Analysis
    print("\n--- Task 5: Result Analysis ---")
    if len(safe_sequence) == n_processes:
        print("SYSTEM STATE: SAFE")
        print("SAFE SEQUENCE:", " -> ".join(safe_sequence))
    else:
        print("SYSTEM STATE: UNSAFE (Deadlock detected/possible)")

if __name__ == "__main__":
    bankers_algorithm()
