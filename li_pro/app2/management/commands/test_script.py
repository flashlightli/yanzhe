from django.core.management.base import BaseCommand, CommandError
#它必须定义一个扩展BaseCommand或其子类之一的类Command


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return {}