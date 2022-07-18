# Configuration file for ipython.

c.InteractiveShellApp.extensions = ["autoreload"]
c.InteractiveShellApp.exec_lines = [
    "%autoreload 2",
    "from django.contrib.auth import get_user_model",
]
