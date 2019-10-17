#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def root(*x):
    return os.path.join(BASE_DIR, *x)


if not settings.configured:
    settings.configure(
        DEBUG=True,
        DATABASES={
            "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
        },
        INSTALLED_APPS=("django.contrib.contenttypes", "apiblueprint_view"),
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "APP_DIRS": True,
                "DIRS": [root("templates")],
                "OPTIONS": {"debug": True, "context_processors": []},
            }
        ],
    )

django.setup()
TestRunner = get_runner(settings)
test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
failures = test_runner.run_tests(["apiblueprint_view"])
sys.exit(failures)
