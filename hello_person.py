#


def person(name, lang):
    greeting = {
        "English": "Hello",
        "Hindi": "Nameste",
        "Telagu": "Namaskaram",
    }
    msg = f"{greeting[lang]} {name}"
    print(msg)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Hindi", "Telagu"],
        help="The language of the greeting."
    )

    args = parser.parse_args()
    person(args.name, args.lang)
    msg = f"Hello {args.name}!"
    print(msg)
