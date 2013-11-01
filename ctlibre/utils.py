from django.shortcuts import get_object_or_404, redirect


def force_slug_language(translation_model):
    """This is a decorator for views that ensures that the user is at the
    correct URL for the specified language (based on the slug)."""
    def wrap(view):
        def new_view(request, slug):
            if slug is not None:
                translation = get_object_or_404(translation_model, slug=slug)

                # If the slug is referring to a language other than the one
                # specified by the user, redirect to that translation's URL (but
                # don't change the user's selected language).
                if translation.language_code != request.LANGUAGE_CODE:
                    return redirect(translation.parent)
                else:
                    return view(request, translation.parent)
            else:
                return view(request, None)
        return new_view
    return wrap
