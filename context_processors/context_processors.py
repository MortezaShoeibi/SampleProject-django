from home.models import Social


def socials(request) -> dict:
    socials = Social.objects.all()
    return {'socials': socials}
