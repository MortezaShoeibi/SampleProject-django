from home.models import Social


def socials(request):
    socials = Social.objects.all()
    return {'socials': socials}
