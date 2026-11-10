from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

assert comm.Get_size() == 4, "Use exactly four processes."

number = rank + 1

# Calculate an inclusive prefix sum in rank order.
prefix = comm.___(number, op=MPI.SUM)

print(f"Rank {rank}: {prefix}")