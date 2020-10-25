print("initialized: ", __name__)  # Package.Module


def moduleMethod():
    print("moduleMethod()")


if __name__ == "__main__":
    # this code will only be executed when script started directly as main!
    # -> python Module.py
    print("Module started directly")
