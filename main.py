from src.argument_parser import parse_args  # pragma: no cover
import src.display as start  # pragma: no cover

args = parse_args()  # pragma: no cover
lumos = start.Display  # pragma: no cover
lumos().display(args)  # pragma: no cover
