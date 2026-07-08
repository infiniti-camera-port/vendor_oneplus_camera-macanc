#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

module = ExtractUtilsModule(
    'camera-macanc',
    'oneplus',
    device_rel_path='vendor/oneplus/camera-macanc',
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
