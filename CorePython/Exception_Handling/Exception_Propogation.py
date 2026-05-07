def son():
    raise RuntimeError("I do a mistake , Sorry")    # the son function throws an exception

def mom():
    son()  # the mom function cant handle it so it propogates the error to dad function


def dad():
    try:
        mom()   # it checks an error in mom function
    except RuntimeError as e:
        print(e)                  # RuntimeError ki jagah koi bhi error ka name likh skte hai

dad()  # Calling dad function