from faker import Factory as Fake
from factory.alchemy import SQLAlchemyModelFactory
import factory

from .core import db
from . import models

import logging

# Suppress factory-boy debug data
factory_log = logging.getLogger("factory")
factory_log.setLevel(logging.WARNING)

faker = Fake.create()


class Cat(SQLAlchemyModelFactory):

    class Meta:
        model = models.Cat
        sqlalchemy_session = db.session

    id = factory.LazyAttribute(lambda x: faker.unix_time())
    born_at = factory.LazyAttribute(lambda x: faker.unix_time())

    name = factory.LazyAttribute(lambda x: faker.first_name())
