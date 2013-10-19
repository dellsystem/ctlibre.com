from django.db.models import BooleanField, ImageField


class UniqueBooleanField(BooleanField):
    def pre_save(self, model_instance, add):
        objects = model_instance.__class__.objects

        # If True, then set it to False for all the other objects.
        if getattr(model_instance, self.attname):
            objects.update(**{self.attname: False})
        # If there is no object for which this attribute is true,
        # make it true for this object.
        elif not objects.exclude(id=model_instance.id)\
                        .filter(**{self.attname: True}):
            return True

        return getattr(model_instance, self.attname)
