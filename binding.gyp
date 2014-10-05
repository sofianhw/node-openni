{
'targets': [
{
'target_name': 'openni',
'sources': [
'src/Callbacks.cc',
'src/Context.cc'
],
'include_dirs': [
'/usr/local/Cellar/openni/1.5.7.10/include/ni/'
],
'conditions': [
['OS=="mac"', {
'link_settings': {
'libraries': [
'libOpenNI.dylib'
],
}
}
],
['OS=="linux"', {
'link_settings': {
'libraries': [
'/usr/lib/libOpenNI.so'
],
}
}
]
]
}
]
}
