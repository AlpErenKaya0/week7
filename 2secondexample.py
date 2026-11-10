from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

assert comm.Get_size() == 4, "Use exactly four processes."

# Only rank 0 prepares the source list.
data = [10, 20, 30, 40] if rank == 0 else None

# Give one number to each process.
local_number = comm.___(data, root=0)

# Combine the numbers into one sum at rank 0.
total = comm.___(local_number, op=MPI.___, root=0)

if rank == 0:
    print("Total:", total)