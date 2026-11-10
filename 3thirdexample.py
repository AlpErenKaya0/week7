from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

assert comm.Get_size() == 4, "Use exactly four processes."

values = [4, 9, 2, 7]
local_value = values[rank]

maximum = comm.___(local_value, op=MPI.___, root=0)

if rank == 0:
    print("Maximum:", maximum)