def get_core_data(request):
    user = request.user
    if user.is_authenticated:
        # Fetch user's core data
        core_data = {
            'user' : user
        }
        return core_data
    