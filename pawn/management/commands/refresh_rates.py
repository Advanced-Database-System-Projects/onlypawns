from django.core.management.base import BaseCommand
from pawn import services as S


class Command(BaseCommand):
    help = "Fetch live exchange rates for every currency and save them."

    def handle(self, *args, **opts):
        updated, failed = S.refresh_rates()
        self.stdout.write(f"Updated: {', '.join(updated) or '-'}")
        if failed:
            self.stdout.write(self.style.WARNING(f"Failed: {', '.join(failed)}"))