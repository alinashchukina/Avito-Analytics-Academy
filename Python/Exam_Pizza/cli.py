import click
from cooking import bake, deliver, pickup
from pizza import Pizza, Margherita, Pepperoni, Hawaiian


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option(
    "--size", default="L", type=click.Choice(["L", "XL"], case_sensitive=False)
)
@click.argument(
    "pizza",
    nargs=1,
    type=click.Choice(["Margherita", "Pepperoni", "Hawaiian"],
                      case_sensitive=False),
)
def order(pizza: str, delivery: bool, size: str) -> None:
    """Готовит и доставляет пиццу"""
    pizza = pizza.lower().title()
    cls_pizza = eval(pizza)
    obj_pizza = cls_pizza(size)
    if delivery:
        print(bake(obj_pizza), deliver(obj_pizza), sep="\n")
    else:
        print(bake(obj_pizza), pickup(obj_pizza), sep="\n")


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for pizza in ["Margherita", "Pepperoni", "Hawaiian"]:
        cls_pizza = eval(pizza)
        obj_pizza = cls_pizza()
        print(f'- {obj_pizza.name}: {", ".join(obj_pizza.dict().keys())}')


if __name__ == "__main__":
    cli()
