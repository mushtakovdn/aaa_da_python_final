from random import randint
import click
from pizza import Pizza


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    bake(RESTAURANT_MENU[pizza])
    if delivery:
        delivery(RESTAURANT_MENU[pizza])
    else:
        pickup(RESTAURANT_MENU[pizza])


@cli.command()
def menu():
    """Выводит меню"""
    string_menu = ''
    for _, p in RESTAURANT_MENU.items():
        name, recipe = p.dict().popitem()
        recipe = ', '.join(recipe)
        string_menu += f'{name} - {recipe}\n'
    click.echo(string_menu)


def log(template):
    """
    декоратор, который выводит имя функции и время выполнения.
    декоратор принимает шаблон, в который подставляется время.
    """
    def decorator(foo):
        def wrapped(*args):
            duration = foo(args)
            print(template.format(duration))
            return duration
        return wrapped
    return decorator


@log('Приготовили за {} минут.')
def bake(pizza: Pizza):
    """Готовит пиццу"""
    duration = randint(15, 30)
    return duration


@log('Доставили за {} минут.')
def delivery(pizza: Pizza):
    """Доставляет пиццу"""
    duration = randint(5, 60)
    return duration


@log('Забрали за {} минут.')
def pickup(pizza: Pizza):
    """Самовывоз"""
    duration = randint(1, 10)
    return duration


if __name__ == '__main__':
    RESTAURANT_MENU = {
        'Margherita': Pizza('Margherita 🧀', [
            'tomato sauce', 'mozzarella', 'tomatoes'
            ], 'XL'),
        'Pepperoni': Pizza('Pepperoni 🍕', [
            'tomato sauce', 'mozzarella', 'pepperoni'
            ], 'XL'),
        'Hawaiian': Pizza('Hawaiian 🌴🍍', [
            'tomato sauce', 'mozzarella', 'chicken', 'pineapples'
            ], 'L'),
    }
    cli()
