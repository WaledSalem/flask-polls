from app.models import User
from app import ma


class UserSchema(ma.ModelSchema):
    """User Schema"""
    class Meta(object):
        strict = True
        model = User
