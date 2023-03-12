odoo.define("website_sale_product_model_viewer", function (require) {
    "use strict";
    require("web.core");

    $(document).ready(function () {
        var $fullscreen_button = $("#product-3d-model-viewer-fullscreen");
        $fullscreen_button.click(function (ev) {
            var isFullscreenAvailable = document.fullscreenEnabled;
            false;
            var modelViewerElem = ev.target.parentElement.parentElement.parentElement;
            if (isFullscreenAvailable) {
                var fullscreenElement = document.fullscreenElement;
                if (fullscreenElement) {
                    if (document.exitFullscreen) {
                        document.exitFullscreen();
                    }
                } else if (modelViewerElem.requestFullscreen) {
                    modelViewerElem.requestFullscreen();
                }
            } else {
                console.error("ERROR : full screen not supported by web browser");
            }
        });
    });
});
