def get_core_data(request):
    user = request.user
    if user.is_authenticated:
        core_data = {
            'user' : user
        }
        return core_data
    else:
        return {}