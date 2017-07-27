import copy

DEFAULT_DATA = {
    'administrator': {
        'name': 'Admin',
        'pw': 'secret',
        'is_author': False,
        'is_admin': True,
        'private_snippet': 'My password is secret. Get it?',
        'web_site': 'https://www.google.com/contact/',
    },

}


def DefaultData():
  """Provides default data for Gruyere."""
  return copy.deepcopy(DEFAULT_DATA)
