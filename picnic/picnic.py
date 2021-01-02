import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Crownest Project 02",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar="str",
                        nargs="+",
                        help="Item(s) to bring")

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help="Check for sorting item(s)")

    return parser.parse_args()


def main():
    args = get_args()
    items = list(args.item)
    num_of_items = len(items)

    template = "You are bringing {}."
    if args.sorted:
        items.sort()

    if num_of_items == 1:
        print(template.format(items[0]))

    elif num_of_items == 2:
        print(template.format(' and '.join(items)))

    else:
        items[-1] = "and " + items[-1]
        print(template.format(', '.join(items)))


if __name__ == "__main__":
    main()
