import pytest

from app.ingestion.chunker import chunker


def test_chunker_0_chunks(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("", encoding="utf-8")

    chunks = chunker(test_file)

    assert len(chunks) == 0  

def test_chunker_150_words(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ligula urna, consectetur suscipit pellentesque eu, iaculis tincidunt tortor. Vestibulum ut congue nunc. Fusce vel blandit ligula. Nulla consectetur nec metus nec molestie. Integer vitae viverra tellus, a tincidunt ipsum. Nam non arcu at odio maximus rutrum at vitae ipsum. Aliquam nisl nulla, vehicula quis pharetra vel, viverra vel sem. Donec ante leo, hendrerit id erat sit amet, blandit maximus nisi.
Pellentesque rutrum dui et magna dictum sodales. Vestibulum facilisis congue lorem vitae maximus. In dui libero, imperdiet vel arcu id, pharetra commodo ligula. Aenean fringilla porta orci vel tempus. Aenean pretium, quam hendrerit dignissim tempor, lorem orci faucibus tortor, at varius velit lorem vel mi. Etiam luctus leo at cursus tincidunt. Ut massa tellus, mattis id felis sed, pulvinar pellentesque metus. Morbi finibus est velit, tincidunt gravida est ultricies in. Phasellus vitae erat sed nulla molestie elementum. Sed id rutrum. ''', encoding="utf-8")

    chunks = chunker(test_file)

    assert len(chunks) == 1
    assert chunks[0]["text"]=='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ligula urna, consectetur suscipit pellentesque eu, iaculis tincidunt tortor. Vestibulum ut congue nunc. Fusce vel blandit ligula. Nulla consectetur nec metus nec molestie. Integer vitae viverra tellus, a tincidunt ipsum. Nam non arcu at odio maximus rutrum at vitae ipsum. Aliquam nisl nulla, vehicula quis pharetra vel, viverra vel sem. Donec ante leo, hendrerit id erat sit amet, blandit maximus nisi.
Pellentesque rutrum dui et magna dictum sodales. Vestibulum facilisis congue lorem vitae maximus. In dui libero, imperdiet vel arcu id, pharetra commodo ligula. Aenean fringilla porta orci vel tempus. Aenean pretium, quam hendrerit dignissim tempor, lorem orci faucibus tortor, at varius velit lorem vel mi. Etiam luctus leo at cursus tincidunt. Ut massa tellus, mattis id felis sed, pulvinar pellentesque metus. Morbi finibus est velit, tincidunt gravida est ultricies in. Phasellus vitae erat sed nulla molestie elementum. Sed id rutrum. '''

def test_chunker_201_words(tmp_path):
    test_file = tmp_path / "text.txt"    
    test_file.write_text('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. In scelerisque sem et fringilla rutrum. Donec hendrerit, velit ac maximus ornare, velit quam tincidunt justo, sed eleifend felis orci at risus. Praesent molestie felis quis libero interdum rutrum. Praesent luctus tincidunt mollis. Sed vel neque eget magna gravida mollis. Integer at dui dui. Interdum et malesuada fames ac ante ipsum primis in faucibus.

Morbi consectetur justo tincidunt purus lacinia, quis maximus risus eleifend. Fusce convallis, ex sed convallis tristique, magna erat tempor diam, ac mattis velit augue nec eros. Quisque auctor ultrices velit non gravida. Etiam in nisi vitae nisi varius viverra blandit vitae felis. Integer in bibendum justo. Sed varius nulla ac elementum fringilla. Vivamus posuere malesuada vulputate. Nam vestibulum et orci sed venenatis. Cras suscipit urna eget eros ultricies, ut fermentum neque pellentesque. Aenean feugiat arcu eget nisl auctor fringilla quis in ante. Pellentesque congue eros vitae iaculis rhoncus. Praesent vel feugiat risus. Praesent a urna quis nunc placerat viverra tempor eget nunc.

Vivamus sit amet euismod nibh. Suspendisse felis ipsum, condimentum consectetur vulputate nec, posuere vel leo. Pellentesque facilisis, ex vehicula placerat faucibus, quam ante efficitur dui, nec volutpat eros mauris finibus orci. Aenean luctus nulla nibh, quis ornare.     ''', encoding="utf-8")

    chunks = chunker(test_file)
    assert len(chunks) == 2

    
def test_chunker_proper_split(tmp_path):
    
    test_file = tmp_path / "text.txt"    
    test_file.write_text('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. In scelerisque sem et fringilla rutrum. Donec hendrerit, velit ac maximus ornare, velit quam tincidunt justo, sed eleifend felis orci at risus. Praesent molestie felis quis libero interdum rutrum. Praesent luctus tincidunt mollis. Sed vel neque eget magna gravida mollis. Integer at dui dui. Interdum et malesuada fames ac ante ipsum primis in faucibus.

Morbi consectetur justo tincidunt purus lacinia, quis maximus risus eleifend. Fusce convallis, ex sed convallis tristique, magna erat tempor diam, ac mattis velit augue nec eros. Quisque auctor ultrices velit non gravida. Etiam in nisi vitae nisi varius viverra blandit vitae felis. Integer in bibendum justo. Sed varius nulla ac elementum fringilla. Vivamus posuere malesuada vulputate. Nam vestibulum et orci sed venenatis. Cras suscipit urna eget eros ultricies, ut fermentum neque pellentesque. Aenean feugiat arcu eget nisl auctor fringilla quis in ante. Pellentesque congue eros vitae iaculis rhoncus. Praesent vel feugiat risus. Praesent a urna quis nunc placerat viverra tempor eget nunc.

Vivamus sit amet euismod nibh. Suspendisse felis ipsum, condimentum consectetur vulputate nec, posuere vel leo. Pellentesque facilisis, ex vehicula placerat faucibus, quam ante efficitur dui, nec volutpat eros mauris finibus orci. Aenean luctus nulla nibh, quis ornare.     ''', encoding="utf-8")

    chunks = chunker(test_file)
    assert chunks[0]["text"]=='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. In scelerisque sem et fringilla rutrum. Donec hendrerit, velit ac maximus ornare, velit quam tincidunt justo, sed eleifend felis orci at risus. Praesent molestie felis quis libero interdum rutrum. Praesent luctus tincidunt mollis. Sed vel neque eget magna gravida mollis. Integer at dui dui. Interdum et malesuada fames ac ante ipsum primis in faucibus.

Morbi consectetur justo tincidunt purus lacinia, quis maximus risus eleifend. Fusce convallis, ex sed convallis tristique, magna erat tempor diam, ac mattis velit augue nec eros. Quisque auctor ultrices velit non gravida. Etiam in nisi vitae nisi varius viverra blandit vitae felis. Integer in bibendum justo. Sed varius nulla ac elementum fringilla. Vivamus posuere malesuada vulputate. Nam vestibulum et orci sed venenatis. Cras suscipit urna eget eros ultricies, ut fermentum neque pellentesque. Aenean feugiat arcu eget nisl auctor fringilla quis in ante. Pellentesque congue eros vitae iaculis rhoncus. Praesent vel feugiat risus. Praesent a urna quis nunc placerat viverra tempor eget nunc.

Vivamus sit amet euismod nibh. Suspendisse felis ipsum, condimentum consectetur vulputate nec, posuere vel leo. Pellentesque facilisis, ex vehicula placerat faucibus, quam ante efficitur dui, nec volutpat eros mauris finibus orci. Aenean luctus nulla nibh, quis'''

    assert chunks[1]["text"]=='''Praesent vel feugiat risus. Praesent a urna quis nunc placerat viverra tempor eget nunc.

Vivamus sit amet euismod nibh. Suspendisse felis ipsum, condimentum consectetur vulputate nec, posuere vel leo. Pellentesque facilisis, ex vehicula placerat faucibus, quam ante efficitur dui, nec volutpat eros mauris finibus orci. Aenean luctus nulla nibh, quis ornare.     '''

