from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from functools import wraps

def owner_required(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Owner').exists():
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return _wrapped_view
