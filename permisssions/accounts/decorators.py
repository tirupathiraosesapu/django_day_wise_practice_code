from functools import wraps
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def role_required(required_role):
    def decorator(view_function):
        @wraps(view_function)
        @login_required
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name=required_role).exists():
                return view_function(request, *args, **kwargs)
            return redirect("unauthorized")

        return wrapper

    return decorator


def admin_required(view_function):
    return role_required("Admin")(view_function)


def manager_required(view_function):
    return role_required("Manager")(view_function)


def employee_required(view_function):
    return role_required("Employee")(view_function)


def role_and_permission_required(required_role, required_permission):
    def decorator(view_function):
        @wraps(view_function)
        @login_required
        def wrapper(request, *args, **kwargs):
            print("User:", request.user.username)
            print("Groups:", list(request.user.groups.values_list("name", flat=True)))
            print("Role:", request.user.groups.filter(name=required_role).exists())
            print("Permission:", request.user.has_perm(required_permission))
            has_role = request.user.groups.filter(name__in=required_role).exists()
            has_permission = request.user.has_perm(required_permission)
            if has_role and has_permission:
                return view_function(request, *args, **kwargs)
            return redirect("unauthorized")

        return wrapper

    return decorator
