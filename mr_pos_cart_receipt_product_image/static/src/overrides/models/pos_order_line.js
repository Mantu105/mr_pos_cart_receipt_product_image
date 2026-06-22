import { patch } from "@web/core/utils/patch";
import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";

/**
 * Add the product image to the data consumed by the generic Orderline
 * component. This drives the image shown on the POS cart order lines.
 *
 * The generic `point_of_sale.Orderline` template already renders
 * `line.imageSrc` when it is set, so we only have to populate it.
 */
patch(PosOrderline.prototype, {
    getDisplayData() {
        const data = super.getDisplayData(...arguments);
        if (this.config.iface_image_orderline && this.product_id) {
            data.imageSrc = `/web/image/product.product/${this.product_id.id}/image_128`;
        }
        return data;
    },
});
