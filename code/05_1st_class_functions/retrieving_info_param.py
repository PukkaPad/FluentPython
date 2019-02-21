# Retrieving Information About Parameters
from inspect import signature
from positional_to_keywordOnly_param import tag
import inspect

def clip(text, max_len = 80):
    """Return text clipped at the last space before or after max_len """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len) 
        if space_before >= 0:
            end = space_before 
    else:
        space_after = text.rfind(' ', max_len) 
    if space_after >= 0:
        end = space_after
    if end is None: # no spaces were found
        end = len(text) 
    return text[:end].rstrip()


if __name__ == "__main__":
    # Extracting information about the function arguments
    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)

    # Extracting the function signature
    sig = signature(clip)
    print('Signature')
    print(sig)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    # Binding the function signature from the tag function
    sig = inspect.signature(tag)
    my_tag={'name': 'img', 'title': 'Sunset Boulevard',
                  'src': 'sunset.jpg', 'cls': 'framed'}
    bound_args = sig.bind(**my_tag)
    print('Binding')
    print(bound_args)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)