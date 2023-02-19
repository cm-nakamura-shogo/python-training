def sample():
    fuga = "fuga"
    print(f"{fuga}, {id(fuga)}")
    print(locals())
    def print_message(name: str):
        # fuga = "fugafuga"
        print(locals())
        print(f"ワイは{name}である。")
        print(f"{fuga}, {id(fuga)}")
        return

    print_message("nokomoro3")

if __name__ == "__main__":
    print(globals())
    sample()