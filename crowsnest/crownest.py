import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Crownest Project 01")
    parser.add_argument('-i',
                        '--item',
                        metavar="item",
                        default=None,
                        help="What do you see sailor?")

    return parser.parse_args()


def main():
    args = get_args()
    article = "a"

    if args.item[0].lower() in "aeiou":
        article = "an"
        print(f"Ahoy Captain! {article} {args.item} off the larboard bow.")

    else:
        print(f"Ahoy Captain! {article} {args.item} off the larboard bow.")


if __name__ == "__main__":
    main()
