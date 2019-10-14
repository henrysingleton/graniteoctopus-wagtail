from django import template

register = template.Library()


@register.filter(name='blocks_by_type')
def filter_blocks_by_type(value, block_type):
    """ Filter StreamField content by the passed block type
    Pass the block type as a string. The block type isn't checked to see if its valid.
    An invalid block type will result in an empty result set.
    TODO: Fix known bug where multiple calls to this filter with different block types on the same result set causes
    the result set to be permanently mutated.
    """
    value.stream_data = [b for b in value.stream_data if b['type'] == block_type]

    return value

