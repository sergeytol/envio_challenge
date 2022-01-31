from datetime import datetime, timezone, timedelta
from uuid import uuid4

from django.core.management.base import BaseCommand

from api.models import Reading


class Command(BaseCommand):
    help = 'Generate test DB data'

    def handle(self, *args, **options):

        device_id = uuid4()
        customer_id = uuid4()

        dt = datetime.now(timezone.utc)
        reading = 0.0

        records = []
        for i in range(10000):
            records.append(Reading(
                time=dt,
                device_id=device_id,
                customer_id=customer_id,
                reading=reading
            ))
            reading += 1
            dt += timedelta(minutes=1)

        Reading.objects.bulk_create(records)

        print("Done.")
        print(f"from: {dt.isoformat()}")
        print(f"device_id: {device_id}")
        print(f"customer_id: {customer_id}")


