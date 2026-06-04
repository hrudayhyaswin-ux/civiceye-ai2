# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

import os

HEADER = """# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

"""

JS_HEADER = """/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

"""

def add_header(filepath, header):
    with open(filepath) as f:
        content = f.read()
    if content.startswith(header.strip()[:20]):
        return
    with open(filepath, 'w') as f:
        f.write(header + content)

for root, dirs, files in os.walk('.'):
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    if '.venv' in dirs:
        dirs.remove('.venv')
    if '.git' in dirs:
        dirs.remove('.git')

    for file in files:
        if file.endswith('.py'):
            add_header(os.path.join(root, file), HEADER)
        elif file.endswith('.js') or file.endswith('.jsx'):
            add_header(os.path.join(root, file), JS_HEADER)
