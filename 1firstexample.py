from mpi4py import MPI
from heapq import merge

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

assert comm.Get_size() == 2, "Use exactly two processes."

# Give each process a different list.
if rank == 0:
    local_data = [8, 2, 6]
else:
    local_data = [7, 1, 3]

# Sort each local list independently.
local_data.sort()

# Collect both sorted lists at rank 0.
parts = comm.___(local_data, root=0)

if rank == 0:
    # Merge the two already-sorted lists.
    result = list(merge(parts[0], parts[1]))
    print(result)