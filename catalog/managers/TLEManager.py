from django.db import models

import datetime
import pytz

class TLEManager(models.Manager):

    def findByCatalogEntryAndTime(self, catalogEntry, time = None):
        """
            Return a tle matching the given time and catalog entry
        """
        if time is None:
            time = datetime.utcnow()

        time = time.replace(tzinfo=pytz.UTC)

        tle = self.filter(
                models.Q(
                    date_added__lte=time
                ),
                satellite_number=catalogEntry
            ).order_by(
                '-date_added',
            )[0]

        return tle