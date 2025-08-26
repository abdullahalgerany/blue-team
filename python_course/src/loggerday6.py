import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="my_logging.log"
)

logger = logging.getLogger(_name_)

logger.info("this is my info logging")
logger.warning("this is my warning logging")
logger.error("this is my error logging")
logger.debug("this is the debug logging")
# #############################
# import argparse


# def main():
#     parser = argparse.ArgumentParser(description="Tiny Demo")
#     sub = parser.add_subparsers(dest="cmd", required=True)

#     p_greet = sub.add_parser("greet", help="say hello")
#     p_greet.add_argument("--name", required=True)

#     p_add = sub.add_parser("sum", help="sum all numbers")
#     p_add.add_argument("a", type=int)
#     p_add.add_argument("b", type=int)
#     parser.print_help()

#     args = parser.parse_args()

#     if args.cmd == "greet":
#         print(f"Hello, {args.name}!")
#     elif args.cmd == "add":
#         print(args.a + args.b)


# if _name_ == "_main_":
#     main()
###########################

# import argparse


# def main():
#     parser = argparse.ArgumentParser(description="Tiny Demo")
#     sub = parser.add_subparsers(dest="cmd", required=True)

#     p_greet = sub.add_parser("greet", help="say hello")
#     p_greet.add_argument("--name", required=True)

#     p_sum = sub.add_parser("sum", help="sum all numbers")
#     p_sum.add_argument("numbers", type=int, nargs='+', help="numbers to sum")
    
#     args = parser.parse_args()

#     if args.cmd == "greet":
#         print(f"Hello, {args.name}!")
#     elif args.cmd == "sum":
#         print(sum(args.numbers))


# if __name__ == "__main__":
#     main()
#######################
# import argparse


# def sum_all(numbers):
#     """Sum all numbers in a list"""
#     return sum(numbers)


# def main():
#     parser = argparse.ArgumentParser(description="Tiny Demo")
#     sub = parser.add_subparsers(dest="cmd", required=True)

#     p_greet = sub.add_parser("greet", help="say hello")
#     p_greet.add_argument("--name", required=True)

#     p_sum = sub.add_parser("sum", help="sum all numbers")
#     p_sum.add_argument("numbers", type=int, nargs='+', help="numbers to sum")

#     p_sum_2 = sub.add_parser("sum2", help="sum all numbers (alternative)")
#     p_sum_2.add_argument("numbers", type=int, nargs='+', help="numbers to sum")
#     p_sum_2.set_defaults(function=sum_all)
    
#     args = parser.parse_args()

#     if args.cmd == "greet":
#         print(f"Hello, {args.name}!")
#     elif args.cmd == "sum":
#         result = sum_all(args.numbers)
#         print(result)
#     elif args.cmd == "sum2":
#         result = args.function(args.numbers)
#         print(result)


# if __name__ == "__main__":
#     main()
##############################
import argparse

def print_name(name):
    print(f"Hello, {name}!")

def add_two(nums: list):
    print(sum(nums))
    

def main():
    parser = argparse.ArgumentParser(description="Tiny Demo")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_greet = sub.add_parser("greet", help="say hello")
    p_greet.add_argument("--name", required=True)

    p_add = sub.add_parser("sum", help="sum all numbers")
    p_add.add_argument('--list', nargs='+', type=int, required=True)


    args = parser.parse_args()

    if args.cmd == "greet":
        print_name(args.name)
    elif args.cmd == "sum":
        add_two(args.list)


if _name_ == "_main_":
    main()