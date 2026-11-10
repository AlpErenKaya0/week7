from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

assert comm.Get_size() == 4, "Use exactly four processes."

local_value = rank + 1

# Return the global sum to every process.
total = comm.___(local_value, op=MPI.SUM)

print(f"Rank {rank}: {total}")