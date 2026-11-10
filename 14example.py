def increment_A():
    while True:
        old = atomic_load(counter)

        # Update only if nobody changed the counter.
        if CAS(counter, expected=old, new=old + 1):
            return

        # Another thread changed the counter.
        # Retry using a new value.
    
def increment_B():
    # Complete the increment with one bounded atomic operation.
    atomic_fetch_add(counter, 1)