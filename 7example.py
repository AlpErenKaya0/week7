from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

assert comm.Get_size() == 2, "Use exactly two processes."

partner = 1 - rank
number = 10 + rank

# Exchange values with the other process.
received = comm.___(
    number,
    dest=partner,
    source=partner
)

print(f"Rank {rank} received {received}")