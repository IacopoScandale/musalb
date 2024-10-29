from argparse import ArgumentParser, Namespace
from .init_comm import init_comm
from .reformat_comm import reformat_comm
from .enumerate_comm import enumerate_comm


def parse_arguments() -> Namespace:
  """
  get musalb command arguments
  """
  parser = ArgumentParser(description="musalb: Music Album Organizer")
  subparsers = parser.add_subparsers(dest="command", required=True)

  # init subcommand
  init_parser = subparsers.add_parser(
    "init", 
    help="Initialize a music album folder"
  )
  init_parser.add_argument(
    "directory", 
    type=str, 
    nargs="?",  # Makes this argument optional
    default=".",  # Default to current directory
    help="Path to the album directory (default: current directory)"
  )

  # reformat subcommand
  reformat_parser = subparsers.add_parser(
    "reformat",
    help=(
      "refreshes music album metadata to all files (useful if new songs"
      "are added to the album)"
    ),
  )
  reformat_parser.add_argument(
    "directory", 
    type=str, 
    nargs="?",  # Makes this argument optional
    default=".",  # Default to current directory
    help="Path to the album directory (default: current directory)"
  )
  reformat_parser.add_argument(
    '-q', '--quiet', 
    action='store_true',
    default=False,
    help="Suppress output verbosity.",
  )

  # enumerate subcommand
  enumerate_parser = subparsers.add_parser(
    "enumerate",
    help="adds track numbers in alphabetical order"
  )
  
  args = parser.parse_args()
  return args


def main() -> None:
  """
  musalb line command
  """
  args: Namespace = parse_arguments()

  # Execute appropriate function based on the command
  if args.command == "init":
    init_comm(args.directory)
  elif args.command == "reformat":
    reformat_comm(args.directory, args.quiet)
  elif args.command == "enumerate":
    enumerate_comm()