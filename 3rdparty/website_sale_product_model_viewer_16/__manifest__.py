# Copyright 2020 Lorenzo Battistini @ TAKOBI
# Copyright 2020 Andrea Piovesana @ Openindustry.it
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "eCommerce: Product model viewer",
    "summary": "3D model viewer for e-commerce products",
    "version": "16.0.3.0.0",
    "development_status": "Beta",
    "category": "Website",
    "website": "https://github.com/OCA/e-commerce",
    "author": "TAKOBI, Openindustry.it, Odoo Community Association (OCA)",
    "maintainers": ["eLBati"],
    "license": "AGPL-3",
    "depends": [
        "web",
        "product_model_viewer_16",
        "website_sale",
    ],
    "assets": {
        "web.assets_frontend": [
            "/website_sale_product_model_viewer_16/static/src/js/product_model_viewer.js",
            "/web_widget_model_viewer_16/static/lib/model-viewer-legacy.js",
        ],
    },
    "data": [
        "views/frontend_templates.xml",
    ],
    "application": False,
    "installable": True,
}
