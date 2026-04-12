#!/usr/bin/env python3
"""Module demonstrating mixins with Dragon"""

class SwimMixin:
    """Mixin that adds swimming ability"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon has multiple abilities via mixins"""

    def roar(self):
        print("The dragon roars!")
