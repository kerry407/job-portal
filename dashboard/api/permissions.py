from rest_framework import permissions 


class IsEmployer(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return request.user == request.user.is_employer


class JobPosterOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True 
        else:
            return obj.poster == request.user
        
        
class JobApplicantOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
    
        return obj.applicant == request.user or \
            obj.job_post.poster == request.user
               

