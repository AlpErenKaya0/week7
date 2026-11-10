from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

assert comm.Get_size() == 4, "Use exactly four processes."

data = [1, 2, 3, 4] if rank == 0 else None

# Distribute the input.
number = comm.___(data, root=0)

# Each process performs the same operation.
square = number * number

# Collect the separate results.
squares = comm.___(square, root=0)

if rank == 0:
    print(squares)