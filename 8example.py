from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

assert comm.Get_size() == 3, "Use exactly three processes."

if rank == 0:
    number = 5
    comm.send(number, dest=___)

elif rank == 1:
    number = comm.recv(source=___)
    result = number * 2
    comm.send(result, dest=___)

else:
    result = comm.recv(source=___)
    print("Result:", result)