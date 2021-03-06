{
  'targets': [
    {
      'target_name': 'keytar',
      'include_dirs': [ '<!(node -e "require(\'nan\')")' ],
      'sources': [
        'src/main.cc',
        'src/keytar.h',
      ],
      'conditions': [
        ['OS=="mac"', {
          'sources': [
            'src/keytar_mac.cc',
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
            ],
          },
        }],
        ['OS=="win"', {
          'sources': [
            'src/keytar_win.cc',
          ],
          'msvs_disabled_warnings': [
            4267,  # conversion from 'size_t' to 'int', possible loss of data
            4530,  # C++ exception handler used, but unwind semantics are not enabled
            4506,  # no definition for inline function
          ],
        }],
        ['OS not in ["mac", "win"]', {
          'sources': [
            'src/keytar_posix.cc',
          ],
          'cflags': [
            '<!(pkg-config --cflags gnome-keyring-1)',
            '-Wno-missing-field-initializers',
          ],
          'link_settings': {
            'ldflags': [
              '<!(pkg-config --libs-only-L --libs-only-other gnome-keyring-1)',
            ],
            'libraries': [
              '<!(pkg-config --libs-only-l gnome-keyring-1)',
            ],
          },
        }],
      ],
    }
  ]
}
