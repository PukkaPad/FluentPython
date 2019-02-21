# Same function written in retrieving_info_param.py
# The only differences are in the first line of the function
from inspect import signature

def clip(text: str, max_len: 'int > 0' = 80) -> str:
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
	print(clip.__annotations__)
	sig = signature(clip)
	print(sig.return_annotation)
	for param in sig.parameters.values():
		note = repr(param.annotation).ljust(13)
		print(note, ':', param.name, '=', param.default)
