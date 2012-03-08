# Copyright (c) 2011, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

{
  'variables': {
    # These variables are used in the creation of the .vcproj file on 
    # Windows.
    'cygwin_dir': 'third_party/cygwin',
  },
  'targets': [
    {
      'target_name': 'compiler',
      'type': 'none',
      'dependencies': [
        'compiler/dart-compiler.gyp:dartc',
      ],
      'actions': []
    },
    {
      'target_name': 'runtime',
      'type': 'none',
      'dependencies': [
        'runtime/dart-runtime.gyp:dart',
        'runtime/dart-runtime.gyp:run_vm_tests',
        'runtime/dart-runtime.gyp:process_test',
      ],
    },
    {
      'target_name': 'frog',
      'type': 'none',
      'dependencies': [
        'frog/dart-frog.gyp:frog',
      ],
    },
    {
      'target_name': 'frogsh',
      'type': 'none',
      'dependencies': [
        'frog/dart-frog.gyp:frogsh',
      ],
    },
    {
      'target_name': 'create_sdk',
      'type': 'none',
      'conditions': [
        ['OS=="win"', {
          'msvs_cygwin_dirs': ['<(cygwin_dir)'],
        }],
      ],
      'dependencies': [
        'runtime',
      ],
      'actions': [
        {
          'action_name': 'create_sdk_py',
          'inputs': [
            '<!@(["python", "frog/scripts/list_frog_files.py", "frog"])',
            # TODO(dgrove) - change these to dependencies and add dom
            # dependences once issues 754 and 755 are fixed
            'client/html/html_frog.dart',
            'client/html/html_dartium.dart',
            'client/dom/dom.dart',
            'client/dom/generated',
            'client/dom/src',
            'frog/scripts/bootstrap/frogc',
            'tools/create_sdk.py',
          ],
          'outputs': [
            '<(PRODUCT_DIR)/dart-sdk',
          ],
          'action': [
            'python',
            'tools/create_sdk.py',
            '<(PRODUCT_DIR)/dart-sdk',
          ],
          'message': 'Creating SDK.',
        },
      ],
    },
    {
      'target_name': 'upload_sdk',
      'type': 'none',
      'conditions': [
        ['OS=="win"', {
          'msvs_cygwin_dirs': ['<(cygwin_dir)'],
        }],
      ],
      'dependencies': [
        'create_sdk',
      ],
      'actions': [
        {
          'action_name': 'upload_sdk_py',
          'inputs': [
            '<(PRODUCT_DIR)/dart-sdk',
            'tools/upload_sdk.py',
          ],
          'outputs': [
            '<(PRODUCT_DIR)/upload_sdk',
          ],
          'action': [
            'python',
            'tools/upload_sdk.py',
            '<(PRODUCT_DIR)/dart-sdk'
          ],
        },
      ],
    }
  ],
}
