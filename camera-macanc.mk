# OnePlus Ace 6T (macanc) per-device camera config.
#
# Variant-specific camera payloads and configuration belong in this camera tier,
# while this scaffold inherits the SM8850 common camera surface.

$(call inherit-product, vendor/oneplus/camera-sm8850-common/camera-sm8850-common.mk)

$(call inherit-product, proprietary/vendor/oneplus/camera-macanc/camera-macanc-vendor.mk)

PRODUCT_PRODUCT_PROPERTIES += \
    ro.build.version.ota=PLR110_11.A.62_0620_202606152334
