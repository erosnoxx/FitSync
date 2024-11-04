from factory.alchemy import SQLAlchemyModelFactory
from factory import LazyAttribute
from faker import Faker
from src.application.extensions.Settings import db
from src.domain.entities.auth import *


fake = Faker(['pt_BR'])