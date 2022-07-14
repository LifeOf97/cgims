from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    """
    Custom permission to only give users with superuser set to true
    the right to proceed
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        elif request.method == "POST":    
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user.is_superuser
            )
        
        else:
            return bool(
                request.user
                and request.user.is_authenticated
            )


class IsOwnerStaff(permissions.BasePermission):
    """
    Custom object level permission to give read and write access to the
    owner of an account instance.
    """
    def has_object_permission(self, request, view, obj):
        # allow safe methods such as GET and HEAD.
        if request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated and request.user.staff == obj:
            return True

        # else check if the requesting user is logged in and is the owner
        # of the object instance.
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsOwnerStudent(permissions.BasePermission):
    """
    Custom object level permission to give read and write access to the
    owner of an account instance.
    """
    def has_object_permission(self, request, view, obj):
        # allow safe methods such as GET and HEAD.
        if request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated and request.user.student == obj:
            return True

        # else check if the requesting user is logged in and is the owner
        # of the object instance.
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)
