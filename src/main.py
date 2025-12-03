#!/usr/bin/env python3
"""Pequeña utilidad para pruebas CI/CD.

Contiene una función `add` y un pequeño CLI para invocarla.
"""
import argparse
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
	"""Return the sum of a and b.

	Works with ints and floats. Kept intentionally tiny for CI smoke tests.
	"""
	return a + b


def main(argv=None) -> int:
	parser = argparse.ArgumentParser(description="Utilities for CI/CD test")
	sub = parser.add_subparsers(dest="command")
	add_p = sub.add_parser("add", help="Add two numbers")
	add_p.add_argument("a", type=float)
	add_p.add_argument("b", type=float)

	args = parser.parse_args(argv)

	if args.command == "add":
		result = add(args.a, args.b)
		# Print as integer when result is an integral float
		if isinstance(result, float) and result.is_integer():
			print(int(result))
		else:
			print(result)
		return 0

	parser.print_help()
	return 1


if __name__ == "__main__":
	raise SystemExit(main())
