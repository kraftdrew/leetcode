def greet(name: str, end: str):
    print(f"Hello, {name}{end}")

is_exclamation = True

greet("Alice" if is_exclamation  else "John"  , end="! " if is_exclamation else "\n")
