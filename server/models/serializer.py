from uuid import UUID
from sqlalchemy_serializer import SerializerMixin


class CustomSerializerMixin(SerializerMixin):
    serialize_types = (
        (UUID, lambda x: str(x)),
    )
