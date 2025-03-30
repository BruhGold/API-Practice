from rest_framework.permissions import BasePermission

class CanEditQuestion(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        if user.has_perm('api.edit_all_question'):
            return True
        if user.has_perm('api.edit_public_problem') and obj.is_public:
            return True
        if user.has_perm('api.edit_own_question') and user.id in obj.editor_ids:
            return True
            
        return False